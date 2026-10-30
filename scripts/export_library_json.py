#!/usr/bin/env python3
"""
scripts/export_library_json.py
Parses the Pakistan Data Resource Inventory Excel workbook and CSV into a clean,
structured JSON catalog at assets/data/pakistan_library_catalog.json.
Uses standard library only (zipfile + xml.etree.ElementTree).
"""

import os
import sys
import json
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XLSX_PATH = os.path.join(ROOT_DIR, "build library", "Pakistan_Data_Resource_Inventory.xlsx")
OUTPUT_JSON_PATH = os.path.join(ROOT_DIR, "assets", "data", "pakistan_library_catalog.json")

def parse_url_entries(text):
    """
    Extracts structured {label, url, type} objects from multi-line text
    containing URLs with or without labels.
    """
    if not text:
        return []
    
    entries = []
    lines = [line.strip() for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n") if line.strip()]
    
    for line in lines:
        url_match = re.search(r'(https?://[^\s\'"<>]+)', line)
        if not url_match:
            continue
        clean_url = url_match.group(1).rstrip(".,;)")
        label = line[:url_match.start()].strip().rstrip(":-–— ")
        if not label:
            label = "Direct Link"
            
        # Determine format badge
        low_url = clean_url.lower()
        low_label = label.lower()
        fmt = "Web"
        if ".zip" in low_url or "zip" in low_label:
            fmt = "ZIP"
        elif ".xlsx" in low_url or ".xls" in low_url or "excel" in low_label:
            fmt = "Excel"
        elif ".csv" in low_url or "csv" in low_label:
            fmt = "CSV"
        elif ".pdf" in low_url or "pdf" in low_label:
            fmt = "PDF"
        elif "stata" in low_label or ".dta" in low_url:
            fmt = "Stata"
        elif "spss" in low_label or ".sav" in low_url:
            fmt = "SPSS"
        elif "api" in low_url or "api" in low_label:
            fmt = "API"
            
        entries.append({
            "label": label,
            "url": clean_url,
            "format": fmt
        })
    return entries

def parse_xlsx(file_path):
    ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    z = zipfile.ZipFile(file_path, 'r')
    
    shared_strings = []
    if 'xl/sharedStrings.xml' in z.namelist():
        sst_tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
        for si in sst_tree.findall('s:si', ns):
            text = ''.join(t.text for t in si.findall('.//s:t', ns) if t.text)
            shared_strings.append(text)
            
    wb = ET.fromstring(z.read('xl/workbook.xml'))
    sheet_meta = []
    for s in wb.findall('.//s:sheet', ns):
        sheet_meta.append({
            'name': s.attrib['name'],
            'sheet_id': s.attrib['sheetId'],
            'r_id': s.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
        })
        
    sheets_data = {}
    for i, meta in enumerate(sheet_meta, 1):
        target = f'xl/worksheets/sheet{i}.xml'
        if target not in z.namelist():
            continue
        sheet_tree = ET.fromstring(z.read(target))
        rows = []
        for row in sheet_tree.findall('.//s:row', ns):
            row_vals = []
            for c in row.findall('s:c', ns):
                t = c.attrib.get('t')
                v = c.find('s:v', ns)
                val = ''
                if v is not None and v.text is not None:
                    if t == 's':
                        idx = int(v.text)
                        val = shared_strings[idx] if idx < len(shared_strings) else ''
                    else:
                        val = v.text
                elif t == 'inlineStr':
                    is_tag = c.find('s:is', ns)
                    if is_tag is not None:
                        t_tag = is_tag.find('s:t', ns)
                        if t_tag is not None and t_tag.text:
                            val = t_tag.text
                row_vals.append(val.strip())
            # Strip trailing empty strings
            while row_vals and not row_vals[-1]:
                row_vals.pop()
            if any(row_vals):
                rows.append(row_vals)
        sheets_data[meta['name']] = rows
        
    return sheets_data

def process_start_here(rows):
    top_stack = []
    credibility_rules = {}
    in_top_stack = False
    in_rules = False
    
    for r in rows:
        if not r:
            continue
        line = ' | '.join(r)
        if 'Best first-pass acquisition stack' in line:
            in_top_stack = True
            in_rules = False
            continue
        if 'Credibility grades and interpretation rules' in line:
            in_top_stack = False
            in_rules = True
            continue
            
        if in_top_stack:
            if r[0] == 'Order' or not r[0].isdigit():
                continue
            top_stack.append({
                'order': int(r[0]),
                'resource': r[1] if len(r) > 1 else '',
                'why_get_it_first': r[2] if len(r) > 2 else '',
                'format_access': r[3] if len(r) > 3 else '',
                'landing_page': r[4] if len(r) > 4 else '',
                'direct_links_note': r[5] if len(r) > 5 else '',
                'suggested_topic': r[6] if len(r) > 6 else '',
                'grade': r[7] if len(r) > 7 else 'A1'
            })
            
        elif in_rules:
            if len(r) >= 2 and ('A1' in r[0] or 'A2' in r[0] or 'B' in r[0] or 'C' in r[0]):
                grade_key = r[0].split('—')[0].strip().split()[0]
                credibility_rules[grade_key] = {
                    'title': r[0],
                    'description': r[1]
                }
                
    return {'top_stack': top_stack, 'credibility_rules': credibility_rules}

def process_master_catalog(rows):
    if not rows:
        return []
    items = []
    
    for r in rows[1:]:
        if not r or not r[0].startswith('PKD-'):
            continue
        direct_entries = parse_url_entries(r[6] if len(r) > 6 else '')
        item = {
            'id': r[0],
            'grade': r[1] if len(r) > 1 else '',
            'topic': r[2] if len(r) > 2 else '',
            'title': r[3] if len(r) > 3 else '',
            'publisher': r[4] if len(r) > 4 else '',
            'landing_page': r[5] if len(r) > 5 else '',
            'direct_entries': direct_entries,
            'direct_urls': [e['url'] for e in direct_entries],
            'formats_access': r[7] if len(r) > 7 else '',
            'period_coverage': r[8] if len(r) > 8 else '',
            'geographic_detail': r[9] if len(r) > 9 else '',
            'research_uses': r[10] if len(r) > 10 else '',
            'caveats': r[11] if len(r) > 11 else '',
            'verification_note': r[12] if len(r) > 12 else '',
            'suggested_priority': r[13] if len(r) > 13 else 'P2',
            'acquisition_status': r[14] if len(r) > 14 else 'Not started'
        }
        items.append(item)
    return items

def process_download_queue(rows):
    if not rows:
        return []
    items = []
    for r in rows[1:]:
        if not r or not r[0].startswith('Q-'):
            continue
        direct_entries = parse_url_entries(r[6] if len(r) > 6 else '')
        item = {
            'queue_id': r[0],
            'grade': r[1] if len(r) > 1 else '',
            'priority': r[2] if len(r) > 2 else '',
            'resource_family': r[3] if len(r) > 3 else '',
            'topic': r[4] if len(r) > 4 else '',
            'landing_page': r[5] if len(r) > 5 else '',
            'direct_entries': direct_entries,
            'direct_urls': [e['url'] for e in direct_entries],
            'formats': r[7] if len(r) > 7 else '',
            'coverage': r[8] if len(r) > 8 else '',
            'caution': r[9] if len(r) > 9 else '',
            'status': r[10] if len(r) > 10 else 'Not started'
        }
        items.append(item)
    return items

def process_topic_map(rows):
    if not rows:
        return []
    items = []
    for r in rows[1:]:
        if not r or len(r) < 2:
            continue
        domain = r[0].strip()
        if not domain or domain.lower() == 'research domain / topic':
            continue
        item = {
            'domain': domain,
            'primary_official': r[1] if len(r) > 1 else '',
            'target_official_file': r[2] if len(r) > 2 else '',
            'external_comparators': r[3] if len(r) > 3 else '',
            'geographic_detail': r[4] if len(r) > 4 else '',
            'analytical_uses': r[5] if len(r) > 5 else '',
            'method_caveats': r[6] if len(r) > 6 else ''
        }
        items.append(item)
    return items

def process_acquisition_workflow(rows):
    if not rows:
        return []
    items = []
    for r in rows[1:]:
        if not r or not r[0].isdigit():
            continue
        item = {
            'step': int(r[0]),
            'checkpoint': r[1] if len(r) > 1 else '',
            'what_to_do': r[2] if len(r) > 2 else '',
            'evidence_to_save': r[3] if len(r) > 3 else '',
            'status': r[4] if len(r) > 4 else 'Not started'
        }
        items.append(item)
    return items

def main():
    print(f"Reading workbook: {XLSX_PATH}")
    if not os.path.exists(XLSX_PATH):
        print(f"Error: {XLSX_PATH} does not exist.")
        sys.exit(1)
        
    sheets = parse_xlsx(XLSX_PATH)
    start_here = process_start_here(sheets.get('Start Here', []))
    master_catalog = process_master_catalog(sheets.get('Master Catalog', []))
    download_queue = process_download_queue(sheets.get('Download Queue', []))
    topic_map = process_topic_map(sheets.get('Topic Map', []))
    workflow = process_acquisition_workflow(sheets.get('Acquisition Workflow', []))
    
    # Enrich master catalog with queue references
    queue_map = {q['resource_family'].lower(): q['queue_id'] for q in download_queue}
    for item in master_catalog:
        title_lower = item['title'].lower()
        matched_queue_id = None
        for q_title, q_id in queue_map.items():
            if q_title in title_lower or title_lower in q_title:
                matched_queue_id = q_id
                break
        item['matched_queue_id'] = matched_queue_id

    # Compute summary statistics
    stats = {
        'total_resources': len(master_catalog),
        'by_grade': {
            'A1': sum(1 for i in master_catalog if i['grade'] == 'A1'),
            'A2': sum(1 for i in master_catalog if i['grade'] == 'A2'),
            'B': sum(1 for i in master_catalog if i['grade'] == 'B'),
            'C': sum(1 for i in master_catalog if i['grade'] == 'C'),
        },
        'by_priority': {
            'P1': sum(1 for i in master_catalog if i['suggested_priority'] == 'P1'),
            'P2': sum(1 for i in master_catalog if i['suggested_priority'] == 'P2'),
            'P3': sum(1 for i in master_catalog if i['suggested_priority'] == 'P3'),
        },
        'with_direct_links': sum(1 for i in master_catalog if i['direct_urls']),
        'total_download_queue': len(download_queue),
        'total_topic_domains': len(topic_map),
        'total_workflow_steps': len(workflow)
    }
    
    data_bundle = {
        'metadata': {
            'title': 'Pakistan Data Resource Inventory',
            'version': '1.0.0',
            'date': '2026-10-28',
            'publisher': 'Pakistan Provincial Reform Institute (PPRI)',
            'stats': stats,
            'credibility_rules': start_here['credibility_rules']
        },
        'top_stack': start_here['top_stack'],
        'workflow': workflow,
        'topic_map': topic_map,
        'download_queue': download_queue,
        'catalog': master_catalog
    }
    
    os.makedirs(os.path.dirname(OUTPUT_JSON_PATH), exist_ok=True)
    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data_bundle, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {OUTPUT_JSON_PATH}")
    print(f"Summary: {stats['total_resources']} resources, {stats['total_download_queue']} download queue items, {stats['total_topic_domains']} topic domains, {stats['total_workflow_steps']} workflow checkpoints.")

if __name__ == '__main__':
    main()

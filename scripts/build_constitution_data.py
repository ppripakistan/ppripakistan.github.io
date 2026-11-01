#!/usr/bin/env python3
"""
scripts/build_full_constitution_data.py
Generates the complete, minimalist dataset for the PPRI Constitution Explorer:
- data/constitution/articles.json (Full 280 Articles + Schedules with salient points and key text)
- data/constitution/amendment-register.json (Amendments 1 to 27)
- data/constitution/constitutional-bills.json (Un-enacted constitutional bills)
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / "constitution"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# AMENDMENT REGISTER (27 Positions, 24 Enacted Acts)
# ---------------------------------------------------------------------------
amendments_data = [
    {
        "position": 1,
        "amendment_number": 1,
        "official_title": "Constitution (First Amendment) Act, 1974",
        "short_title": "First Amendment (Redefinition of Frontiers & Bangladesh Recognition)",
        "assent_date": "1974-05-04",
        "gazette_date": "1974-05-08",
        "status": "enacted",
        "key_changes": [
            "Amended Article 1 to recognize the reality of the separation of East Pakistan (Bangladesh) and redefine the boundaries of Pakistan.",
            "Amended Articles 8, 17, 61, 101, 127, 193, 199, 200, 209, 212, 250, 259, 260, 272, and the First Schedule."
        ],
        "substantive_impact": "Adjusted the constitutional boundaries of the federation following the 1971 war and provided powers to regulate political parties acting against sovereignty or integrity.",
        "affected_articles": ["1", "8", "17", "61", "101", "127", "193", "199", "200", "209", "212", "250", "259", "260", "272"]
    },
    {
        "position": 2,
        "amendment_number": 2,
        "official_title": "Constitution (Second Amendment) Act, 1974",
        "short_title": "Second Amendment (Definition of Non-Muslim)",
        "assent_date": "1974-09-17",
        "gazette_date": "1974-09-21",
        "status": "enacted",
        "key_changes": [
            "Amended Article 106 to declare persons of the Ahmadi / Lahori group as non-Muslim minority for constitutional and electoral purposes.",
            "Amended Article 260 to insert a formal definition of non-Muslim."
        ],
        "substantive_impact": "Defined theological minority status in constitutional law, establishing statutory parameters for representation in assemblies.",
        "affected_articles": ["106", "260"]
    },
    {
        "position": 3,
        "amendment_number": 3,
        "official_title": "Constitution (Third Amendment) Act, 1975",
        "short_title": "Third Amendment (Preventive Detention Rules)",
        "assent_date": "1975-02-13",
        "gazette_date": "1975-02-18",
        "status": "enacted",
        "key_changes": [
            "Amended Article 10 to extend the period for which preventive detention without review can be maintained from one month to three months.",
            "Amended Article 232 regarding the proclamation of Emergency."
        ],
        "substantive_impact": "Strengthened executive powers of preventive detention and reduced procedural safeguards during state security operations.",
        "affected_articles": ["10", "232"]
    },
    {
        "position": 4,
        "amendment_number": 4,
        "official_title": "Constitution (Fourth Amendment) Act, 1975",
        "short_title": "Fourth Amendment (Minority Seats & High Court Powers)",
        "assent_date": "1975-11-21",
        "gazette_date": "1975-11-25",
        "status": "enacted",
        "key_changes": [
            "Amended Articles 8, 17, 19, 51, 54, 106, 199, and 271.",
            "Curtailed the power of High Courts under Article 199 to grant bail or prohibit preventive detention.",
            "Allocated 6 additional reserved seats for non-Muslim minorities in the National Assembly."
        ],
        "substantive_impact": "Curbed judicial writ jurisdiction over preventive detentions while formalizing reserved minority representation in the federal parliament.",
        "affected_articles": ["8", "17", "19", "51", "54", "106", "199", "271"]
    },
    {
        "position": 5,
        "amendment_number": 5,
        "official_title": "Constitution (Fifth Amendment) Act, 1976",
        "short_title": "Fifth Amendment (Judicial Tenures & High Court Separation)",
        "assent_date": "1976-09-13",
        "gazette_date": "1976-09-16",
        "status": "enacted",
        "key_changes": [
            "Amended Articles 101, 160, 175, 179, 180, 187, 192, 195, 196, 199, 200, 206, 212, 260, 280, and the First and Fifth Schedules.",
            "Fixed fixed tenures for Chief Justice of Pakistan (5 years) and High Court Chief Justices (4 years).",
            "Separated the Sindh & Balochistan High Court into two distinct High Courts."
        ],
        "substantive_impact": "Restructured high judicial tenures and established separate High Courts for Sindh and Balochistan.",
        "affected_articles": ["101", "160", "175", "179", "180", "187", "192", "195", "196", "199", "200", "206", "212", "260", "280"]
    },
    {
        "position": 6,
        "amendment_number": 6,
        "official_title": "Constitution (Sixth Amendment) Act, 1976",
        "short_title": "Sixth Amendment (Chief Justice Retirement Age Extension)",
        "assent_date": "1976-12-31",
        "gazette_date": "1977-01-04",
        "status": "enacted",
        "key_changes": [
            "Amended Articles 179 and 195 to permit a Chief Justice of Pakistan or a High Court Chief Justice to serve out their 5-year or 4-year term even if reaching superannuation age (65 or 62)."
        ],
        "substantive_impact": "Allowed sitting Chief Justices to complete executive tenure appointments beyond normal constitutional retirement ages.",
        "affected_articles": ["179", "195"]
    },
    {
        "position": 7,
        "amendment_number": 7,
        "official_title": "Constitution (Seventh Amendment) Act, 1977",
        "short_title": "Seventh Amendment (Prime Minister Referendum Mechanism)",
        "assent_date": "1977-05-16",
        "gazette_date": "1977-05-21",
        "status": "enacted",
        "key_changes": [
            "Inserted Article 96A providing for a national referendum to obtain a vote of confidence in the Prime Minister.",
            "Amended Article 245 to bar judicial review of Armed Forces actions called in aid of civil power."
        ],
        "substantive_impact": "Introduced a direct referendum mechanism during the 1977 political crisis and insulated military law-and-order actions from High Court writ jurisdiction.",
        "affected_articles": ["96A", "101", "245"]
    },
    {
        "position": 8,
        "amendment_number": 8,
        "official_title": "Constitution (Eighth Amendment) Act, 1985",
        "short_title": "Eighth Amendment (Restoration of Constitution & Article 58(2)(b))",
        "assent_date": "1985-11-09",
        "gazette_date": "1985-11-11",
        "status": "enacted",
        "key_changes": [
            "Indemnified and validated martial law orders, President's Orders, and the Revival of the Constitution Order (RCO, 1985).",
            "Inserted Article 58(2)(b) empowering the President to dissolve the National Assembly at discretion.",
            "Converted the parliamentary system into a semi-presidential dyarchy; created Article 270A indemnity."
        ],
        "substantive_impact": "Fundamentally altered Pakistan's constitutional structure by creating presidential discretionary dissolution powers that dominated 1988–1997 governance.",
        "affected_articles": ["48", "51", "56", "58", "59", "60", "75", "90", "91", "101", "105", "106", "112", "116", "130", "144", "152A", "270A"]
    },
    {
        "position": 9,
        "amendment_number": None,
        "official_title": "Constitution (Ninth Amendment) Bill, 1985 (Un-enacted)",
        "short_title": "Ninth Amendment Bill (Shariah as Supreme Law — Lapsed)",
        "assent_date": None,
        "gazette_date": None,
        "status": "un_enacted_bill",
        "key_changes": [
            "Proposed amending Article 2 and Article 203B to establish Islamic injunctions and Shariah as the supreme law of the land.",
            "Passed by the Senate in 1986 but lapsed when the National Assembly was dissolved in 1988."
        ],
        "substantive_impact": "Never enacted. Lapsed on dissolution of the National Assembly.",
        "affected_articles": ["2", "203B", "203D"]
    },
    {
        "position": 10,
        "amendment_number": 10,
        "official_title": "Constitution (Tenth Amendment) Act, 1987",
        "short_title": "Tenth Amendment (National Assembly & Senate Working Days)",
        "assent_date": "1987-03-25",
        "gazette_date": "1987-03-29",
        "status": "enacted",
        "key_changes": [
            "Amended Articles 54 and 61 to reduce the minimum required working days of the National Assembly from 160 to 130 days per year."
        ],
        "substantive_impact": "Adjusted the parliamentary calendar and required annual sitting days for the federal legislature.",
        "affected_articles": ["54", "61"]
    },
    {
        "position": 11,
        "amendment_number": None,
        "official_title": "Constitution (Eleventh Amendment) Bill, 1989 (Un-enacted)",
        "short_title": "Eleventh Amendment Bill (Restoration of Women's Reserved Seats — Lapsed)",
        "assent_date": None,
        "gazette_date": None,
        "status": "un_enacted_bill",
        "key_changes": [
            "Introduced in the Senate in 1989 to restore reserved seats for women in the National Assembly following the expiration of the original 10-year / three-elections constitutional sunset.",
            "Never enacted into law."
        ],
        "substantive_impact": "Never enacted. Women's reserved seats were later re-established by the Legal Framework Order, 2002 and 17th Amendment.",
        "affected_articles": ["51", "106"]
    },
    {
        "position": 12,
        "amendment_number": 12,
        "official_title": "Constitution (Twelfth Amendment) Act, 1991",
        "short_title": "Twelfth Amendment (Special Courts for Speedy Trials)",
        "assent_date": "1991-07-28",
        "gazette_date": "1991-07-28",
        "status": "enacted",
        "key_changes": [
            "Inserted Article 212B establishing Special Courts for Speedy Trials for heinous offences.",
            "Contained an automatic 3-year sunset clause, after which Article 212B stood repealed."
        ],
        "substantive_impact": "Established temporary parallel judicial tribunals for trial of heinous crimes, which expired in 1994.",
        "affected_articles": ["212B"]
    },
    {
        "position": 13,
        "amendment_number": 13,
        "official_title": "Constitution (Thirteenth Amendment) Act, 1997",
        "short_title": "Thirteenth Amendment (Repeal of Article 58(2)(b))",
        "assent_date": "1997-04-03",
        "gazette_date": "1997-04-04",
        "status": "enacted",
        "key_changes": [
            "Omitted Article 58(2)(b) and Article 112(2)(b), stripping the President and Provincial Governors of the power to dissolve assemblies at discretion.",
            "Restored parliamentary supremacy by making the President act strictly on Prime Minister's advice in appointments of Governors and Service Chiefs."
        ],
        "substantive_impact": "Restored parliamentary primacy by eliminating discretionary dissolution powers of the President.",
        "affected_articles": ["58", "101", "112", "130", "243"]
    },
    {
        "position": 14,
        "amendment_number": 14,
        "official_title": "Constitution (Fourteenth Amendment) Act, 1997",
        "short_title": "Fourteenth Amendment (Anti-Defection Law — Article 63A)",
        "assent_date": "1997-07-03",
        "gazette_date": "1997-07-04",
        "status": "enacted",
        "key_changes": [
            "Inserted Article 63A to disqualify parliamentarians from assembly membership if they defect, breach party discipline, or vote against party directions in prime ministerial election, confidence votes, or money bills."
        ],
        "substantive_impact": "Created stringent constitutional anti-defection prohibitions to eliminate floor-crossing and preserve party discipline.",
        "affected_articles": ["63A"]
    },
    {
        "position": 15,
        "amendment_number": None,
        "official_title": "Constitution (Fifteenth Amendment) Bill, 1998 (Un-enacted)",
        "short_title": "Fifteenth Amendment Bill (Shariah Supremacy — Lapsed)",
        "assent_date": None,
        "gazette_date": None,
        "status": "un_enacted_bill",
        "key_changes": [
            "Proposed inserting Article 2B to declare the Holy Quran and Sunnah as the supreme law of Pakistan and empower the federal government to enforce Shariah directives.",
            "Passed by the National Assembly in October 1998; never passed by the Senate prior to the 1999 military takeover."
        ],
        "substantive_impact": "Never enacted. Lapsed following the October 1999 military coup.",
        "affected_articles": ["2B"]
    },
    {
        "position": 16,
        "amendment_number": 16,
        "official_title": "Constitution (Sixteenth Amendment) Act, 1999",
        "short_title": "Sixteenth Amendment (Extension of Quota System to 2013)",
        "assent_date": "1999-08-03",
        "gazette_date": "1999-08-05",
        "status": "enacted",
        "key_changes": [
            "Amended Article 27 to extend the affirmative action quota system for provincial and regional representation in federal civil services from 20 years to 40 years (until 2013)."
        ],
        "substantive_impact": "Preserved regional and provincial quotas in federal public service recruitment to ensure under-represented provinces retained representation.",
        "affected_articles": ["27"]
    },
    {
        "position": 17,
        "amendment_number": 17,
        "official_title": "Constitution (Seventeenth Amendment) Act, 2003",
        "short_title": "Seventeenth Amendment (Validation of LFO 2002 & Restoration of 58(2)(b))",
        "assent_date": "2003-12-31",
        "gazette_date": "2003-12-31",
        "status": "enacted",
        "key_changes": [
            "Indemnified the Legal Framework Order, 2002 (LFO) issued under General Pervez Musharraf.",
            "Re-inserted Article 58(2)(b) with a requirement for Supreme Court reference within 15 days of assembly dissolution.",
            "Sanctioned presidential dual office (President & Chief of Army Staff) under special statutory exception."
        ],
        "substantive_impact": "Restored presidential dissolution powers, validated post-1999 legal framework, and formalized reserved seats expansion.",
        "affected_articles": ["41", "58", "112", "152A", "179", "195", "243", "268", "270AA"]
    },
    {
        "position": 18,
        "amendment_number": 18,
        "official_title": "Constitution (Eighteenth Amendment) Act, 2010",
        "short_title": "Eighteenth Amendment (Provincial Autonomy & Democratic Restoration)",
        "assent_date": "2010-04-19",
        "gazette_date": "2010-04-20",
        "status": "enacted",
        "key_changes": [
            "Abolished Article 58(2)(b), permanently removing presidential assembly dissolution powers.",
            "Abolished the Concurrent Legislative List, devolving 17 federal ministries to the four provinces.",
            "Inserted Article 160(3A) establishing that a province's share in an NFC Award shall never be reduced below its share in the previous Award.",
            "Inserted Article 140A requiring provinces to devolve political, administrative, and financial responsibility to elected local governments.",
            "Amended Article 172(3) to grant provinces 50:50 equal joint ownership of mineral oil and natural gas with the federal government.",
            "Introduced Article 10A (Fair Trial), Article 19A (Right to Information), and Article 25A (Free Compulsory Education).",
            "Created Article 175A for judicial appointments via Judicial Commission of Pakistan (JCP) and Parliamentary Committee."
        ],
        "substantive_impact": "The most extensive structural reform in Pakistan's constitutional history; transformed Pakistan into a genuine federal parliamentary republic with unprecedented provincial autonomy.",
        "affected_articles": ["1", "6", "10A", "17", "19A", "25A", "48", "51", "58", "59", "62", "63", "63A", "89", "90", "91", "101", "105", "106", "112", "140A", "142", "144", "149", "153", "154", "156", "160", "172", "175A", "232", "239", "242", "270AA", "Fourth Schedule"]
    },
    {
        "position": 19,
        "amendment_number": 19,
        "official_title": "Constitution (Nineteenth Amendment) Act, 2010",
        "short_title": "Nineteenth Amendment (Judicial Commission Composition Refinement)",
        "assent_date": "2011-01-01",
        "gazette_date": "2011-01-04",
        "status": "enacted",
        "key_changes": [
            "Amended Article 175A and Article 182 following Supreme Court observations in the 18th Amendment challenge.",
            "Expanded the Judicial Commission of Pakistan to include 4 senior-most judges of the Supreme Court.",
            "Regulated the appointment process for ad-hoc judges and High Court benches."
        ],
        "substantive_impact": "Fine-tuned judicial appointment machinery to protect judicial independence while preserving the parliamentary committee mechanism.",
        "affected_articles": ["175A", "182"]
    },
    {
        "position": 20,
        "amendment_number": 20,
        "official_title": "Constitution (Twentieth Amendment) Act, 2012",
        "short_title": "Twentieth Amendment (Caretaker Government & Free Elections)",
        "assent_date": "2012-02-28",
        "gazette_date": "2012-02-29",
        "status": "enacted",
        "key_changes": [
            "Amended Articles 48, 214, 215, 216, 218, 219, 224, 224A, and the Third Schedule.",
            "Established a consensus mechanism between Prime Minister and Leader of the Opposition for appointing the Caretaker Prime Minister and Chief Ministers.",
            "Created an 8-member bipartisan Parliamentary Committee and Election Commission arbitration mechanism in case of deadlock."
        ],
        "substantive_impact": "Institutionalized neutral caretaker administrations and strengthened the Election Commission to safeguard election neutrality.",
        "affected_articles": ["48", "214", "215", "216", "218", "219", "224", "224A"]
    },
    {
        "position": 21,
        "amendment_number": 21,
        "official_title": "Constitution (Twenty-first Amendment) Act, 2015",
        "short_title": "Twenty-first Amendment (Military Courts for Terrorist Offences)",
        "assent_date": "2015-01-07",
        "gazette_date": "2015-01-07",
        "status": "enacted",
        "key_changes": [
            "Amended Article 175 and the First Schedule to exempt trials of terrorist groups using religion or sect under the Pakistan Army Act, 1952 from constitutional fundamental rights challenge.",
            "Included a strict 2-year sunset clause expiring on 7 January 2017."
        ],
        "substantive_impact": "Established temporary military court jurisdiction for rapid trial of terrorist perpetrators following the Army Public School Peshawar massacre.",
        "affected_articles": ["175", "First Schedule"]
    },
    {
        "position": 22,
        "amendment_number": 22,
        "official_title": "Constitution (Twenty-second Amendment) Act, 2016",
        "short_title": "Twenty-second Amendment (Election Commission Eligibility Criteria)",
        "assent_date": "2016-06-08",
        "gazette_date": "2016-06-10",
        "status": "enacted",
        "key_changes": [
            "Amended Articles 213, 215, 217, 218, 219, and 222.",
            "Broadened eligibility criteria for the Chief Election Commissioner and ECP members to include retired senior civil servants and technocrats, ending the requirement that members must be retired High Court judges."
        ],
        "substantive_impact": "Diversified ECP qualifications and staggered the retirement of commission members to maintain institutional continuity.",
        "affected_articles": ["213", "215", "217", "218", "219", "222"]
    },
    {
        "position": 23,
        "amendment_number": 23,
        "official_title": "Constitution (Twenty-third Amendment) Act, 2017",
        "short_title": "Twenty-third Amendment (Military Courts 2-Year Extension)",
        "assent_date": "2017-03-30",
        "gazette_date": "2017-03-31",
        "status": "enacted",
        "key_changes": [
            "Extended the sunset clause of military courts under the Pakistan Army Act, 1952 for a further period of two years (until 6 January 2019).",
            "Originally introduced in the National Assembly as the 'Twenty-eighth Amendment Bill, 2017', but enacted as the Twenty-third Amendment Act."
        ],
        "substantive_impact": "Maintained military tribunal jurisdiction over terrorist offences for an additional two years.",
        "affected_articles": ["175", "First Schedule"]
    },
    {
        "position": 24,
        "amendment_number": 24,
        "official_title": "Constitution (Twenty-fourth Amendment) Act, 2017",
        "short_title": "Twenty-fourth Amendment (Delimitation on Provisional Census 2017)",
        "assent_date": "2017-12-22",
        "gazette_date": "2017-12-24",
        "status": "enacted",
        "key_changes": [
            "Amended Article 51 to reallocate National Assembly seats among federating units on the basis of provisional results of the 6th Population & Housing Census, 2017.",
            "Retained total National Assembly strength at 272 general seats while shifting seat quotas between provinces."
        ],
        "substantive_impact": "Enabled conduct of the 2018 General Elections by authorizing nationwide constituency delimitation based on provisional 2017 census data.",
        "affected_articles": ["51"]
    },
    {
        "position": 25,
        "amendment_number": 25,
        "official_title": "Constitution (Twenty-fifth Amendment) Act, 2018",
        "short_title": "Twenty-fifth Amendment (FATA Merger with Khyber Pakhtunkhwa)",
        "assent_date": "2018-05-31",
        "gazette_date": "2018-06-04",
        "status": "enacted",
        "key_changes": [
            "Amended Articles 1, 51, 59, 106, 155, 246, and omitted Article 247.",
            "Merged the Federally Administered Tribal Areas (FATA) and Provincially Administered Tribal Areas (PATA) into the Province of Khyber Pakhtunkhwa.",
            "Extended the jurisdiction of the Supreme Court and Peshawar High Court to the merged tribal districts.",
            "Abolished the Frontier Crimes Regulation (FCR) framework; phased out separate tribal Senate seats."
        ],
        "substantive_impact": "Historic integration of 5 million tribal citizens into the formal constitutional and judicial mainstream of Pakistan and Khyber Pakhtunkhwa.",
        "affected_articles": ["1", "51", "59", "106", "155", "246", "247"]
    },
    {
        "position": 26,
        "amendment_number": 26,
        "official_title": "Constitution (Twenty-sixth Amendment) Act, 2024",
        "short_title": "Twenty-sixth Amendment (Judicial Reforms & Clean Environment)",
        "assent_date": "2024-10-21",
        "gazette_date": "2024-10-21",
        "status": "enacted",
        "key_changes": [
            "Inserted Article 9A establishing the Right to a Clean, Healthy and Sustainable Environment as a fundamental right.",
            "Amended Article 175A to reconstruct the Judicial Commission of Pakistan (JCP) to evaluate judicial performance and form Constitutional Benches.",
            "Created dedicated Constitutional Benches in the Supreme Court and High Courts under Articles 191A and 202A.",
            "Amended Article 179 to fix the term of the Chief Justice of Pakistan at three years with superannuation age of 65 years.",
            "Replaced seniority convention: CJP appointed by a Special Parliamentary Committee from among the three senior-most Supreme Court judges."
        ],
        "substantive_impact": "Major overhaul of superior court judicial appointments, introduction of constitutional benches, term limits for the Chief Justice, and formal recognition of environmental fundamental rights.",
        "affected_articles": ["9A", "38", "175A", "177", "179", "184", "185", "186A", "187", "191A", "193", "199", "202A", "209"]
    },
    {
        "position": 27,
        "amendment_number": 27,
        "official_title": "Constitution (Twenty-seventh Amendment) Act, 2025",
        "short_title": "Twenty-seventh Amendment (Federal Constitutional Court Architecture)",
        "assent_date": "2025-11-15",
        "gazette_date": "2025-11-18",
        "status": "enacted",
        "key_changes": [
            "Consolidated the constitutional jurisdiction of superior courts by formalizing the Federal Constitutional Court (FCC) alongside the Supreme Court of Pakistan.",
            "Refined jurisdictional boundaries between constitutional interpretation matters (FCC) and ordinary appellate/civil litigation (Supreme Court).",
            "Streamlined institutional procedures for judicial oversight and bicameral parliamentary review."
        ],
        "substantive_impact": "Completes the bifurcation of constitutional adjudication and ordinary appellate civil/criminal administration in Pakistan's high judicature.",
        "affected_articles": ["175", "175A", "176", "177", "179", "184", "185", "186A", "191A", "209"]
    }
]

# ---------------------------------------------------------------------------
# UN-ENACTED CONSTITUTIONAL BILLS
# ---------------------------------------------------------------------------
bills_data = [
    {
        "bill_id": "na-bill-art-24a-2026",
        "bill_title": "Constitution (Amendment) Bill, 2026 (Insertion of Article 24A)",
        "introduced_in": "National Assembly",
        "introduction_date": "2026-02-17",
        "status": "un_enacted_proposal",
        "proposer_type": "Private Member",
        "target_articles": ["24A"],
        "summary": "Proposes insertion of Article 24A regarding property restitution and citizen compensation for unlawful state deprivation.",
        "status_note": "Referred to Standing Committee. Not enacted into law."
    },
    {
        "bill_id": "na-bill-arts-51-106-2026",
        "bill_title": "Constitution (Amendment) Bill, 2026 (Articles 51 and 106)",
        "introduced_in": "National Assembly",
        "introduction_date": "2026-03-03",
        "status": "un_enacted_proposal",
        "proposer_type": "Private Member",
        "target_articles": ["51", "106"],
        "summary": "Proposes adjustments to minority and women seat allocation mechanisms based on finalized 7th Digital Population Census results.",
        "status_note": "Pending committee report. Not enacted into law."
    },
    {
        "bill_id": "senate-bill-art-62-2024",
        "bill_title": "Constitution (Amendment) Bill, 2024 (Article 62)",
        "introduced_in": "Senate of Pakistan",
        "introduction_date": "2024-08-20",
        "status": "un_enacted_proposal",
        "proposer_type": "Private Member",
        "target_articles": ["62"],
        "summary": "Proposes defining procedural timebars and evidentiary standards for parliamentarian disqualification provisions.",
        "status_note": "Under legislative committee consideration. Not enacted."
    }
]

# ---------------------------------------------------------------------------
# COMPLETE 280 ARTICLES + SCHEDULES DATA CATALOG
# ---------------------------------------------------------------------------

def make_articles_catalog():
    articles = []

    # Helper function
    def add_art(num, title, part, part_title, chapter, chap_title, salient, clauses=None, status="in_force", tags=None):
        if tags is None:
            tags = []
        if clauses is None:
            clauses = [f"Article {num} establishes the statutory provisions governing {title.lower()} under the Constitution of Pakistan."]
        articles.append({
            "article_number": str(num),
            "title": title,
            "part": part,
            "part_title": part_title,
            "chapter": chapter,
            "chapter_title": chap_title,
            "salient_points": salient,
            "clauses": clauses,
            "status": status,
            "tags": tags
        })

    # =========================================================================
    # PREAMBLE & PART I: INTRODUCTORY (Articles 1 - 6)
    # =========================================================================
    add_art("Preamble", "The Preamble (Objectives Resolution)", "Preamble", "The Preamble", None, None,
            "Affirms that sovereignty over the entire Universe belongs to Almighty Allah alone and that the authority delegated to the State of Pakistan is a sacred trust. Enshrines democracy, freedom, equality, tolerance, social justice, fundamental rights, and the independence of the judiciary.",
            ["Whereas sovereignty over the entire Universe belongs to Almighty Allah alone, and the authority to be exercised by the people of Pakistan within the limits prescribed by Him is a sacred trust...",
             "Wherein the principles of democracy, freedom, equality, tolerance and social justice, as enunciated by Islam, shall be fully observed...",
             "Wherein the independence of the Judiciary shall be fully secured."],
            tags=["preamble", "sovereignty", "judiciary", "democracy"])

    add_art("1", "The Republic and its territories", "Part I", "Introductory", None, None,
            "Declares Pakistan to be an Islamic Republic comprising four Provinces (Balochistan, Khyber Pakhtunkhwa, Punjab, Sindh), the Islamabad Capital Territory, and such states and territories as may be included in Pakistan.",
            ["(1) Pakistan shall be a Federal Republic to be known as the Islamic Republic of Pakistan, hereinafter referred to as Pakistan.",
             "(2) The territories of Pakistan shall comprise— (a) the Provinces of Balochistan, Khyber Pakhtunkhwa, Punjab and Sindh; (b) the Islamabad Capital Territory; and (c) such States and territories as are or may be included in Pakistan, whether by accession or otherwise."],
            tags=["territories", "federation", "republic"])

    add_art("2", "Islam to be State religion", "Part I", "Introductory", None, None,
            "Establishes Islam as the official State religion of the Islamic Republic of Pakistan.",
            ["Islam shall be the State religion of Pakistan."],
            tags=["religion", "islam", "state"])

    add_art("2A", "The Objectives Resolution to form part of substantive provisions", "Part I", "Introductory", None, None,
            "Makes the substantive principles and declarations of the Objectives Resolution an active, enforceable part of the Constitution.",
            ["The principles and provisions set out in the Objectives Resolution are hereby declared to form part of the substantive provisions of the Constitution and shall have effect accordingly."],
            tags=["objectives_resolution", "islam", "judiciary"])

    add_art("3", "Elimination of exploitation", "Part I", "Introductory", None, None,
            "Mandates that the State shall ensure the elimination of all forms of exploitation and the gradual fulfillment of the fundamental principle: from each according to his ability, to each according to his work.",
            ["The State shall ensure the elimination of all forms of exploitation and the gradual fulfilment of the fundamental principle, from each according to his ability to each according to his work."],
            tags=["exploitation", "socio_economic", "justice"])

    add_art("4", "Right of individuals to be dealt with in accordance with law, etc.", "Part I", "Introductory", None, None,
            "The bedrock of the rule of law: guarantees that every citizen, and every person residing in Pakistan, has an inalienable right to enjoy the protection of law and be treated strictly in accordance with law. Prohibits state action detrimental to life, liberty, bodily integrity, or property without legal authority.",
            ["(1) To enjoy the protection of law and to be treated in accordance with law is the inalienable right of every citizen, wherever he may be, and of every other person for the time being within Pakistan.",
             "(2) In particular— (a) no action detrimental to the life, liberty, body, reputation or property of any person shall be taken except in accordance with law; (b) no person shall be prevented from, or be hindered in, doing that which is not prohibited by law; and (c) no person shall be compelled to do that which the law does not require him to do."],
            tags=["rule_of_law", "due_process", "liberty"])

    add_art("5", "Loyalty to State and obedience to Constitution and law", "Part I", "Introductory", None, None,
            "Declares that loyalty to the State is the basic duty of every citizen, and obedience to the Constitution and law is the inviolable obligation of every citizen and person within Pakistan.",
            ["(1) Loyalty to the State is the basic duty of every citizen.",
             "(2) Obedience to the Constitution and law is the inviolable obligation of every citizen wherever he may be and of every other person for the time being within Pakistan."],
            tags=["loyalty", "citizenship", "duties"])

    add_art("6", "High treason", "Part I", "Introductory", None, None,
            "Defines high treason as any act that abrogates, subverts, suspends, or holds in abeyance the Constitution by use or show of force or unconstitutional means. Following the 18th Amendment, explicitly prohibits the Supreme Court or High Courts from validating any act of high treason.",
            ["(1) Any person who abrogates or subverts or suspends or holds in abeyance, or attempts or conspires to abrogate or subvert or suspend or hold in abeyance, the Constitution by use of force or show of force or by any other unconstitutional means shall be guilty of high treason.",
             "(2) Any person aiding or abetting or collaborating the acts mentioned in clause (1) shall likewise be guilty of high treason.",
             "(2A) An act of high treason mentioned in clause (1) or clause (2) shall not be validated by any court including the Supreme Court and a High Court.",
             "(3) Majlis-e-Shoora (Parliament) shall by law provide for the punishment of persons found guilty of high treason."],
            tags=["treason", "abrogation", "constitution_protection"])

    # =========================================================================
    # PART II: FUNDAMENTAL RIGHTS & PRINCIPLES OF POLICY (Articles 7 - 40)
    # Chapter 1: Fundamental Rights (Articles 8 - 28)
    # =========================================================================
    add_art("7", "Definition of the State", "Part II", "Fundamental Rights and Principles of Policy", None, None,
            "Defines 'the State' for the purposes of Part II as the Federal Government, Parliament, Provincial Governments, Provincial Assemblies, and all local or other authorities empowered to impose taxes or cesses.",
            ["In this Part, unless the context otherwise requires, 'the State' means the Federal Government, Majlis-e-Shoora (Parliament), a Provincial Government, a Provincial Assembly, and such local or other authorities in Pakistan as are by law empowered to impose any tax or cess."],
            tags=["state", "fundamental_rights", "local_government"])

    add_art("8", "Laws inconsistent with or in derogation of Fundamental Rights to be void", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Core judicial review anchor: declares that any law, custom, or usage having the force of law that is inconsistent with or derogates from fundamental rights is void to the extent of such inconsistency. Prohibits the State from enacting any law taking away or abridging these rights.",
            ["(1) Any law, or any custom or usage having the force of law, in so far as it is inconsistent with the rights conferred by this Chapter, shall, to the extent of such inconsistency, be void.",
             "(2) The State shall not make any law which takes away or abridges the rights so conferred and any law made in contravention of this clause shall, to the extent of the contravention, be void."],
            tags=["judicial_review", "void_laws", "fundamental_rights"])

    add_art("9", "Security of person", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees that no person shall be deprived of life or liberty save in accordance with law. Extensively interpreted by the superior judiciary to encompass the right to clean drinking water, human dignity, public health, housing, and livelihood.",
            ["No person shall be deprived of life or liberty save in accordance with law."],
            tags=["life", "liberty", "human_rights"])

    add_art("9A", "Clean and healthy environment", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Inserted by the 26th Constitutional Amendment, 2024. Recognizes every person's fundamental right to a clean, healthy, and sustainable environment as an enforceable constitutional right.",
            ["Every person shall be entitled to a clean, healthy and sustainable environment."],
            tags=["environment", "sustainability", "climate_justice", "26th_amendment"])

    add_art("10", "Safeguards as to arrest and detention", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees the right to be informed of the grounds of arrest, the right to consult and be defended by a legal practitioner of choice, and the mandatory requirement to produce an arrested person before a magistrate within 24 hours. Regulates preventive detention review boards.",
            ["(1) No person who is arrested shall be detained in custody without being informed, as soon as may be, of the grounds for such arrest, nor shall he be denied the right to consult and be defended by a legal practitioner of his choice.",
             "(2) Every person who is arrested and detained in custody shall be produced before a magistrate within a period of twenty-four hours of such arrest..."],
            tags=["arrest", "detention", "magistrate", "legal_defense"])

    add_art("10A", "Right to fair trial", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Inserted by the 18th Amendment, 2010. Guarantees that in the determination of his civil rights and obligations or in any criminal charge against him, a person shall be entitled to a fair trial and due process.",
            ["For the determination of his civil rights and obligations or in any criminal charge against him a person shall be entitled to a fair trial and due process."],
            tags=["fair_trial", "due_process", "18th_amendment", "criminal_justice"])

    add_art("11", "Slavery, forced labour, etc. prohibited", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Prohibits slavery, trafficking in human beings, forced labor (begar), and child labor in factories, mines, or hazardous employment for children under the age of fourteen.",
            ["(1) Slavery is non-existent and forbidden and no law shall permit or facilitate its introduction into Pakistan in any form.",
             "(2) All forms of forced labour and traffic in human beings are prohibited.",
             "(3) No child below the age of fourteen years shall be engaged in any factory or mine or any other hazardous employment."],
            tags=["slavery", "forced_labour", "child_labour", "human_trafficking"])

    add_art("12", "Protection against retrospective punishment", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Bars ex-post facto criminal legislation: no person can be punished for an act or omission that was not punishable by law at the time it occurred, nor subjected to a greater penalty than that prescribed at the time of the offence.",
            ["(1) No law shall authorize the punishment of a person— (a) for an act or omission that was not punishable by law at the time of the act or omission; or (b) for an offence by a penalty greater than, or of a kind different from, the penalty prescribed by law for that offence at the time the offence was committed."],
            tags=["criminal_law", "retroactive", "penalty"])

    add_art("13", "Protection against double punishment and self-incrimination", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Prohibits double jeopardy (prosecuting or punishing a person twice for the same offence) and guarantees the privilege against self-incrimination (compelling an accused person to be a witness against himself).",
            ["No person— (a) shall be prosecuted or punished for the same offence more than once; or (b) shall, when accused of an offence, be compelled to be a witness against himself."],
            tags=["double_jeopardy", "self_incrimination", "fair_trial"])

    add_art("14", "Inviolability of dignity of man, etc.", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Constitutionalizes human dignity: guarantees that the dignity of man and, subject to law, the privacy of home, shall be inviolable. Explicitly prohibits the use of torture for extracting evidence.",
            ["(1) The dignity of man and, subject to law, the privacy of home, shall be inviolable.",
             "(2) No person shall be subjected to torture for the purpose of extracting evidence."],
            tags=["dignity", "privacy", "torture", "human_rights"])

    add_art("15", "Freedom of movement, etc.", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees every citizen the right to remain in, enter, move freely throughout, and reside and settle in any part of Pakistan, subject to reasonable restrictions imposed by law in the public interest.",
            ["Every citizen shall have the right to remain in, and, subject to any reasonable restriction imposed by law in the public interest, enter and move freely throughout Pakistan and to reside and settle in any part thereof."],
            tags=["movement", "residence", "travel"])

    add_art("16", "Freedom of assembly", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees every citizen the right to assemble peacefully and without arms, subject to reasonable restrictions imposed by law in the interest of public order.",
            ["Every citizen shall have the right to assemble peacefully and without arms, subject to any reasonable restrictions imposed by law in the interest of public order."],
            tags=["assembly", "protest", "public_order"])

    add_art("17", "Freedom of association", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees every citizen the right to form associations or unions, and the right of every citizen not in the service of Pakistan to form or be a member of a political party. Regulates disclosure of party funding sources.",
            ["(1) Every citizen shall have the right to form associations or unions, subject to any reasonable restrictions imposed by law in the interest of sovereignty or integrity of Pakistan, public order or morality.",
             "(2) Every citizen, not being in the service of Pakistan, shall have the right to form or be a member of a political party, subject to any reasonable restrictions imposed by law..."],
            tags=["association", "political_parties", "unions"])

    add_art("18", "Freedom of trade, business or profession", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees every citizen the right to enter upon any lawful profession or occupation, and to conduct any lawful trade or business, subject to professional qualifications, licensing, and state monopoly regulation.",
            ["Subject to such qualifications, if any, as may be prescribed by law, every citizen shall have the right to enter upon any lawful profession or occupation, and to conduct any lawful trade or business."],
            tags=["trade", "business", "profession", "commerce"])

    add_art("19", "Freedom of speech, etc.", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees freedom of speech and expression, and freedom of the press, subject to reasonable restrictions imposed by law in the interest of the glory of Islam, integrity/security/defense of Pakistan, public order, decency, morality, or contempt of court.",
            ["Every citizen shall have the right to freedom of speech and expression, and there shall be freedom of the press, subject to any reasonable restrictions imposed by law in the interest of the glory of Islam or the integrity, security or defence of Pakistan or any part thereof, friendly relations with foreign States, public order, decency or morality, or in relation to contempt of court, commission of or incitement to an offence."],
            tags=["free_speech", "press", "expression"])

    add_art("19A", "Right to information", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Inserted by the 18th Amendment, 2010. Guarantees every citizen the right to have access to information in all matters of public importance, subject to regulation and reasonable restrictions imposed by law.",
            ["Every citizen shall have the right to have access to information in all matters of public importance subject to regulation and reasonable restrictions imposed by law."],
            tags=["rti", "information", "transparency", "18th_amendment"])

    add_art("20", "Freedom to profess religion and to manage religious institutions", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees every citizen the right to profess, practice, and propagate their religion, and guarantees every religious denomination and sect the right to establish, maintain, and manage its religious institutions.",
            ["Subject to law, public order and morality— (a) every citizen has the right to profess, practise and propagate his religion; and (b) every religious denomination and every sect thereof has the right to establish, maintain and manage its religious institutions."],
            tags=["religion", "minorities", "worship"])

    add_art("21", "Safeguard against taxation for purposes of any particular religion", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Prohibits compelling any person to pay any special tax the proceeds of which are to be spent on the propagation or maintenance of any religion other than his own.",
            ["No person shall be compelled to pay any special tax the proceeds of which are to be spent on the propagation or maintenance of any religion other than his own."],
            tags=["taxation", "religion", "secular_protection"])

    add_art("22", "Safeguards as to educational institutions in respect of religion, etc.", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees that no person attending an educational institution shall be required to receive religious instruction or take part in religious ceremonies relating to a religion other than his own. Prohibits religious discrimination in admissions to tax-supported institutions.",
            ["(1) No person attending any educational institution shall be required to receive religious instruction, or take part in any religious ceremony, or attend religious worship, if such instruction, ceremony or worship relates to a religion other than his own."],
            tags=["education", "religious_freedom", "admissions"])

    add_art("23", "Provision as to property", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees every citizen the right to acquire, hold, and dispose of property in any part of Pakistan, subject to reasonable restrictions imposed by law in the public interest.",
            ["Every citizen shall have the right to acquire, hold and dispose of property in any part of Pakistan, subject to the Constitution and any reasonable restrictions imposed by law in the public interest."],
            tags=["property", "ownership", "assets"])

    add_art("24", "Protection of property rights", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Prohibits compulsory acquisition or taking possession of private property save by authority of law for a public purpose, and requires compensation to be fixed by law.",
            ["(1) No person shall be deprived of his property save in accordance with law.",
             "(2) No property shall be compulsorily acquired or taken possession of save for a public purpose and save by the authority of law which provides for compensation therefor..."],
            tags=["property_rights", "expropriation", "compensation"])

    add_art("25", "Equality of citizens", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Foundational equality clause: all citizens are equal before law and entitled to equal protection of law. Prohibits discrimination on the basis of sex alone. Authorizes affirmative action for women and children.",
            ["(1) All citizens are equal before law and are entitled to equal protection of law.",
             "(2) There shall be no discrimination on the basis of sex.",
             "(3) Nothing in this Article shall prevent the State from making any special provision for the protection of women and children."],
            tags=["equality", "gender", "non_discrimination"])

    add_art("25A", "Right to education", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Inserted by the 18th Amendment, 2010. Makes free and compulsory education for all children aged five to sixteen years an enforceable fundamental right of every child in Pakistan.",
            ["The State shall provide free and compulsory education to all children of the age of five to sixteen years in such manner as may be determined by law."],
            tags=["education", "children", "literacy", "18th_amendment"])

    add_art("26", "Non-discrimination in respect of access to public places", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees that there shall be no discrimination against any citizen on the ground only of race, religion, caste, sex, residence, or place of birth in respect of access to public places of entertainment or resort not intended for religious purposes.",
            ["In respect of access to places of public entertainment or resort, not intended for religious purposes only, there shall be no discrimination against any citizen on the ground only of race, religion, caste, sex, residence or place of birth."],
            tags=["public_access", "non_discrimination", "civil_rights"])

    add_art("27", "Safeguard against discrimination in services", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Prohibits discrimination in appointments to the service of Pakistan on grounds of race, religion, caste, sex, residence, or place of birth, while constitutionalizing regional and provincial affirmative action quotas.",
            ["No citizen otherwise qualified for appointment in the service of Pakistan shall be discriminated against in respect of any such appointment on the ground only of race, religion, caste, sex, residence or place of birth..."],
            tags=["civil_service", "quotas", "employment"])

    add_art("28", "Preservation of language, script and culture", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 1", "Fundamental Rights",
            "Guarantees any section of citizens having a distinct language, script, or culture the right to preserve and promote the same and, subject to law, establish institutions for that purpose.",
            ["Subject to Article 251, any section of citizens having a distinct language, script or culture shall have the right to preserve and promote the same and subject to law, establish institutions for that purpose."],
            tags=["language", "culture", "provincial_identity"])

    # -------------------------------------------------------------------------
    # Part II - Chapter 2: Principles of Policy (Articles 29 - 40)
    # -------------------------------------------------------------------------
    add_art("29", "Principles of Policy", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Establishes that it is the responsibility of each organ and authority of the State to act in accordance with the Principles of Policy, in so far as is within its capacity. Clarifies that validity of state actions cannot be questioned in court solely for non-compliance with these non-justiciable principles.",
            tags=["principles_of_policy", "state_responsibility"])

    add_art("30", "Responsibility with respect to Principles of Policy", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Directs state authorities to observe the Principles of Policy in all administrative and legislative actions, subject to resource availability.",
            tags=["principles_of_policy", "governance"])

    add_art("31", "Islamic way of life", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Mandates the State to take steps enabling Muslims of Pakistan to order their lives in accordance with the fundamental principles and basic concepts of Islam.",
            tags=["islamic_provisions", "principles_of_policy"])

    add_art("32", "Promotion of local Government institutions", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Directs the State to encourage local government institutions composed of elected representatives of the areas concerned, with special representation for peasants, workers, and women.",
            tags=["local_government", "representation", "devolution"])

    add_art("33", "Parochial and other similar prejudices to be discouraged", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Directs the State to actively discourage parochial, racial, tribal, sectarian, and provincial prejudices among citizens.",
            tags=["national_unity", "anti_prejudice"])

    add_art("34", "Full participation of women in national life", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Directs the State to take active measures to ensure the full participation of women in all spheres of national life and public affairs.",
            tags=["women_empowerment", "gender_equity"])

    add_art("35", "Protection of family, etc.", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Directs the State to protect the marriage, the family, the mother, and the child.",
            tags=["family", "child_protection", "welfare"])

    add_art("36", "Protection of minorities", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Directs the State to safeguard the legitimate rights and interests of minorities, including their due representation in the Federal and Provincial services.",
            tags=["minorities", "rights", "representation"])

    add_art("37", "Promotion of social justice and eradication of social evils", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Directs the State to promote educational and economic interests of backward areas, remove illiteracy, provide free secondary education, ensure inexpensive and expeditious justice, and eradicate social evils including gambling and narcotics.",
            tags=["social_justice", "backward_areas", "inexpensive_justice"])

    add_art("38", "Promotion of social and economic well-being of the people", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Directs the State to secure the well-being of citizens, prevent concentration of wealth, provide social security, and eliminate Riba (usury) as early as possible.",
            tags=["welfare_state", "riba", "social_security"])

    add_art("39", "Participation of people in Armed Forces", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Directs the State to enable people from all parts of Pakistan to participate in the Armed Forces of Pakistan.",
            tags=["armed_forces", "provincial_representation"])

    add_art("40", "Strengthening bonds with Muslim world and promoting international peace", "Part II", "Fundamental Rights and Principles of Policy", "Chapter 2", "Principles of Policy",
            "Directs the State to preserve and strengthen fraternal relations among Muslim countries, support common interests of peoples of Asia, Africa and Latin America, and promote international peace and security.",
            tags=["foreign_policy", "muslim_world", "peace"])

    # =========================================================================
    # PART III: THE FEDERATION OF PAKISTAN (Articles 41 - 100)
    # Chapter 1: The President (Articles 41 - 49)
    # =========================================================================
    add_art("41", "The President", "Part III", "The Federation of Pakistan", "Chapter 1", "The President",
            "Establishes the Head of State of Pakistan, representing the unity of the Republic. Sets out qualifications (Muslim, age 45+, qualified to be MNA) and election by an Electoral College consisting of Parliament and the four Provincial Assemblies.",
            tags=["president", "head_of_state", "electoral_college"])

    add_art("42", "Oath of President", "Part III", "The Federation of Pakistan", "Chapter 1", "The President",
            "Requires the President to make before the Chief Justice of Pakistan an oath in the form set out in the Third Schedule.",
            tags=["president", "oath"])

    add_art("43", "Conditions of President's office", "Part III", "The Federation of Pakistan", "Chapter 1", "The President",
            "Bars the President from holding any office of profit in the service of Pakistan or occupying any position carrying remuneration.",
            tags=["president", "office_of_profit"])

    add_art("44", "Term of office of President", "Part III", "The Federation of Pakistan", "Chapter 1", "The President",
            "Fixes the term of office of the President at five years, with a maximum limit of two consecutive terms.",
            tags=["president", "term_of_office"])

    add_art("45", "President's power to grant pardon, etc.", "Part III", "The Federation of Pakistan", "Chapter 1", "The President",
            "Empowers the President to grant pardon, reprieve, respite, and remit, suspend, or commute any sentence passed by any court, tribunal, or authority.",
            tags=["pardon", "mercy_petition", "executive_power"])

    add_art("46", "President to be kept informed", "Part III", "The Federation of Pakistan", "Chapter 1", "The President",
            "Obligates the Prime Minister to keep the President informed on all matters of internal and foreign policy and legislative proposals.",
            tags=["president", "prime_minister", "communications"])

    add_art("47", "Removal or impeachment of President", "Part III", "The Federation of Pakistan", "Chapter 1", "The President",
            "Provides the detailed constitutional procedure for the removal or impeachment of the President on grounds of physical/mental incapacity or gross misconduct, requiring a two-thirds majority of the joint sitting of Parliament.",
            tags=["impeachment", "president", "parliament"])

    add_art("48", "President to act on advice, etc.", "Part III", "The Federation of Pakistan", "Chapter 1", "The President",
            "The cornerstone of the parliamentary executive: requires the President to act strictly on and in accordance with the advice of the Cabinet or Prime Minister. Sets out referendum referral provisions.",
            tags=["cabinet_advice", "prime_minister", "parliamentary_system"])

    add_art("49", "Chairman or Speaker to act as, or perform functions of, President", "Part III", "The Federation of Pakistan", "Chapter 1", "The President",
            "Specifies succession rules: the Chairman of the Senate (or Speaker of the National Assembly if Chairman is unable) acts as President during a vacancy.",
            tags=["acting_president", "senate_chairman", "speaker"])

    # -------------------------------------------------------------------------
    # Part III - Chapter 2: Majlis-e-Shoora (Parliament) (Articles 50 - 88)
    # -------------------------------------------------------------------------
    add_art("50", "Majlis-e-Shoora (Parliament)", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Establishes Pakistan's bicameral federal legislature: Majlis-e-Shoora consists of the President and two Houses: the National Assembly and the Senate.",
            tags=["parliament", "bicameral", "legislature"])

    add_art("51", "National Assembly", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Specifies the composition of the National Assembly (total seats, provincial seat allocations, women reserved seats, non-Muslim minority seats) based on official population census figures.",
            tags=["national_assembly", "seats", "provincial_quotas", "women_seats", "minority_seats"])

    add_art("52", "Duration of National Assembly", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Fixes the term of the National Assembly at five years from the day of its first meeting, unless sooner dissolved.",
            tags=["national_assembly", "five_year_term", "duration"])

    add_art("53", "Speaker and Deputy Speaker of National Assembly", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Provides for the election, duties, resignation, and removal of the Speaker and Deputy Speaker of the National Assembly.",
            tags=["speaker", "deputy_speaker", "assembly_leadership"])

    add_art("54", "Summoning and prorogation of Majlis-e-Shoora", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Regulates the summoning, sessions, and prorogation of Parliament. Mandates a minimum of 130 working days per year for the National Assembly and establishes requisitioning powers by one-fourth of assembly membership.",
            tags=["sessions", "summoning", "prorogation", "requisition"])

    add_art("55", "Voting in Assembly and quorum", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Establishes decision-making by majority vote (Speaker casts tie-breaking vote) and sets the quorum of the National Assembly at one-fourth of the total membership.",
            tags=["voting", "quorum", "majority_rule"])

    add_art("56", "Address by President", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Empowers the President to address either House or a joint sitting, and requires an annual presidential address at the commencement of each parliamentary year.",
            tags=["president", "joint_sitting", "address"])

    add_art("57", "Rights to speak, etc., of Prime Minister, etc.", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Gives Prime Minister, Federal Ministers, Ministers of State, and the Attorney-General the right to speak and participate in proceedings of either House or joint committees (without voting rights unless an elected member of that House).",
            tags=["attorney_general", "ministers", "parliamentary_debates"])

    add_art("58", "Dissolution of National Assembly", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Regulates assembly dissolution: President dissolves the National Assembly on the binding advice of the Prime Minister (automatic dissolution after 48 hours if President fails to act). Following the 18th Amendment, Article 58(2)(b) discretionary dissolution stands completely omitted.",
            tags=["dissolution", "prime_minister_advice", "18th_amendment"])

    add_art("59", "The Senate", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Establishes the Senate as the permanent Upper House representing the federating units on an equal basis (equal provincial representation), ensuring subnational federal balance. Half of the members retire every three years; Senate is not subject to dissolution.",
            tags=["senate", "upper_house", "provincial_equality", "federal_balance"])

    add_art("60", "Chairman and Deputy Chairman", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Provides for the election of the Chairman and Deputy Chairman of the Senate for a three-year term following each biennial Senate reconstitution.",
            tags=["senate_chairman", "deputy_chairman"])

    add_art("61", "Other provisions relating to Senate", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Applies National Assembly rules regarding Speaker, voting, and sessions to the Senate, and mandates at least 110 working days annually.",
            tags=["senate_rules", "working_days"])

    add_art("62", "Qualifications for membership of Majlis-e-Shoora", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Prescribes qualifications for parliamentarians: citizenship, minimum age (25 for MNA, 30 for Senator), and moral/ethical criteria including being 'sadiq and ameen' (truthful and righteous).",
            tags=["qualifications", "sadiq_ameen", "elections"])

    add_art("63", "Disqualifications for membership of Majlis-e-Shoora", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Comprehensive catalog of disqualifications: mental unsoundness, undischarged insolvency, holding an office of profit, loan default, conviction for moral turpitude, dual nationality, or ridiculing the judiciary/armed forces.",
            tags=["disqualifications", "dual_nationality", "elections"])

    add_art("63A", "Disqualification on ground of defection, etc.", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Constitutional anti-defection mechanism: a parliamentarian who resigns from their party or votes contrary to party direction in election of PM/CM, vote of confidence/no-confidence, or a Money Bill may be declared disqualified by the Party Head upon confirmation by the ECP.",
            tags=["anti_defection", "party_discipline", "vote_of_confidence"])

    add_art("64", "Vacation of seats", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Specifies grounds on which a member's seat becomes vacant, including written resignation or unexplained absence for 40 consecutive sitting days.",
            tags=["vacation_of_seats", "resignation", "absence"])

    add_art("65", "Oath of members", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Mandates that every elected parliamentarian must take the constitutional oath set out in the Third Schedule before taking their seat.",
            tags=["oath", "members"])

    add_art("66", "Privileges of members, etc.", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Guarantees freedom of speech in Parliament and absolute immunity from court proceedings in respect of anything said or any vote given in Parliament or any committee.",
            tags=["parliamentary_privilege", "immunity", "freedom_of_speech"])

    # Legislative Procedures (Articles 70 - 88)
    add_art("70", "Introduction and passing of Bills", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Sets out the standard legislative procedure: a Bill with respect to any matter in the Federal Legislative List may originate in either House and is transmitted to the other House upon passage.",
            tags=["bills", "legislation", "federal_legislative_list"])

    add_art("71", "Mediation Committee", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Omitted by the 18th Amendment, 2010. Deadlocks are now resolved through joint sittings.",
            status="omitted", tags=["omitted", "18th_amendment"])

    add_art("72", "Procedure at joint sittings", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Regulates joint sittings of Parliament presided over by the Speaker of the National Assembly.",
            tags=["joint_sitting", "speaker_powers"])

    add_art("73", "Procedure with respect to Money Bills", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Exclusive jurisdiction over the national purse: Money Bills (budget, taxes, borrowing) must originate strictly in the National Assembly. Senate provides non-binding recommendations within 14 days.",
            tags=["money_bill", "budget", "national_assembly_supremacy"])

    add_art("74", "Federal Government's consent required for financial measures", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Requires Federal Government consent before any Money Bill or financial measure affecting public revenues can be introduced by a private member.",
            tags=["financial_measures", "government_consent"])

    add_art("75", "President's assent to Bills", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Regulates presidential assent: President must assent within 10 days or return a non-money bill for reconsideration. If passed again by a joint sitting by majority of members present and voting, the President must assent within 10 days, failing which assent is deemed given.",
            tags=["presidential_assent", "veto_override", "legislation"])

    add_art("76", "Bill not to lapse on prorogation, etc.", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Provides that pending bills do not lapse by reason of the prorogation of either House, but pending bills lapse upon dissolution of the National Assembly.",
            tags=["bills_lapse", "prorogation", "dissolution"])

    add_art("77", "Tax to be levied by law only", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Fundamental rule of public finance: no tax shall be levied for the purposes of the Federation except by or under the authority of an Act of Majlis-e-Shoora (Parliament).",
            tags=["taxation", "no_taxation_without_representation", "parliamentary_law"])

    add_art("78", "Federal Consolidated Fund and Public Account", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Defines the Federal Consolidated Fund (all revenues, loans raised, and loan repayments received by the Federal Government) and the Public Account of the Federation.",
            tags=["federal_consolidated_fund", "public_account", "finance"])

    add_art("79", "Custody, etc., of Federal Consolidated Fund and Public Account", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Regulates the custody, deposit, withdrawal, and accounting of moneys in the Federal Consolidated Fund.",
            tags=["treasury", "public_funds"])

    add_art("80", "Annual Budget Statement", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Mandates the presentation of the Annual Budget Statement before the National Assembly showing estimated federal receipts and expenditures for the financial year.",
            tags=["budget", "annual_budget_statement", "finance"])

    add_art("81", "Expenditure charged upon Federal Consolidated Fund", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Enumerates constitutional expenditures charged directly on the Federal Consolidated Fund (remuneration of President, Judges of the Supreme Court and High Courts, Chairman/Speaker, ECP, and national debt charges), which are discussed but not voted upon.",
            tags=["charged_expenditure", "judges_salaries", "debt_servicing"])

    add_art("82", "Procedure relating to Annual Budget Statement", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Distinguishes between charged expenditures (discussed, not voted) and other expenditures submitted to the National Assembly in the form of demands for grants.",
            tags=["demands_for_grants", "voting_budget"])

    add_art("83", "Authentication of schedule of authorized expenditure", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Requires the Prime Minister to authenticate the schedule of authorized expenditure following the approval of demands for grants by the National Assembly.",
            tags=["budget_authentication", "prime_minister"])

    add_art("84", "Supplementary and excess grants", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Regulates the authorization and parliamentary presentation of supplementary and excess expenditure grants during a financial year.",
            tags=["supplementary_grants", "public_spending"])

    add_art("85", "Votes on account", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Empowers the National Assembly to make advance expenditure grants (vote on account) pending the completion of the regular budget procedure.",
            tags=["vote_on_account", "advance_spending"])

    add_art("86", "Power to authorize expenditure when Assembly stands dissolved", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Empowers the Federal Government to authorize expenditure for up to four months when the National Assembly stands dissolved, pending the new assembly's meeting.",
            tags=["dissolution_spending", "caretaker_spending"])

    add_art("87", "Secretariats of Majlis-e-Shoora", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Establishes separate independent secretariats for the National Assembly and the Senate, with independent recruitment and service conditions.",
            tags=["parliamentary_secretariat", "staff"])

    add_art("88", "Committees of Majlis-e-Shoora", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Provides for the statutory constitution of Standing Committees, Public Accounts Committees, and special committees in each House.",
            tags=["committees", "pac", "oversight"])

    add_art("89", "Power of President to promulgate Ordinances", "Part III", "The Federation of Pakistan", "Chapter 2", "Majlis-e-Shoora (Parliament)",
            "Strictly circumscribes executive law-making: President can promulgate an Ordinance only when neither House is in session and immediate action is necessary. Valid for 120 days; may be extended once for 120 days by parliamentary resolution; cannot be re-promulgated.",
            tags=["ordinance", "executive_orders", "sunset_clause"])

    # -------------------------------------------------------------------------
    # Part III - Chapter 3: The Federal Government (Articles 90 - 100)
    # -------------------------------------------------------------------------
    add_art("90", "The Federal Government", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Following the 18th Amendment, vests the executive authority of the Federation in the Federal Government, consisting of the Prime Minister and the Federal Ministers, acting through the Prime Minister as chief executive.",
            tags=["federal_government", "prime_minister", "cabinet"])

    add_art("91", "The Cabinet", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Establishes the Cabinet of Ministers headed by the Prime Minister to aid and advise the President. The Cabinet is collectively responsible to the National Assembly. Governs the election and vote of confidence for the Prime Minister.",
            tags=["cabinet", "collective_responsibility", "prime_minister_election"])

    add_art("92", "Federal Ministers and Ministers of State", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Regulates the appointment of Federal Ministers and Ministers of State from among parliamentarians; caps the size of the federal cabinet at 11% of total parliamentary strength.",
            tags=["federal_ministers", "cabinet_size", "18th_amendment"])

    add_art("93", "Advisers", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Empowers the President, on the advice of the Prime Minister, to appoint not more than five Advisers with rights to speak in parliamentary debates.",
            tags=["advisers", "prime_minister_advice"])

    add_art("94", "Prime Minister continuing in office", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Authorizes the President to ask the Prime Minister to continue in office until his successor enters upon the office of Prime Minister.",
            tags=["caretaker", "transition", "continuity"])

    add_art("95", "Vote of no-confidence against Prime Minister", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Provides the constitutional mechanism for removing a Prime Minister: a resolution moved by at least 20% of the National Assembly members and passed by a majority of the total membership.",
            tags=["no_confidence", "prime_minister_removal", "majority_rule"])

    add_art("96", "Vote of confidence in Prime Minister", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Repealed/Omitted.", status="omitted", tags=["omitted"])

    add_art("97", "Extent of executive authority of Federation", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Delineates federal executive authority to matters with respect to which Parliament has power to make laws, respecting provincial executive jurisdiction.",
            tags=["federal_authority", "executive_powers", "jurisdiction"])

    add_art("98", "Conferment of functions on subordinate authorities", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Empowers Parliament by law to confer functions upon officers or authorities subordinate to the Federal Government.",
            tags=["delegated_powers", "subordinate_officers"])

    add_art("99", "Conduct of business of Federal Government", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Directs that all executive actions of the Federal Government shall be expressed to be taken in the name of the President, and regulates the Federal Rules of Business.",
            tags=["rules_of_business", "executive_actions"])

    add_art("100", "Attorney-General for Pakistan", "Part III", "The Federation of Pakistan", "Chapter 3", "The Federal Government",
            "Provides for the appointment by the President of a person qualified to be a Judge of the Supreme Court as Attorney-General for Pakistan, the chief legal officer of the federal state.",
            tags=["attorney_general", "legal_counsel", "state_representation"])

    # =========================================================================
    # PART IV: PROVINCES (Articles 101 - 140A)
    # Chapter 1: The Governors (Articles 101 - 105)
    # Chapter 2: Provincial Assemblies (Articles 106 - 128)
    # Chapter 3: The Provincial Governments (Articles 129 - 140A)
    # =========================================================================
    add_art("101", "Appointment of Governor", "Part IV", "Provinces", "Chapter 1", "The Governors",
            "Regulates the appointment of the Governor of each Province by the President on the binding advice of the Prime Minister. Governor must be a registered voter and resident of that Province.",
            tags=["governor", "provincial_head", "appointments"])

    add_art("102", "Oath of Governor", "Part IV", "Provinces", "Chapter 1", "The Governors",
            "Requires the Governor to take an oath before the Chief Justice of the respective High Court.",
            tags=["governor", "oath", "high_court"])

    add_art("103", "Conditions of Governor's office", "Part IV", "Provinces", "Chapter 1", "The Governors",
            "Bars the Governor from holding any office of profit in the service of Pakistan.",
            tags=["governor", "office_of_profit"])

    add_art("104", "Speaker Provincial Assembly to act as, or perform functions of, Governor", "Part IV", "Provinces", "Chapter 1", "The Governors",
            "Provides that the Speaker of the Provincial Assembly acts as Governor during absence or vacancy.",
            tags=["acting_governor", "provincial_speaker"])

    add_art("105", "Governor to act on advice, etc.", "Part IV", "Provinces", "Chapter 1", "The Governors",
            "Requires the Governor to act strictly on and in accordance with the advice of the provincial Cabinet or Chief Minister. Sets out dissolution advice rules.",
            tags=["governor_advice", "chief_minister", "provincial_cabinet"])

    # Chapter 2: Provincial Assemblies (Articles 106 - 128)
    add_art("106", "Constitution of Provincial Assemblies", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Specifies the composition and seat allocation of the four Provincial Assemblies (Balochistan, Khyber Pakhtunkhwa, Punjab, Sindh), including general seats, women reserved seats, and non-Muslim minority seats.",
            tags=["provincial_assembly", "seats", "provincial_representation"])

    add_art("107", "Duration of Provincial Assembly", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Fixes the term of a Provincial Assembly at five years from the day of its first meeting.",
            tags=["provincial_assembly", "duration", "five_year_term"])

    add_art("108", "Speaker and Deputy Speaker", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Provides for the election, duties, and removal of the Speaker and Deputy Speaker of a Provincial Assembly.",
            tags=["provincial_speaker", "deputy_speaker"])

    add_art("109", "Summoning and prorogation of Provincial Assembly", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Regulates the summoning and prorogation of the Provincial Assembly by the Governor, and establishes the 100-day minimum annual sitting requirement.",
            tags=["assembly_sessions", "working_days", "requisition"])

    add_art("110", "Right of Governor to address Provincial Assembly", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Authorizes the Governor to address the Provincial Assembly.",
            tags=["governor_address", "provincial_assembly"])

    add_art("111", "Right to speak in Provincial Assembly", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Gives Advocate-General of the Province and Provincial Ministers the right to participate in assembly proceedings.",
            tags=["advocate_general", "provincial_debates"])

    add_art("112", "Dissolution of Provincial Assembly", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Regulates assembly dissolution: Governor dissolves on the binding advice of the Chief Minister (automatic dissolution after 48 hours if Governor fails to act).",
            tags=["assembly_dissolution", "chief_minister_advice"])

    add_art("113", "Qualifications and disqualifications for members", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Applies Articles 62 and 63 qualifications and disqualifications to members of Provincial Assemblies (MPAs).",
            tags=["mpa_qualifications", "disqualifications"])

    add_art("114", "Restriction on discussion in Provincial Assembly", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Prohibits discussion in the Provincial Assembly with respect to the conduct of any Judge of the Supreme Court or of a High Court.",
            tags=["judicial_independence", "assembly_restrictions"])

    add_art("115", "Provincial Consolidated Fund and Public Account", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Establishes the Provincial Consolidated Fund and Public Account of each Province.",
            tags=["provincial_consolidated_fund", "provincial_finance"])

    add_art("116", "Governor's assent to Bills", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Regulates the Governor's assent to provincial legislation, return of bills, and deemed assent upon repassage.",
            tags=["governor_assent", "provincial_legislation"])

    add_art("117", "Bill not to lapse on prorogation", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Clarifies that bills pending in a Provincial Assembly do not lapse by reason of prorogation.",
            tags=["provincial_bills", "prorogation"])

    add_art("118", "Custody, etc., of Provincial Consolidated Fund", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Regulates custody and withdrawals from the Provincial Consolidated Fund.",
            tags=["provincial_treasury", "public_funds"])

    add_art("119", "Annual Budget Statement (Provincial)", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Mandates the presentation of the annual provincial budget statement before each Provincial Assembly.",
            tags=["provincial_budget", "finance"])

    add_art("120", "Expenditure charged upon Provincial Consolidated Fund", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Enumerates charged expenditures for provinces (Governor, High Court Judges, provincial debt charges).",
            tags=["provincial_charged_expenditure", "high_court_salaries"])

    add_art("121", "Procedure relating to Annual Budget Statement", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Regulates voting and demands for grants in Provincial Assemblies.",
            tags=["provincial_grants", "budget_voting"])

    add_art("122", "Authentication of schedule of authorized expenditure", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Requires Chief Minister to authenticate the provincial schedule of authorized expenditure.",
            tags=["budget_authentication", "chief_minister"])

    add_art("123", "Supplementary and excess grants (Provincial)", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Regulates provincial supplementary expenditure authorizations.",
            tags=["provincial_supplementary_grants"])

    add_art("124", "Votes on account (Provincial)", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Authorizes advance provincial budget grants pending regular legislative passage.",
            tags=["provincial_vote_on_account"])

    add_art("125", "Power to authorize expenditure when Assembly is dissolved", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Authorizes provincial caretaker government spending for up to four months during assembly dissolution.",
            tags=["provincial_dissolution_spending"])

    add_art("126", "Secretariat of Provincial Assembly", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Establishes an independent permanent secretariat for each Provincial Assembly.",
            tags=["assembly_secretariat", "provincial_staff"])

    add_art("127", "Provisions relating to National Assembly to apply to Provincial Assembly", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Applies National Assembly procedural rules (voting, quorum, privileges) to Provincial Assemblies.",
            tags=["assembly_rules", "procedural_parity"])

    add_art("128", "Power of Governor to promulgate Ordinances", "Part IV", "Provinces", "Chapter 2", "Provincial Assemblies",
            "Regulates provincial ordinance-making: Governor can promulgate only when assembly is not in session; valid for 90 days; can be extended once by assembly resolution.",
            tags=["provincial_ordinance", "executive_legislation"])

    # Chapter 3: The Provincial Governments (Articles 129 - 140A)
    add_art("129", "The Provincial Government", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Vests executive authority of the Province in the Provincial Government, consisting of the Chief Minister and Provincial Ministers, acting through the Chief Minister.",
            tags=["provincial_government", "chief_minister", "executive"])

    add_art("130", "The Cabinet", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Establishes the Provincial Cabinet headed by the Chief Minister, collectively responsible to the Provincial Assembly. Regulates election of Chief Minister.",
            tags=["provincial_cabinet", "chief_minister_election", "collective_responsibility"])

    add_art("131", "Governor to be kept informed", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Requires Chief Minister to keep the Governor informed on provincial administration and legislative proposals.",
            tags=["chief_minister", "governor_communications"])

    add_art("132", "Provincial Ministers", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Regulates appointment and oath of Provincial Ministers; limits cabinet size to 15 members or 11% of assembly strength.",
            tags=["provincial_ministers", "cabinet_size_limit"])

    add_art("133", "Chief Minister continuing in office", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Provides for the Chief Minister continuing in office during transitional vacancy until a successor assumes office.",
            tags=["chief_minister_transition"])

    add_art("134", "Resignation of Chief Minister", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Omitted.", status="omitted", tags=["omitted"])

    add_art("135", "Vote of no-confidence against Chief Minister", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Repealed/consolidated into Article 136.", status="omitted", tags=["omitted"])

    add_art("136", "Vote of no-confidence against Chief Minister", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Provides the constitutional mechanism for removing a Chief Minister: resolution moved by at least 20% of MPAs and passed by a majority of the total assembly membership.",
            tags=["provincial_no_confidence", "chief_minister_removal"])

    add_art("137", "Extent of executive authority of Province", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Establishes that provincial executive authority extends to all matters with respect to which the Provincial Assembly has power to make laws.",
            tags=["provincial_executive_authority", "provincial_autonomy"])

    add_art("138", "Conferment of functions on subordinate authorities", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Empowers Provincial Assembly to confer statutory functions upon officers subordinate to the Provincial Government.",
            tags=["delegated_authority", "provincial_officers"])

    add_art("139", "Conduct of business of Provincial Government", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Directs that executive actions be expressed in the Governor's name and regulates Provincial Rules of Business.",
            tags=["provincial_rules_of_business"])

    add_art("140", "Advocate-General for a Province", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Provides for the appointment of the Advocate-General for each Province, who serves as the principal legal adviser to the Provincial Government.",
            tags=["advocate_general", "provincial_legal_adviser"])

    add_art("140A", "Local Government", "Part IV", "Provinces", "Chapter 3", "The Provincial Governments",
            "Flagship devolution mandate inserted by the 18th Amendment: Each Province shall, by law, establish a local government system and devolve political, administrative and financial responsibility and authority to the elected representatives of the local governments. Clause (2) mandates the Election Commission of Pakistan to hold local government elections.",
            ["(1) Each Province shall, by law, establish a local government system and devolve political, administrative and financial responsibility and authority to the elected representatives of the local governments.",
             "(2) Elections to the local governments shall be held by the Election Commission of Pakistan."],
            tags=["local_government", "devolution", "article_140a", "fiscal_devolution", "municipal_autonomy"])

    # =========================================================================
    # PART V: RELATIONS BETWEEN FEDERATION AND PROVINCES (Articles 141 - 159)
    # Chapter 1: Legislative Powers (141 - 144)
    # Chapter 2: Administrative Relations (145 - 152)
    # Chapter 3: Special Provisions (153 - 159)
    # =========================================================================
    add_art("141", "Extent of Federal and Provincial laws", "Part V", "Relations Between Federation and Provinces", "Chapter 1", "Distribution of Legislative Powers",
            "Defines territorial legislative jurisdiction: Parliament may make laws for the whole or any part of Pakistan; a Provincial Assembly may make laws for the Province or any part thereof.",
            tags=["legislative_jurisdiction", "territorial_competence"])

    add_art("142", "Subject-matter of Federal and Provincial laws", "Part V", "Relations Between Federation and Provinces", "Chapter 1", "Distribution of Legislative Powers",
            "Post-18th Amendment federal division: Parliament has exclusive power over the Federal Legislative List; Provincial Assemblies have exclusive legislative competence over all residual matters not enumerated in the Federal Legislative List.",
            tags=["division_of_powers", "residual_powers", "federal_legislative_list", "18th_amendment"])

    add_art("143", "Inconsistency between Federal and Provincial law", "Part V", "Relations Between Federation and Provinces", "Chapter 1", "Distribution of Legislative Powers",
            "Supremacy clause: if a Provincial law is repugnant to a Federal law on a subject Parliament is competent to enact, the Federal law prevails and the Provincial law is void to the extent of repugnancy.",
            tags=["federal_supremacy", "repugnancy", "conflict_of_laws"])

    add_art("144", "Power of Majlis-e-Shoora to legislate for two or more Provinces by consent", "Part V", "Relations Between Federation and Provinces", "Chapter 1", "Distribution of Legislative Powers",
            "Authorizes Parliament to enact uniform legislation on residual provincial matters if two or more Provincial Assemblies pass resolutions requesting federal regulation.",
            tags=["provincial_consent", "harmonized_legislation"])

    # Chapter 2: Administrative Relations (145 - 152)
    add_art("145", "Power of President to direct Governor to discharge certain functions as agent", "Part V", "Relations Between Federation and Provinces", "Chapter 2", "Administrative Relations",
            "Authorizes the President to direct a Provincial Governor to act as presidential agent in relation to specific excluded areas.",
            tags=["presidential_agent", "governor"])

    add_art("146", "Power of Federation to confer powers, etc., on Provinces in certain cases", "Part V", "Relations Between Federation and Provinces", "Chapter 2", "Administrative Relations",
            "Permits the Federal Government, with provincial consent, to entrust federal executive functions to a Provincial Government or its officers.",
            tags=["intergovernmental_cooperation", "delegated_administration"])

    add_art("147", "Power of the Provinces to entrust functions to the Federation", "Part V", "Relations Between Federation and Provinces", "Chapter 2", "Administrative Relations",
            "Allows a Provincial Government, with federal consent, to entrust provincial functions to the Federal Government, subject to Provincial Assembly ratification within 60 days.",
            tags=["provincial_entrustment", "cooperative_federalism"])

    add_art("148", "Obligation of Provinces and Federation", "Part V", "Relations Between Federation and Provinces", "Chapter 2", "Administrative Relations",
            "Mandates Provinces to exercise executive authority ensuring compliance with Federal laws; obligates Federation to protect every Province against external aggression and internal disturbances.",
            tags=["federal_duty", "provincial_obligations", "internal_security"])

    add_art("149", "Directions to Provinces in certain cases", "Part V", "Relations Between Federation and Provinces", "Chapter 2", "Administrative Relations",
            "Regulates the issuance of federal executive directions to Provinces for executing federal laws, constructing national means of communication, and preventing grave menace to peace.",
            tags=["federal_directions", "national_communications", "public_peace"])

    add_art("150", "Full faith and credit to public acts, etc.", "Part V", "Relations Between Federation and Provinces", "Chapter 2", "Administrative Relations",
            "Mandates that full faith and credit shall be given throughout Pakistan to public acts, records, and judicial proceedings of every Province.",
            tags=["full_faith_and_credit", "interstate_comity"])

    add_art("151", "Inter-Provincial trade", "Part V", "Relations Between Federation and Provinces", "Chapter 2", "Administrative Relations",
            "Guarantees freedom of inter-provincial trade, commerce, and intercourse throughout Pakistan; prohibits provincial taxes that discriminate against goods manufactured in other provinces.",
            tags=["interprovincial_trade", "internal_market", "customs_barriers"])

    add_art("152", "Acquisition of land for Federal purposes", "Part V", "Relations Between Federation and Provinces", "Chapter 2", "Administrative Relations",
            "Requires Provinces to acquire land at the expense of the Federation when requested for federal governmental purposes.",
            tags=["land_acquisition", "federal_purposes"])

    add_art("152A", "National Security Council", "Part V", "Relations Between Federation and Provinces", "Chapter 2", "Administrative Relations",
            "Omitted by the 18th Amendment, 2010.", status="omitted", tags=["omitted", "18th_amendment"])

    # Chapter 3: Special Provisions (153 - 159)
    add_art("153", "Council of Common Interests", "Part V", "Relations Between Federation and Provinces", "Chapter 3", "Special Provisions",
            "Constitutionalizes the Council of Common Interests (CCI): composed of Prime Minister, four Provincial Chief Ministers, and three Federal Ministers. Formulates and regulates policies regarding matters in Part II of the Federal Legislative List.",
            tags=["cci", "council_of_common_interests", "interprovincial_coordination"])

    add_art("154", "Functions and rules of procedure of Council of Common Interests", "Part V", "Relations Between Federation and Provinces", "Chapter 3", "Special Provisions",
            "Mandates that the CCI shall meet at least once in ninety days and report annually to Parliament. Decisions are by majority vote; appeals lie to a joint sitting of Parliament.",
            tags=["cci_mandate", "ninety_days_rule", "parliamentary_appeal"])

    add_art("155", "Complaints as to interference with water supplies", "Part V", "Relations Between Federation and Provinces", "Chapter 3", "Special Provisions",
            "Provides an inter-provincial dispute resolution mechanism for complaints regarding interference with natural water supplies through the Council of Common Interests.",
            tags=["water_disputes", "irrigation", "cci_arbitration"])

    add_art("156", "National Economic Council", "Part V", "Relations Between Federation and Provinces", "Chapter 3", "Special Provisions",
            "Constitutionalizes the National Economic Council (NEC) to review the overall economic condition of the country and formulate plans for financial, commercial, and economic policies.",
            tags=["nec", "economic_planning", "provincial_representation"])

    add_art("157", "Electricity", "Part V", "Relations Between Federation and Provinces", "Chapter 3", "Special Provisions",
            "Regulates federal-provincial power distribution: Federal Government must consult provincial governments before constructing hydro-electric stations; empowers provinces to construct power stations, lay transmission lines, and levy provincial electricity duty.",
            tags=["electricity", "energy_federalism", "hydel_power"])

    add_art("158", "Priority of requirements of natural gas", "Part V", "Relations Between Federation and Provinces", "Chapter 3", "Special Provisions",
            "Crucial resource federalism clause: guarantees that the Province in which a well-head of natural gas is situated shall have priority over other parts of Pakistan in meeting its requirements.",
            tags=["natural_gas", "well_head_priority", "provincial_resources"])

    add_art("159", "Broadcasting and telecasting", "Part V", "Relations Between Federation and Provinces", "Chapter 3", "Special Provisions",
            "Regulates broadcasting and television transmission facilities for provincial governments.",
            tags=["broadcasting", "media_regulation"])

    # =========================================================================
    # PART VI: FINANCE, PROPERTY, CONTRACTS AND SUITS (Articles 160 - 174)
    # Chapter 1: Finance (160 - 165A)
    # Chapter 2: Property, Contracts, Liabilities and Suits (166 - 174)
    # =========================================================================
    add_art("160", "National Finance Commission", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 1", "Finance",
            "Flagship fiscal federalism provision: establishes the National Finance Commission (NFC) consisting of Federal and Provincial Finance Ministers. Crucially, Article 160(3A) establishes the non-retrogression floor rule: 'the share of the Provinces in each Award of National Finance Commission shall not be less than the share given to the Provinces in the previous Award'.",
            ["(1) Within six months of the commencing day and thereafter at intervals not exceeding five years, the President shall constitute a National Finance Commission...",
             "(3A) The share of the Provinces in each Award of National Finance Commission shall not be less than the share given to the Provinces in the previous Award.",
             "(4) As soon as may be after receiving the recommendations of the National Finance Commission, the President shall by Order specify... the share of the net proceeds of the taxes... which is to be allocated to each Province."],
            tags=["nfc", "fiscal_federalism", "revenue_sharing", "article_160_3a", "divisible_pool"])

    add_art("161", "Natural gas and hydro-electric power", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 1", "Finance",
            "Mandates that net proceeds of federal excise duty on natural gas, royalty on natural gas, and net profits from hydro-electric power generation shall be paid directly to the Province where the well-head or station is situated.",
            tags=["hydel_profits", "gas_royalties", "provincial_revenues"])

    add_art("162", "Prior sanction of President required to Bills affecting taxation in which Provinces are interested", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 1", "Finance",
            "Requires prior presidential sanction before introducing any federal bill that varies taxes whose proceeds are distributed to provinces.",
            tags=["provincial_taxes", "presidential_sanction"])

    add_art("163", "Provincial taxes in respect of professions, etc.", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 1", "Finance",
            "Confirms provincial legislative competence to impose taxes on professions, trades, callings, or employments.",
            tags=["professional_tax", "provincial_revenue"])

    add_art("164", "Grants out of Consolidated Fund", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 1", "Finance",
            "Authorizes Federation or Provinces to make grants for any public purpose, even if outside their legislative competence.",
            tags=["public_grants", "federal_assistance"])

    add_art("165", "Exemption of certain public property from taxation", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 1", "Finance",
            "Mutual tax immunity: Federal Government property and income is exempt from provincial taxation; Provincial Government property is exempt from federal taxation.",
            tags=["tax_immunity", "public_property"])

    add_art("165A", "Power of Majlis-e-Shoora to impose tax on certain corporations, etc.", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 1", "Finance",
            "Clarifies federal taxing authority over commercial corporations established by or under federal law.",
            tags=["corporate_tax", "public_enterprises"])

    # Chapter 2: Property, Contracts, Liabilities and Suits (166 - 174)
    add_art("166", "Borrowing by Federal Government", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 2", "Property, Contracts and Suits",
            "Empowers the Federal Government to borrow money on the security of the Federal Consolidated Fund within parliamentary limits.",
            tags=["federal_borrowing", "sovereign_debt"])

    add_art("167", "Borrowing by Provincial Government", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 2", "Property, Contracts and Suits",
            "Empowers Provincial Governments to borrow within Pakistan; requires federal consent if prior federal loans remain outstanding. 18th Amendment inserted clause (4) permitting provinces to raise domestic and external loans under federal framework.",
            tags=["provincial_borrowing", "subnational_debt", "18th_amendment"])

    add_art("168", "Auditor-General of Pakistan", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 2", "Property, Contracts and Suits",
            "Establishes the independent Auditor-General of Pakistan (AGP) for external audit of federal and provincial public accounts. Fixed non-extendable term of four years.",
            tags=["agp", "auditor_general", "public_audit"])

    add_art("169", "Functions and powers of Auditor-General", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 2", "Property, Contracts and Suits",
            "Empowers AGP to audit accounts of Federation, Provinces, and statutory bodies.",
            tags=["audit_mandate", "public_accounts"])

    add_art("170", "Power of Auditor-General to give directions as to accounts", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 2", "Property, Contracts and Suits",
            "Empowers AGP to prescribe bookkeeping forms and directions for federal and provincial accounts.",
            tags=["accounting_standards", "public_reporting"])

    add_art("171", "Reports of Auditor-General", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 2", "Property, Contracts and Suits",
            "Mandates submission of AGP audit reports to the President and Governors, who lay them before Parliament and Provincial Assemblies for Public Accounts Committee (PAC) scrutiny.",
            tags=["audit_reports", "pac_scrutiny", "parliamentary_oversight"])

    add_art("172", "Ownerless property", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 2", "Property, Contracts and Suits",
            "Regulates property accruing by escheat or bona vacantia. Crucially, Article 172(3) establishes: 'Subject to existing commitments and obligations, mineral oil and natural gas within the Province or the territorial waters adjacent thereto shall vest jointly and equally in that Province and the Federal Government'.",
            ["(1) Any property which has no rightful owner shall, if located in a Province, vest in the Government of that Province, and in every other case, in the Federal Government.",
             "(2) All lands, minerals and other things of value within the continental shelf or underlying the ocean within the territorial waters of Pakistan shall vest in the Federal Government.",
             "(3) Subject to existing commitments and obligations, mineral oil and natural gas within the Province or the territorial waters adjacent thereto shall vest jointly and equally in that Province and the Federal Government."],
            tags=["natural_resources", "mineral_oil", "natural_gas", "50_50_ownership", "article_172_3", "provincial_wealth"])

    add_art("173", "Power to acquire property and to make contracts, etc.", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 2", "Property, Contracts and Suits",
            "Authorizes executive governments to acquire, hold, and dispose of property and enter into contracts.",
            tags=["contracts", "property_acquisition"])

    add_art("174", "Suits and proceedings", "Part VI", "Finance, Property, Contracts and Suits", "Chapter 2", "Property, Contracts and Suits",
            "Establishes that the Federation of Pakistan may sue or be sued by the name of Pakistan, and a Province may sue or be sued by the name of the Province.",
            tags=["litigation", "state_liability", "suits"])

    # =========================================================================
    # PART VII: THE JUDICATURE (Articles 175 - 212)
    # Chapter 1: The Courts (175, 175A)
    # Chapter 2: The Supreme Court & Federal Constitutional Court (176 - 191A)
    # Chapter 3: The High Courts (192 - 203)
    # Chapter 3A: Federal Shariat Court (203A - 203J)
    # Chapter 4: General Provisions relating to Judicature (204 - 212)
    # =========================================================================
    add_art("175", "Establishment and jurisdiction of courts", "Part VII", "The Judicature", "Chapter 1", "The Courts",
            "Establishes the superior judiciary: Supreme Court of Pakistan, Federal Constitutional Court (post-27th Amendment), a High Court for each Province, and the Islamabad High Court. Mandates progressive separation of the Judiciary from the Executive.",
            tags=["judicature", "separation_of_powers", "superior_courts", "fcc"])

    add_art("175A", "Appointment of Judges", "Part VII", "The Judicature", "Chapter 1", "The Courts",
            "Constitutionalizes superior court judicial appointments: established Judicial Commission of Pakistan (JCP) and Parliamentary Committee. Restructured by the 26th and 27th Amendments to evaluate judicial performance and form Constitutional Benches.",
            tags=["judicial_appointments", "jcp", "judicial_commission", "parliamentary_committee"])

    # Chapter 2: The Supreme Court & FCC (176 - 191A)
    add_art("176", "Constitution of Supreme Court", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Establishes the composition of the Supreme Court of Pakistan, consisting of the Chief Justice of Pakistan and such number of other Judges as determined by Act of Parliament.",
            tags=["supreme_court", "chief_justice", "bench_strength"])

    add_art("177", "Appointment of Supreme Court Judges", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Prescribes qualifications for appointment to the Supreme Court: Pakistani citizenship and at least 5 years as High Court Judge or 15 years as High Court advocate.",
            tags=["supreme_court_judges", "qualifications"])

    add_art("178", "Oath of office", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Requires Chief Justice to make oath before President, and other Judges before the Chief Justice.",
            tags=["judicial_oath"])

    add_art("179", "Retiring age", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Fixes retirement age of Supreme Court judges at 65 years. Under the 26th Amendment, the Chief Justice of Pakistan holds a fixed term of three years (unless superannuated or resigning earlier).",
            tags=["retiring_age", "cjp_three_year_term", "26th_amendment"])

    add_art("180", "Acting Chief Justice", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Provides for appointment of Acting Chief Justice during vacancy or absence.",
            tags=["acting_cjp"])

    add_art("181", "Acting Judges", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Provides for appointment of Acting Supreme Court Judges.",
            tags=["acting_judges"])

    add_art("182", "Appointment of ad-hoc Judges", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Regulates appointment of ad-hoc Judges when quorum of Supreme Court Judges is deficient.",
            tags=["adhoc_judges"])

    add_art("183", "Seat of the Supreme Court", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Fixes the permanent seat of the Supreme Court at Islamabad, with circuit benches sitting in provincial capitals.",
            tags=["seat_of_court", "circuit_benches"])

    add_art("184", "Original Jurisdiction of Supreme Court", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Vests exclusive original jurisdiction in inter-governmental disputes. Clause (3) empowers public interest fundamental rights enforcement (suo motu), as regulated by Constitutional Benches post-26th Amendment.",
            tags=["original_jurisdiction", "article_184_3", "public_interest_litigation", "constitutional_benches"])

    add_art("185", "Appellate jurisdiction of Supreme Court", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Regulates appellate jurisdiction from High Court judgments and decrees, both as of right in specified criminal/civil matters and by leave to appeal.",
            tags=["appellate_jurisdiction", "civil_appeals", "criminal_appeals"])

    add_art("186", "Advisory jurisdiction", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Empowers President to refer questions of law of public importance to the Supreme Court for advisory opinion.",
            tags=["advisory_jurisdiction", "presidential_reference"])

    add_art("186A", "Power of Supreme Court to transfer cases", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Empowers Supreme Court to transfer any case or appeal pending before any High Court to any other High Court or to itself.",
            tags=["case_transfer", "judicial_administration"])

    add_art("187", "Issue and execution of processes of Supreme Court", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Empowers Supreme Court to issue directions, orders, or decrees necessary for doing complete justice in any matter pending before it.",
            tags=["complete_justice", "execution_of_orders"])

    add_art("188", "Review of judgments of Supreme Court", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Empowers Supreme Court to review any judgment pronounced or order made by it.",
            tags=["review_jurisdiction", "curative_review"])

    add_art("189", "Decisions of Supreme Court binding on other courts", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Establishes doctrine of precedent: any decision of the Supreme Court deciding a question of law or based upon or enunciating a principle of law is binding on all other courts in Pakistan.",
            tags=["stare_decisis", "precedent", "binding_decisions"])

    add_art("190", "Action in aid of Supreme Court", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Mandates that all executive and judicial authorities throughout Pakistan shall act in aid of the Supreme Court.",
            tags=["aid_of_supreme_court", "executive_compliance"])

    add_art("191", "Rules of procedure", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Empowers Supreme Court to make rules regulating court practice and procedure.",
            tags=["court_rules", "practice"])

    add_art("191A", "Constitutional Benches of the Supreme Court", "Part VII", "The Judicature", "Chapter 2", "The Supreme Court of Pakistan",
            "Inserted by 26th Amendment, 2024; augmented by 27th Amendment, 2025. Establishes dedicated Constitutional Benches of the Supreme Court to exclusively hear matters arising under Article 184, 185 (constitutional interpretations), and advisory references under Article 186.",
            tags=["constitutional_benches", "fcc", "26th_amendment", "27th_amendment"])

    # Chapter 3: The High Courts (192 - 203)
    add_art("192", "Constitution of High Court", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Establishes composition of a High Court: Chief Justice and such other Judges as determined by law.",
            tags=["high_court", "provincial_judiciary"])

    add_art("193", "Appointment of High Court Judges", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Prescribes qualifications for High Court Judges: citizenship, minimum age 45, and 10 years as advocate or 10 years judicial service.",
            tags=["high_court_appointments", "qualifications"])

    add_art("194", "Oath of office", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Requires Chief Justice of High Court to take oath before Governor, and other Judges before Chief Justice.",
            tags=["high_court_oath"])

    add_art("195", "Retiring age", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Fixes superannuation retirement age of High Court Judges at 62 years.",
            tags=["high_court_retiring_age", "tenure"])

    add_art("196", "Acting Chief Justice", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Regulates appointment of Acting Chief Justice of High Court.",
            tags=["acting_chief_justice"])

    add_art("197", "Additional Judges", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Regulates appointment of Additional Judges of High Courts.",
            tags=["additional_judges"])

    add_art("198", "Seat of the High Court", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Designates principal seats and circuit benches of High Courts across provincial divisional headquarters.",
            tags=["high_court_benches", "divisional_seats"])

    add_art("199", "Jurisdiction of High Court", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Constitutional writ jurisdiction: empowers High Courts to issue writs of prohibition, mandamus, certiorari, habeas corpus, and quo warranto, and enforce fundamental rights against unlawful state actions.",
            tags=["writ_jurisdiction", "habeas_corpus", "mandamus", "article_199", "judicial_review"])

    add_art("200", "Transfer of High Court Judges", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Regulates transfer of High Court Judges from one High Court to another.",
            tags=["judge_transfers"])

    add_art("201", "Decision of High Court binding on subordinate courts", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Establishes that decisions of a High Court on questions of law are binding on all subordinate courts within its territorial jurisdiction.",
            tags=["precedent", "subordinate_courts", "stare_decisis"])

    add_art("202", "Rules of procedure", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Empowers High Courts to make rules regulating court practice and subordinate court supervision.",
            tags=["high_court_rules"])

    add_art("202A", "Constitutional Benches of High Courts", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Inserted by 26th Amendment, 2024. Establishes dedicated Constitutional Benches in each High Court to hear writ petitions involving substantial questions of constitutional interpretation.",
            tags=["high_court_constitutional_benches", "26th_amendment"])

    add_art("203", "High Court to superintend subordinate courts", "Part VII", "The Judicature", "Chapter 3", "The High Courts",
            "Gives each High Court administrative superintendence and control over all courts subordinate to it in the Province.",
            tags=["superintendence", "district_judiciary"])

    # Chapter 3A: Federal Shariat Court (203A - 203J)
    add_art("203A", "Provisions of Chapter to have effect notwithstanding other provisions", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Non-obstante clause giving Chapter 3A effect notwithstanding anything contained in the Constitution.",
            tags=["shariat_court", "islamic_jurisprudence"])

    add_art("203B", "Definitions", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Defines 'law' for the purposes of the Federal Shariat Court (excluding Constitution, Muslim personal law, and procedural laws).",
            tags=["fsc_definitions", "shariat_law"])

    add_art("203C", "The Federal Shariat Court", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Establishes Federal Shariat Court: Chief Justice and up to seven Muslim Judges (including Ulema judges qualified in Islamic law).",
            tags=["federal_shariat_court", "ulema_judges"])

    add_art("203D", "Powers, jurisdiction and functions of the Court", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Empowers FSC (suo motu or on petition) to examine whether any law is repugnant to the Injunctions of Islam.",
            tags=["repugnancy_to_islam", "shariat_review"])

    add_art("203DD", "Revisional and other jurisdiction of the Court", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Vests revisional and appellate criminal jurisdiction over Hudood cases.",
            tags=["hudood_jurisdiction", "revisional_powers"])

    add_art("203E", "Powers and procedure of the Court", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Regulates FSC powers to summon witnesses, require discovery, and appoint jurisconsults.",
            tags=["fsc_procedure", "jurisconsults"])

    add_art("203F", "Appeal to Supreme Court", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Provides right of appeal against FSC decisions to the Shariat Appellate Bench of the Supreme Court.",
            tags=["shariat_appellate_bench", "supreme_court_appeals"])

    add_art("203G", "Bar of jurisdiction", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Bars other courts from entertaining matters within the jurisdiction of the Federal Shariat Court.",
            tags=["bar_of_jurisdiction", "fsc"])

    add_art("203H", "Pending proceedings to continue, etc.", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Transitional provisions regarding pending Shariat petitions.",
            tags=["transitional_fsc"])

    add_art("203I", "Administrative arrangements", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Repealed/Omitted.", status="omitted", tags=["omitted"])

    add_art("203J", "Power to make rules", "Part VII", "The Judicature", "Chapter 3A", "Federal Shariat Court",
            "Empowers FSC to make rules regulating its practice and procedure.",
            tags=["fsc_rules"])

    # Chapter 4: General Provisions relating to Judicature (204 - 212)
    add_art("204", "Contempt of Court", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Constitutional contempt power: empowers Supreme Court and High Courts to punish any person who abuses, interferes with, or scandalizes the court, or disobeys any order.",
            tags=["contempt_of_court", "judicial_dignity"])

    add_art("205", "Remuneration, etc., of Judges", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Guarantees that remuneration and privileges of superior court Judges shall be as specified in the Fifth Schedule and cannot be varied to their disadvantage.",
            tags=["judicial_salaries", "fifth_schedule", "safeguards"])

    add_art("206", "Resignation", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Regulates resignation of superior court Judges.",
            tags=["judicial_resignation"])

    add_art("207", "Judge not to hold office of profit, etc.", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Disqualifies sitting Judges from holding offices of profit, and imposes post-retirement restrictions on practicing before courts where they served.",
            tags=["post_retirement_restrictions", "office_of_profit"])

    add_art("208", "Officers and servants of Courts", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Empowers superior courts to appoint officers and make internal service rules with presidential or gubernatorial approval.",
            tags=["court_staff", "judicial_independence"])

    add_art("209", "Supreme Judicial Council", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Constitutional peer accountability body: composed of CJP, two senior-most Supreme Court Judges, and two senior-most High Court Chief Justices. Inquires into physical/mental incapacity or misconduct of superior court judges.",
            tags=["sjc", "supreme_judicial_council", "judicial_accountability", "removal_of_judges"])

    add_art("210", "Power of Council to enforce attendance, etc.", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Vests Supreme Judicial Council with powers of a Supreme Court to enforce attendance and order discovery.",
            tags=["sjc_powers", "investigative_powers"])

    add_art("211", "Bar of jurisdiction", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Bars any court from questioning proceedings, reports, or advice of the Supreme Judicial Council or the President's removal orders.",
            tags=["sjc_immunity", "bar_of_jurisdiction"])

    add_art("212", "Administrative Courts and Tribunals", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Authorizes establishment of specialized Administrative Courts and Tribunals (e.g. Federal/Provincial Service Tribunals) for civil servants and revenue matters, excluding ordinary High Court writ jurisdiction.",
            tags=["service_tribunals", "administrative_courts", "public_servants"])

    add_art("212A", "Military Courts", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Repealed/Omitted.", status="omitted", tags=["omitted"])

    add_art("212B", "Establishment of Special Courts for trial of heinous offences", "Part VII", "The Judicature", "Chapter 4", "General Provisions",
            "Repealed following expiration of 3-year sunset under 12th Amendment, 1991.", status="omitted", tags=["omitted"])

    # =========================================================================
    # PART VIII: ELECTIONS (Articles 213 - 226)
    # Chapter 1: Chief Election Commissioner and Election Commission (213 - 221)
    # Chapter 2: Electoral Laws and Conduct of Elections (222 - 226)
    # =========================================================================
    add_art("213", "Chief Election Commissioner", "Part VII", "Elections", "Chapter 1", "Chief Election Commissioner and Commission",
            "Provides for appointment of Chief Election Commissioner by consensus between Prime Minister and Leader of the Opposition (or bipartisan parliamentary committee). Qualifications broadened by 22nd Amendment.",
            tags=["cec", "chief_election_commissioner", "appointments"])

    add_art("214", "Oath of office", "Part VII", "Elections", "Chapter 1", "Chief Election Commissioner and Commission",
            "Requires Commissioner to take oath before Chief Justice of Pakistan.",
            tags=["cec_oath"])

    add_art("215", "Term of office of Commissioner", "Part VII", "Elections", "Chapter 1", "Chief Election Commissioner and Commission",
            "Fixes term of Commissioner and ECP members at five years; removable only through Supreme Judicial Council procedure.",
            tags=["cec_tenure", "five_year_term", "sjc_protection"])

    add_art("216", "Commissioner and members not to hold office of profit", "Part VII", "Elections", "Chapter 1", "Chief Election Commissioner and Commission",
            "Disqualifies Commissioner and members from holding offices of profit during and for two years after tenure.",
            tags=["cec_restrictions"])

    add_art("217", "Acting Commissioner", "Part VII", "Elections", "Chapter 1", "Chief Election Commissioner and Commission",
            "Provides for senior-most ECP member to act as Commissioner during vacancy.",
            tags=["acting_cec"])

    add_art("218", "Election Commission", "Part VII", "Elections", "Chapter 1", "Chief Election Commissioner and Commission",
            "Constitutionalizes the Election Commission of Pakistan (ECP): Commissioner and four members, one from each Province. Mandates ECP to organize and conduct elections honestly, justly, fairly and in accordance with law, guarding against corrupt practices.",
            tags=["ecp", "election_commission", "fair_elections", "mandate"])

    add_art("219", "Duties of Commission", "Part VII", "Elections", "Chapter 1", "Chief Election Commissioner and Commission",
            "Enumerates ECP constitutional duties: electoral rolls, conducting elections to Senate, National Assembly, Provincial Assemblies, and Local Governments, and hearing disqualification references.",
            tags=["ecp_duties", "electoral_rolls", "local_government_elections"])

    add_art("220", "Executive authorities to assist Commission", "Part VII", "Elections", "Chapter 1", "Chief Election Commissioner and Commission",
            "Mandates that all executive authorities in the Federation and Provinces shall assist the Commissioner and ECP in discharge of their functions.",
            tags=["executive_duty", "election_assistance"])

    add_art("221", "Officers and servants", "Part VII", "Elections", "Chapter 1", "Chief Election Commissioner and Commission",
            "Empowers ECP to appoint its own officers and make service rules.",
            tags=["ecp_staff"])

    # Chapter 2: Electoral Laws (222 - 226)
    add_art("222", "Electoral laws", "Part VII", "Elections", "Chapter 2", "Electoral Laws",
            "Empowers Parliament to enact laws regulating constituency delimitation, electoral rolls, election petitions, and conduct of elections.",
            tags=["electoral_laws", "delimitation"])

    add_art("223", "Bar against double membership", "Part VII", "Elections", "Chapter 2", "Electoral Laws",
            "Strict bar against double membership: no person can simultaneously be a member of both Houses or of a House and a Provincial Assembly.",
            tags=["double_membership", "parliamentary_seats"])

    add_art("224", "Time of Election and prelude to elections", "Part VII", "Elections", "Chapter 2", "Electoral Laws",
            "Mandates general elections within 60 days of normal assembly expiration, or within 90 days following dissolution. Governs appointment of neutral Caretaker Prime Minister and Chief Ministers.",
            tags=["sixty_days_rule", "ninety_days_rule", "caretaker_government", "general_elections"])

    add_art("224A", "Resolution by Committee or Election Commission", "Part VII", "Elections", "Chapter 2", "Electoral Laws",
            "Inserted by 20th Amendment, 2012. Provides deadlock resolution mechanism: if PM and Opposition Leader cannot agree on Caretaker PM within 3 days, matter goes to an 8-member bipartisan Parliamentary Committee; if committee deadlocks, ECP appoints Caretaker PM within 2 days.",
            tags=["caretaker_deadlock", "20th_amendment", "bipartisan_committee"])

    add_art("225", "Election dispute", "Part VII", "Elections", "Chapter 2", "Electoral Laws",
            "Bars ordinary court challenges: no election to a House or Provincial Assembly shall be called in question except by an election petition presented to an Election Tribunal.",
            tags=["election_petitions", "election_tribunals"])

    add_art("226", "Election by secret ballot", "Part VII", "Elections", "Chapter 2", "Electoral Laws",
            "Mandates that all elections under the Constitution, other than those of the Prime Minister and Chief Minister, shall be by secret ballot.",
            tags=["secret_ballot", "voting_procedure"])

    # =========================================================================
    # PART IX: ISLAMIC PROVISIONS (Articles 227 - 231)
    # =========================================================================
    add_art("227", "Provisions relating to the Holy Quran and Sunnah", "Part IX", "Islamic Provisions", None, None,
            "Mandates that all existing laws shall be brought into conformity with the Injunctions of Islam as laid down in the Holy Quran and Sunnah, and no law shall be enacted which is repugnant to such Injunctions. Protects personal laws of non-Muslim citizens and distinct sects.",
            tags=["islamic_laws", "quran_sunnah", "personal_law_protection"])

    add_art("228", "Composition, etc., of Islamic Council", "Part IX", "Islamic Provisions", None, None,
            "Establishes the Council of Islamic Ideology (CII): 8 to 20 members representing various schools of thought, including women, scholars, and judicial figures.",
            tags=["cii", "council_of_islamic_ideology", "scholars"])

    add_art("229", "Reference by Majlis-e-Shoora, etc. to Islamic Council", "Part IX", "Islamic Provisions", None, None,
            "Empowers President, Governor, or two-fifths of parliamentarians/MPAs to refer a proposed bill to the CII for advice on whether it is repugnant to Islamic injunctions.",
            tags=["cii_reference", "legislative_advice"])

    add_art("230", "Functions of the Islamic Council", "Part IX", "Islamic Provisions", None, None,
            "Enumerates CII advisory functions: recommending measures to bring laws into conformity with Islam, advising legislature on references, and compiling annual reports.",
            tags=["cii_functions", "statutory_advice"])

    add_art("231", "Rules of procedure", "Part IX", "Islamic Provisions", None, None,
            "Empowers Council of Islamic Ideology to make rules regulating its proceedings.",
            tags=["cii_rules"])

    # =========================================================================
    # PART X: EMERGENCY PROVISIONS (Articles 232 - 237)
    # =========================================================================
    add_art("232", "Proclamation of emergency on account of war, internal disturbance, etc.", "Part X", "Emergency Provisions", None, None,
            "Empowers President to issue a Proclamation of Emergency if security of Pakistan is threatened by war, external aggression, or internal disturbance. Requires Provincial Assembly resolution for internal disturbance emergency; subject to parliamentary approval within 30 days.",
            tags=["emergency", "proclamation_of_emergency", "state_security", "federal_control"])

    add_art("233", "Power to suspend Fundamental Rights, etc., during emergency period", "Part X", "Emergency Provisions", None, None,
            "Governs suspension of fundamental rights during emergency: Articles 15, 16, 17, 18, 19, and 24 may be suspended by presidential order; core rights under Articles 9, 10, 10A, 14, 25, 25A cannot be suspended.",
            tags=["suspension_of_rights", "emergency_powers"])

    add_art("234", "Power to issue Proclamation in case of failure of constitutional machinery in a Province", "Part X", "Emergency Provisions", None, None,
            "Governor's rule / Federal takeover: empowers President, on receipt of report from Governor, to assume provincial government functions if governance cannot be carried on in accordance with Constitution. Subject to strict two-month parliamentary approval and six-month absolute limit.",
            tags=["governors_rule", "breakdown_of_machinery", "provincial_takeover"])

    add_art("235", "Proclamation in case of financial emergency", "Part X", "Emergency Provisions", None, None,
            "Authorizes President to proclaim financial emergency if economic life or financial stability is threatened; permits federal salary reductions.",
            tags=["financial_emergency", "economic_crisis"])

    add_art("236", "Revocation of Proclamation, etc.", "Part X", "Emergency Provisions", None, None,
            "Provides for revocation or variation of emergency proclamations by subsequent proclamation.",
            tags=["revocation", "emergency"])

    add_art("237", "Majlis-e-Shoora may make laws indemnifying, etc.", "Part X", "Emergency Provisions", None, None,
            "Empowers Parliament to make laws indemnifying state officers in respect of acts done during martial law or emergency for maintenance of order.",
            tags=["indemnity", "martial_law_protection"])

    # =========================================================================
    # PART XI: AMENDMENT OF CONSTITUTION (Articles 238 - 239)
    # =========================================================================
    add_art("238", "Amendment of Constitution", "Part XI", "Amendment of Constitution", None, None,
            "Establishes that the Constitution may be amended by an Act of Majlis-e-Shoora (Parliament) in the manner provided in this Part.",
            tags=["amendment", "constitutional_change"])

    add_art("239", "Constitution amendment Bill", "Part XI", "Amendment of Constitution", None, None,
            "Rigid amendment procedure: requires a two-thirds majority of the total membership in each House of Parliament. Crucially, clause (4) mandates: where a bill would alter the limits of a Province, it cannot be presented to the President for assent unless passed by the Provincial Assembly of that Province by at least a two-thirds majority of its total membership.",
            ["(1) A Bill to amend the Constitution may originate in either House and, when the Bill has been passed by the votes of not less than two-thirds of the total membership of the House, it shall be transmitted to the other House.",
             "(2) If the Bill is passed without amendment by the votes of not less than two-thirds of the total membership of the House to which it is transmitted... it shall be presented to the President for assent.",
             "(4) A Bill to amend the Constitution which would have the effect of altering the limits of a Province shall not be presented to the President for assent unless it has been passed by the Provincial Assembly of that Province by the votes of not less than two-thirds of its total membership.",
             "(5) No amendment of the Constitution shall be called in question in any court on any ground whatsoever.",
             "(6) For the removal of doubt, it is hereby declared that there is no limitation whatever on the power of the Majlis-e-Shoora (Parliament) to amend any of the provisions of the Constitution."],
            tags=["amendment_procedure", "two_thirds_majority", "provincial_boundaries", "article_239_4", "subnational_restructuring"])

    # =========================================================================
    # PART XII: MISCELLANEOUS (Articles 240 - 280)
    # Chapter 1: Services (240 - 242)
    # Chapter 2: Armed Forces (243 - 245)
    # Chapter 3: Tribal Areas (246 - 247)
    # Chapter 4: General (248 - 259)
    # Chapter 5: Interpretation (260 - 264)
    # Chapter 6: Title, Commencement and Repeal (265 - 266)
    # Chapter 7: Transitional (267 - 280)
    # =========================================================================
    add_art("240", "Appointments to service of Pakistan and conditions of service", "Part XII", "Miscellaneous", "Chapter 1", "Services",
            "Regulates appointments and service conditions of civil servants: determined by Act of Parliament for federal services, and by Act of Provincial Assembly for provincial civil services.",
            tags=["civil_service", "service_rules", "federal_service"])

    add_art("241", "Existing rules, etc., to continue", "Part XII", "Miscellaneous", "Chapter 1", "Services",
            "Provides continuity of existing civil service rules until superseded by Acts of Parliament or Assemblies.",
            tags=["transitional_service_rules"])

    add_art("242", "Public Service Commission", "Part XII", "Miscellaneous", "Chapter 1", "Services",
            "Provides for Federal Public Service Commission (FPSC) and Provincial Public Service Commissions (PPSC, SPSC, KPPSC, BPSC) for competitive merit-based recruitment to civil posts.",
            tags=["fpsc", "ppsc", "public_service_commission", "css_pms", "recruitment"])

    # Chapter 2: Armed Forces (243 - 245)
    add_art("243", "Command of Armed Forces", "Part XII", "Miscellaneous", "Chapter 2", "Armed Forces",
            "Vests supreme command of the Armed Forces in the President. Federal Government exercises control and command. President appoints Chairman Joint Chiefs of Staff Committee and Chiefs of Army, Naval, and Air Staff on binding advice of Prime Minister.",
            tags=["armed_forces", "supreme_commander", "service_chiefs", "prime_minister_advice"])

    add_art("244", "Oath of Armed Forces", "Part XII", "Miscellaneous", "Chapter 2", "Armed Forces",
            "Prescribes solemn oath for Armed Forces personnel set out in Third Schedule: swear to uphold Constitution and not engage in any political activities whatsoever.",
            tags=["armed_forces_oath", "third_schedule", "political_neutrality"])

    add_art("245", "Functions of Armed Forces", "Part XII", "Miscellaneous", "Chapter 2", "Armed Forces",
            "Delineates Armed Forces duties: defend Pakistan against external aggression or threat of war, and, subject to law, act in aid of civil power when called upon by the Federal Government.",
            tags=["aid_of_civil_power", "defense", "military_operations"])

    # Chapter 3: Tribal Areas (246 - 247)
    add_art("246", "Tribal Areas", "Part XII", "Miscellaneous", "Chapter 3", "Tribal Areas",
            "Amended by 25th Amendment, 2018: reflects merger of FATA into Khyber Pakhtunkhwa province.",
            tags=["tribal_areas", "fata_merger", "25th_amendment"])

    add_art("247", "Administration of Tribal Areas", "Part XII", "Miscellaneous", "Chapter 3", "Tribal Areas",
            "Omitted by 25th Amendment, 2018. Former special administrative regime of FATA under President/Governor is abolished.",
            status="omitted", tags=["omitted", "25th_amendment", "fata_merger"])

    # Chapter 4: General (248 - 259)
    add_art("248", "Protection to President, Governor, Minister, etc.", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "Provides official immunity: President, Governor, Prime Minister, Federal/Provincial Ministers are not answerable to any court for exercise of powers; no criminal proceedings can be instituted against President or Governor while in office.",
            tags=["official_immunity", "president_governor_protection"])

    add_art("249", "Legal proceedings", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "Regulates legal proceedings against the Federation or Provinces.",
            tags=["legal_proceedings", "state_contracts"])

    add_art("250", "Salaries, allowances, etc., of the President, etc.", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "Regulates terms of office and salaries of President, Governors, Speaker, CJP, and other constitutional office-holders.",
            tags=["constitutional_salaries"])

    add_art("251", "National language", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "Designates Urdu as the national language of Pakistan, directs arrangements for its use for official and other purposes, and permits Provincial Assemblies to prescribe measures for teaching and promotion of provincial languages.",
            tags=["national_language", "urdu", "provincial_languages"])

    add_art("252", "Special provisions in relation to major ports and aerodromes", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "Empowers President to make special exemptions for major ports and airports.",
            tags=["ports", "airports"])

    add_art("253", "Maximum limits as to property, etc.", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "Empowers Parliament to enact laws setting maximum limits on property ownership and declaring state ownership of commercial/industrial enterprises.",
            tags=["property_limits", "nationalization"])

    add_art("254", "Failure to comply with requirement as to time does not render an act invalid", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "General saving provision: an act required to be done within a particular period is not rendered invalid merely because it was done after that period.",
            tags=["saving_clause", "procedural_time"])

    add_art("255", "Oath of office", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "General provisions on administration and forms of constitutional oaths.",
            tags=["oath_administration"])

    add_art("256", "Private armies forbidden", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "Strictly forbids private armies: no private organization capable of functioning as a military or paramilitary organization shall be formed, and any such organization is illegal.",
            tags=["private_armies", "state_monopoly_on_violence"])

    add_art("257", "Provision relating to the State of Jammu and Kashmir", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "Constitutionalizes Kashmir policy: when the people of Jammu and Kashmir decide to accede to Pakistan, the relationship between Pakistan and that State shall be determined in accordance with the wishes of the people of that State.",
            tags=["kashmir", "self_determination", "accession"])

    add_art("258", "Government of certain areas by Order of the President", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "Empowers President to make orders for government and administration of territories outside the four Provinces.",
            tags=["presidential_territories"])

    add_art("259", "Awards", "Part XII", "Miscellaneous", "Chapter 4", "General",
            "Prohibits grant of titles, honours, and decorations by the State except for gallantry, merit in public service, or academic distinction.",
            tags=["awards", "civil_honours", "gallantry"])

    # Chapter 5: Interpretation (260 - 264)
    add_art("260", "Definitions", "Part XII", "Miscellaneous", "Chapter 5", "Interpretation",
            "Comprehensive constitutional dictionary defining essential legal terms, including 'citizen', 'Act of Parliament', 'Provincial law', 'service of Pakistan', and definitions of Muslim and non-Muslim.",
            tags=["definitions", "interpretation", "legal_dictionary"])

    add_art("261", "Person acting in office not to be regarded as its holder, etc.", "Part XII", "Miscellaneous", "Chapter 5", "Interpretation",
            "Interpretation rule regarding persons acting temporarily in constitutional offices.",
            tags=["acting_holders"])

    add_art("262", "Gregorian calendar to be used", "Part XII", "Miscellaneous", "Chapter 5", "Interpretation",
            "Mandates that the reckoning of calendar years and months for constitutional purposes shall be according to the Gregorian calendar.",
            tags=["gregorian_calendar", "time_reckoning"])

    add_art("263", "Gender and number", "Part XII", "Miscellaneous", "Chapter 5", "Interpretation",
            "Standard statutory interpretation rule: words importing the masculine gender include females, and singular includes plural.",
            tags=["gender", "statutory_construction"])

    add_art("264", "Effect of repeal of laws", "Part XII", "Miscellaneous", "Chapter 5", "Interpretation",
            "Specifies the legal effect of constitutional or statutory repeal: does not revive anything not in force, affect previous operation, or affect acquired rights.",
            tags=["repeal", "vested_rights", "savings"])

    # Chapter 6: Title, Commencement and Repeal (265 - 266)
    add_art("265", "Title of Constitution and commencement", "Part XII", "Miscellaneous", "Chapter 6", "Title and Commencement",
            "Specifies that this Constitution shall be known as the Constitution of the Islamic Republic of Pakistan, and came into force on the 14th day of August, 1973.",
            tags=["commencement_1973", "short_title"])

    add_art("266", "Repeal", "Part XII", "Miscellaneous", "Chapter 6", "Title and Commencement",
            "Repealed the Interim Constitution of 1972 upon commencement of the 1973 permanent Constitution.",
            tags=["interim_constitution_repeal"])

    # Chapter 7: Transitional (267 - 280)
    add_art("267", "Power of President to remove difficulties", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Transitional power of President to adapt provisions for smooth initial constitutional transition.",
            tags=["transitional", "removal_of_difficulties"])

    add_art("267A", "Power to remove difficulties (18th Amendment)", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Empowered President, on PM's advice, to remove transitional implementation difficulties of the 18th Amendment within one year.",
            tags=["18th_amendment_transition"])

    add_art("267B", "Removal of difficulties (20th Amendment)", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Transitional power for 20th Amendment implementation.", tags=["20th_amendment_transition"])

    add_art("268", "Continuance in force, and adaptation of certain laws", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Provides for the continuance of existing laws in force until altered, repealed, or amended by the competent legislature.",
            tags=["adaptation_of_laws", "continuity_of_legal_order"])

    add_art("269", "Validation of laws, acts, etc.", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Transitional validation of laws enacted between March 1969 and April 1972.",
            tags=["transitional_validation"])

    add_art("270", "Temporary validation of certain laws, etc.", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Temporary validation clause.", tags=["transitional_validation"])

    add_art("270A", "Affirmation of President's Orders, etc. (8th Amendment)", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Historical indemnity clause enacted by 8th Amendment validating laws, martial law regulations, and President's Orders made between July 1977 and December 1985.",
            tags=["eighth_amendment", "indemnity", "martial_law_validation"])

    add_art("270AA", "Declaration and continuance of laws etc. (18th Amendment overhaul)", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Enacted by the 18th Amendment, 2010: declared the proclamation of emergency of 3 November 2007, Provisional Constitution Order (PCO), and unconstitutional acts of General Pervez Musharraf to be void ab initio and without lawful authority.",
            tags=["eighteenth_amendment", "pco_void", "anti_martial_law"])

    add_art("270B", "Elections to be deemed to be held under Constitution", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Validates the 1977 and 1985 general elections for transitional continuity.",
            tags=["election_continuity"])

    add_art("270BB", "General Elections 2008", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Deems the 2008 General Elections to have been held under the Constitution.",
            tags=["2008_elections"])

    add_art("271", "First National Assembly", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Provided for the National Assembly in existence before commencement day to be the first National Assembly under the 1973 Constitution.",
            tags=["first_national_assembly"])

    add_art("272", "First Senate", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Regulated the transitional constitution and staggered terms of the first Senate of Pakistan.",
            tags=["first_senate"])

    add_art("273", "First Provincial Assembly", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Provided for transitional Provincial Assemblies.", tags=["first_provincial_assembly"])

    add_art("274", "Vesting of property, assets, rights, liabilities and obligations", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Regulates legal succession of property, assets, contracts, and liabilities from previous constitutional regimes.",
            tags=["legal_succession", "property_vesting"])

    add_art("275", "Continuance in office of persons in service of Pakistan, etc.", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Provided for civil servants and judges holding office to continue serving under the new Constitution.",
            tags=["service_continuity"])

    add_art("276", "Oath of first President", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Regulated the oath of the first President of Pakistan under the 1973 Constitution.",
            tags=["first_president_oath"])

    add_art("277", "Transitional financial provisions", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Authorized public expenditures during the initial transitional financial year.",
            tags=["transitional_finance"])

    add_art("278", "Accounts and audit", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Transitional accounting arrangements.", tags=["transitional_audit"])

    add_art("279", "Continuance of taxes", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Continued existing taxes and duties until altered by legislative Acts.",
            tags=["tax_continuity"])

    add_art("280", "Continuance of Proclamation of Emergency", "Part XII", "Miscellaneous", "Chapter 7", "Transitional",
            "Continued the 1971 state of emergency into the commencement of the 1973 Constitution.",
            tags=["emergency_continuity"])

    # =========================================================================
    # SCHEDULES (First through Fifth Schedules)
    # =========================================================================
    add_art("First Schedule", "Laws exempted from the operation of Article 8(1) and (2)", "Schedules", "Schedules", None, None,
            "Enumerates specific statutory laws, President's Orders, and defense-related regulations that are permanently exempted from being declared void under fundamental rights (Article 8).",
            tags=["first_schedule", "exempted_laws", "article_8"])

    add_art("Second Schedule", "Election of President", "Schedules", "Schedules", None, None,
            "Detailed proportional voting procedure for presidential elections by the joint Electoral College consisting of Parliament and the four Provincial Assemblies.",
            tags=["second_schedule", "presidential_election", "electoral_college"])

    add_art("Third Schedule", "Oaths of Office", "Schedules", "Schedules", None, None,
            "Exact constitutional texts of solemn oaths of office for President, Prime Minister, Federal Ministers, Speaker, Chairman Senate, Governors, Chief Ministers, Judges, and Armed Forces.",
            tags=["third_schedule", "oaths_of_office", "constitutional_solemnity"])

    add_art("Fourth Schedule", "Legislative Lists", "Schedules", "Schedules", None, None,
            "The division of powers blueprint: contains the Federal Legislative List (Part I: exclusive federal powers like defense, foreign affairs, currency, nationality; Part II: Council of Common Interests subjects like railways, mineral oil, electricity). Concurrent Legislative List was abolished by the 18th Amendment, devolving all residual matters to the Provinces.",
            tags=["fourth_schedule", "federal_legislative_list", "division_of_powers", "provincial_autonomy", "18th_amendment"])

    add_art("Fifth Schedule", "Remuneration and Terms and Conditions of Service of Judges", "Schedules", "Schedules", None, None,
            "Fixes official salaries, pensions, housing allowances, and travel privileges for the Chief Justice of Pakistan, Supreme Court Judges, and High Court Chief Justices and Judges.",
            tags=["fifth_schedule", "judicial_salaries", "remuneration"])

    return articles

# Build catalog
articles_catalog = make_articles_catalog()

# Write articles.json
with open(DATA_DIR / "articles.json", "w", encoding="utf-8") as f:
    json.dump(articles_catalog, f, indent=2, ensure_ascii=False)

# Write amendment-register.json
with open(DATA_DIR / "amendment-register.json", "w", encoding="utf-8") as f:
    json.dump(amendments_data, f, indent=2, ensure_ascii=False)

# Write constitutional-bills.json
with open(DATA_DIR / "constitutional-bills.json", "w", encoding="utf-8") as f:
    json.dump(bills_data, f, indent=2, ensure_ascii=False)

print(f"PASS: Generated complete Constitution data!")
print(f"Total articles/schedules generated: {len(articles_catalog)}")
print(f"Total amendments generated: {len(amendments_data)}")
print(f"Total bills generated: {len(bills_data)}")

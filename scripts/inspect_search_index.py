import json

with open('search-index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total search index entries: {len(data)}")
print("First entry:", data[0] if data else "Empty")
# Check if insights is already in index
has_insights = any('/insights/' in item.get('url', '') for item in data)
print("Has insights in search index?", has_insights)

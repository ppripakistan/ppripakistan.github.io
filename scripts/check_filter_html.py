with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_filters = text.find('class="vi-filter')
if idx_filters != -1:
    print(text[idx_filters-50:idx_filters+600])
else:
    print("vi-filter not found, searching for filter")
    idx = text.find('filter')
    print(text[idx-50:idx+300])

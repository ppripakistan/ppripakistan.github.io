with open('assets/css/visual-insights.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('vi-nav-pills')
if idx != -1:
    print(text[idx-50:idx+600])
else:
    print("vi-nav-pills not in CSS, searching pill")
    idx = text.find('pill')
    print(text[idx-50:idx+400])

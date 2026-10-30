with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="card-prov-matrix"')
div_start = text.rfind('<div class="vi-card', 0, start)
print("Start of card-prov-matrix:")
print(text[div_start:div_start+800])
print("\nEnd of insights/index.html around card-prov-matrix:")
print(text[-2000:])

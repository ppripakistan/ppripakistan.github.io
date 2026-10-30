with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="card-prov-matrix"')
div_start = text.rfind('<div class="vi-card', 0, start)
footer_pos = text.find('class="vi-card-footer"', div_start)
actions_pos = text.find('class="vi-actions"', footer_pos)
end_card = text.find('</div>\n        </div>', actions_pos)
if end_card == -1:
    end_card = text.find('</div>\r\n        </div>', actions_pos)

print("Card 16 end found at:", end_card)
card_16_html = text[div_start:end_card + len('</div>\n        </div>')]
print("Card 16 HTML length:", len(card_16_html))
print("Last 200 chars:\n", card_16_html[-200:])

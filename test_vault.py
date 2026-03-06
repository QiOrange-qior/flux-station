import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

idx = html.find('<!-- Asset 6 (1:1) -->')
end_divs = html[idx:idx+2000]
print(end_divs)

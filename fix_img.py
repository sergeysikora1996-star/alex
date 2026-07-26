import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('46vw, 70px', '65vw, 110px')
html = html.replace('width="70"', 'width="110"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

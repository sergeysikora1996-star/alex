import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('65vw, 110px', '85vw, 150px')
html = html.replace('width="110"', 'width="150"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '''</div>\n</div>\n<script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js''',
    '''</div>\n</div>\n</div>\n</div>\n<script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

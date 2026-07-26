import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '''                              <path d="M12.5 16H12.51" stroke="#F05252" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>\n                            </svg></div>\n                        </div>\n                    </div>''',
    '''                              <path d="M12.5 16H12.51" stroke="#F05252" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>\n                            </svg></div>\n                        </div>\n                      </form>\n                    </div>'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

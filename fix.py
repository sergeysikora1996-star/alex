import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: section-hero missing closes
html = html.replace(
    '''              </a>\n        </div>\n      </section>''',
    '''              </a>\n            </div>\n          </div>\n        </div>\n      </section>'''
)

# Fix 2: section-bonuses extra closes
html = html.replace(
    '''          </div>\n        </div>\n      </section>\n          </div>\n        </div>\n      </section>\n      <section class="section-timer-cta">''',
    '''          </div>\n        </div>\n      </section>\n      <section class="section-timer-cta">'''
)

# Fix 3: section-plan missing closes
html = html.replace(
    '''                  <h3 class="plan_card_title">Зідзвон із ментором</h3>\n                  <div class="plan_card_paragraph">У вас буде зідзвон 1 на 1</div>\n                </div>\n      </section>''',
    '''                  <h3 class="plan_card_title">Зідзвон із ментором</h3>\n                  <div class="plan_card_paragraph">У вас буде зідзвон 1 на 1</div>\n                </div>\n              </div>\n            </div>\n          </div>\n        </div>\n      </section>'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

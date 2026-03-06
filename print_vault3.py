from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

vault_view = soup.find(id='vault-view')
if vault_view:
    # check for aside in vault_view
    aside = vault_view.find('aside')
    if aside:
        print("Aside found in vault_view!")
        print(aside.prettify()[:1000])
    else:
        print("No aside in vault-view.")
        # just print the tabs
        buttons = vault_view.find('div', class_='flex gap-6 border-b')
        if buttons:
            print(buttons.prettify())

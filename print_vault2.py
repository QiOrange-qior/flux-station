from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

vault_view = soup.find(id='vault-view')
if vault_view:
    print(vault_view.prettify()[2000:4000])

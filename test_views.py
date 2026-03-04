import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("video view present:", '<div id="video-view"' in content)
print("api view present:", '<div id="api-view"' in content)
print("vault view present:", '<div id="vault-view"' in content)

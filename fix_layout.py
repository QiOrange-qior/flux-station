import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove w-full and add min-w-0 to all view wrappers
content = re.sub(r'class="flex-1 flex w-full h-full([^"]*)"', r'class="flex-1 flex h-full min-w-0\1"', content)

with open('index.html', 'w') as f:
    f.write(content)

print("Layout fix applied.")

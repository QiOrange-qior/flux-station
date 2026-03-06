import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix the duplicated divs around "存储空间"
content = re.sub(
    r'<div class="p-4 border-t border-gray-100 dark:border-gray-800">\s*<div class="p-4 border-t border-gray-100 dark:border-gray-800">',
    r'<div class="p-4 border-t border-gray-100 dark:border-gray-800">',
    content
)

# Fix the extra closing tags
content = re.sub(
    r'<div class="bg-primary h-1.5 rounded-full" style="width: 12%"><\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<div class="p-4 border-t border-gray-100 dark:border-gray-800">',
    r'<div class="bg-primary h-1.5 rounded-full" style="width: 12%"></div>\n        </div>\n    </div>\n    <div class="p-4 border-t border-gray-100 dark:border-gray-800">',
    content
)

with open('index.html', 'w') as f:
    f.write(content)

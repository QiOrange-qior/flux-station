import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace body class to center a 16:9 container
body_start = content.find('<body class="')
body_end = content.find('>', body_start) + 1

new_body = '<body class="bg-gray-200 dark:bg-gray-950 h-screen w-screen overflow-hidden flex items-center justify-center selection:bg-primary selection:text-white transition-colors duration-300">\n'
new_body += '<!-- 16:9 Container -->\n'
new_body += '<div class="relative w-full max-w-[1920px] aspect-video max-h-screen bg-background-light dark:bg-background-dark text-text-main-light dark:text-text-main-dark overflow-hidden flex shadow-2xl xl:rounded-2xl border border-gray-300 dark:border-gray-800">'

content = content[:body_start] + new_body + content[body_end:]

# Close the 16:9 container before </body>
body_close = content.find('</body>')
content = content[:body_close] + '</div>\n' + content[body_close:]

with open('index.html', 'w') as f:
    f.write(content)

print("Applied 16:9 container")

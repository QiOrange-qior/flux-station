import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure the Ignite button properly triggers the results view
if 'onclick="switchView(\'results\')"' not in content:
    content = content.replace(
        '<button class="bg-[#6366F1] hover:bg-[#5558e3] text-white font-medium rounded-full px-6 py-3 transition-colors flex items-center gap-2 group">',
        '<button onclick="switchView(\'results\')" class="bg-[#6366F1] hover:bg-[#5558e3] text-white font-medium rounded-full px-6 py-3 transition-colors flex items-center gap-2 group">'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

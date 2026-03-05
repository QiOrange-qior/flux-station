import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the Assets Library header and its tabs
pattern = r'(<h3[^>]*>Assets Library</h3>\s*)<p[^>]*>Curated Collection</p>\s*<div class="flex items-center gap-4 mb-6">.*?</div>'

replacement = r'''\1<p class="text-[10px] uppercase tracking-[0.2em] text-[#6366F1]/80 dark:text-[#6366F1]/80 font-bold mb-6">Recent History</p>
            <div class="flex gap-2 p-1 bg-[#F5F3FF] dark:bg-gray-800 rounded-xl mb-6 border border-[#EDE9FE] dark:border-gray-700">
                <button class="flex-1 py-2 px-2 rounded-lg bg-white dark:bg-gray-700 shadow-sm text-[11px] font-bold text-[#6366F1] dark:text-white flex items-center justify-center gap-1.5 uppercase tracking-wide border border-[#EDE9FE] dark:border-gray-600">
                    Recent
                </button>
                <button class="flex-1 py-2 px-2 rounded-lg text-[11px] font-bold text-[#6B7280] dark:text-gray-400 hover:text-[#6366F1] dark:hover:text-white transition-colors flex items-center justify-center gap-1.5 uppercase tracking-wide">
                    Collections
                </button>
            </div>'''

new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

if count > 0:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully replaced {count} occurrences.")
else:
    print("Pattern not found!")

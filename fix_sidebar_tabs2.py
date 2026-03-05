import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for the generation view sidebar header:
pattern = r'<h3 class="font-serif text-2xl[^>]*>Assets Library</h3>.*?<div class="flex gap-2 p-1[^>]*>.*?</div>'

new_header_code = """<h3 class="font-serif text-[32px] text-[#111827] dark:text-gray-100 mb-2 tracking-tight">Assets Library</h3>
            <p class="text-[11px] uppercase tracking-widest text-[#6B7280] dark:text-gray-400 font-semibold mb-6">Curated Collection</p>
            <div class="flex items-center gap-4 mb-6">
                <button class="flex items-center gap-2 px-3.5 py-2 rounded-xl bg-white dark:bg-gray-800 shadow-sm border border-gray-200 dark:border-gray-700 text-sm font-semibold text-[#111827] dark:text-white transition-all">
                    <span class="material-symbols-outlined text-[18px]">folder</span>
                    My Files
                </button>
                <button class="flex items-center gap-1.5 px-1 py-2 text-sm font-medium text-slate-500 hover:text-[#111827] dark:text-slate-400 dark:hover:text-white transition-colors">
                    <span class="material-symbols-outlined text-[18px]">history</span>
                    History
                </button>
                <button class="flex items-center gap-1.5 px-1 py-2 text-sm font-medium text-slate-500 hover:text-[#111827] dark:text-slate-400 dark:hover:text-white transition-colors">
                    <span class="material-symbols-outlined text-[18px]">favorite</span>
                    Saved
                </button>
            </div>"""

new_content = re.sub(pattern, new_header_code, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replaced!")

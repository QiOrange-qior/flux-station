import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# The pattern to replace
# We need to find the right sidebar header which currently has:
# <h3 class="font-serif text-2xl text-text-main-light dark:text-text-main-dark mb-1">Assets Library</h3>
# <p class="text-[10px] uppercase tracking-[0.2em] text-primary/60 dark:text-primary/40 font-black mb-6">Recent History</p>
# <div class="flex gap-2 p-1 bg-gray-50 dark:bg-gray-800/50 rounded-xl mb-6 border border-gray-100 dark:border-gray-700/50">...</div>

# We will replace it for ALL sidebars in the file (there are multiple <aside> tags for different views).
# Actually, the right sidebar in "generation-view", "plaza-view", etc.

new_header_code = """<h3 class="font-serif text-[28px] text-[#111827] dark:text-gray-100 mb-2 tracking-tight">Assets Library</h3>
            <p class="text-[11px] uppercase tracking-widest text-slate-500 dark:text-slate-400 font-semibold mb-6">Curated Collection</p>
            <div class="flex items-center gap-1 mb-6">
                <button class="flex items-center gap-1.5 px-3 py-1.5 rounded-[10px] bg-white dark:bg-gray-800 shadow-[0_1px_2px_rgba(0,0,0,0.05)] border border-gray-200 dark:border-gray-700 text-[13px] font-semibold text-[#111827] dark:text-white transition-all">
                    <span class="material-symbols-outlined text-[18px]">folder_open</span>
                    My Files
                </button>
                <button class="flex items-center gap-1.5 px-3 py-1.5 rounded-[10px] text-[13px] font-medium text-slate-500 hover:text-[#111827] dark:text-slate-400 dark:hover:text-white transition-colors">
                    <span class="material-symbols-outlined text-[18px]">history</span>
                    History
                </button>
                <button class="flex items-center gap-1.5 px-3 py-1.5 rounded-[10px] text-[13px] font-medium text-slate-500 hover:text-[#111827] dark:text-slate-400 dark:hover:text-white transition-colors">
                    <span class="material-symbols-outlined text-[18px]">favorite</span>
                    Saved
                </button>
            </div>"""

# Replace in index.html
# Need a robust regex since there are multiple views.
# Wait, let's check how many right sidebars there are.
# In generation-view:
# <div class="p-6 pb-2 border-b border-gray-100 dark:border-gray-800">
# ...
# In other views there might not be a right sidebar (video-view is hidden, etc.)

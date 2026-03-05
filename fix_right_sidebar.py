import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# The specific right sidebar code to replace
old_sidebar_pattern = r'<!-- Sidebar / Library -->.*?<aside class="w-80 flex-shrink-0 border-l border-gray-200 dark:border-gray-800 bg-surface-light/50 dark:bg-surface-dark/50 backdrop-blur-md z-20 flex flex-col h-full">.*?</aside>'

new_sidebar_code = """<!-- Sidebar / Library -->
    <aside class="w-80 flex-shrink-0 border-l border-gray-200 dark:border-gray-800 bg-surface-light/50 dark:bg-surface-dark/50 backdrop-blur-md z-20 flex flex-col h-full relative">
        <div class="p-6 pb-4">
            <h3 class="font-serif text-2xl text-text-main-light dark:text-text-main-dark mb-1">Assets Library</h3>
            <p class="text-[10px] uppercase tracking-[0.2em] text-primary/60 dark:text-primary/40 font-black mb-6">Recent History</p>
            <div class="flex gap-2 p-1 bg-gray-50 dark:bg-gray-800/50 rounded-xl mb-6 border border-gray-100 dark:border-gray-700/50">
                <button class="flex-1 py-2 px-2 rounded-lg bg-white dark:bg-gray-700 shadow-sm text-[10px] font-bold text-primary flex items-center justify-center gap-1.5 uppercase tracking-wide border border-gray-100 dark:border-gray-600">
                    Recent
                </button>
                <button class="flex-1 py-2 px-2 rounded-lg text-[10px] font-bold text-slate-400 hover:text-primary transition-colors flex items-center justify-center gap-1.5 uppercase tracking-wide">
                    Collections
                </button>
            </div>
            <div class="grid grid-cols-2 gap-3 overflow-y-auto max-h-[calc(100vh-280px)] no-scrollbar pr-1">
                <div class="aspect-square rounded-2xl overflow-hidden border border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-gray-800 group cursor-pointer relative hover:shadow-md transition-all">
                    <img alt="Old gen" class="w-full h-full object-cover group-hover:scale-110 transition-transform" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAjDTJ_TDCOqlVAOFTjJ1PTZhF48F8a0oW0-A2yoWUCJEY5cHOr0ag8UuyP6l_ajopHOkRhplhxSoJ-oBv-scj5xTW57reVwjQZAhoBprTK_g-m0uO-9pzSSw3H0Wtw45PqhS8kSCxtMZsGjQo21wY8b2b1r1Qi8NmBmopBpI5Fm-Z6noTiHsjeaQFC3eVX-Y-5aGYxsPwGS0cipQrEjETV-3XRvHgJ8NjmVHkKtKmtvqkV7cisLA48vAh_hP4MxHrg93OPDw8e0uTj"/>
                    <div class="absolute inset-0 bg-primary/20 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                </div>
                <div class="aspect-square rounded-2xl overflow-hidden border border-gray-100 dark:border-gray-700 bg-white dark:bg-gray-800 group cursor-pointer relative hover:shadow-md transition-all">
                    <div class="w-full h-full flex items-center justify-center bg-gradient-to-br from-indigo-50 to-white dark:from-indigo-900/20 dark:to-gray-800">
                        <span class="material-symbols-outlined text-primary/30">bubble_chart</span>
                    </div>
                </div>
                <div class="aspect-square rounded-2xl overflow-hidden border border-gray-100 dark:border-gray-700 bg-white dark:bg-gray-800 group cursor-pointer relative hover:shadow-md transition-all">
                    <div class="w-full h-full flex items-center justify-center bg-gradient-to-tr from-pink-50 to-white dark:from-pink-900/20 dark:to-gray-800">
                        <span class="material-symbols-outlined text-primary/30">texture</span>
                    </div>
                </div>
                <div class="aspect-square rounded-2xl overflow-hidden border border-gray-100 dark:border-gray-700 bg-white dark:bg-gray-800 group cursor-pointer relative hover:shadow-md transition-all">
                    <div class="w-full h-full flex items-center justify-center bg-gradient-to-bl from-orange-50 to-white dark:from-orange-900/20 dark:to-gray-800">
                        <span class="material-symbols-outlined text-primary/30">shapes</span>
                    </div>
                </div>
                <div class="aspect-square rounded-2xl overflow-hidden border border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-gray-800 group cursor-pointer relative hover:shadow-md transition-all">
                    <div class="w-full h-full flex items-center justify-center bg-gray-50 dark:bg-gray-800">
                        <span class="material-symbols-outlined text-gray-300 dark:text-gray-600">cloud_queue</span>
                    </div>
                </div>
                <div class="aspect-square rounded-2xl overflow-hidden border border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-gray-800 group cursor-pointer relative hover:shadow-md transition-all">
                    <div class="w-full h-full flex items-center justify-center bg-gray-50 dark:bg-gray-800">
                        <span class="material-symbols-outlined text-gray-300 dark:text-gray-600">image</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="mt-auto p-6 border-t border-gray-100 dark:border-gray-800 bg-gray-50/40 dark:bg-gray-900/40">
            <div class="flex justify-between items-center mb-3">
                <span class="text-[10px] font-bold text-gray-400 dark:text-gray-500 uppercase tracking-widest">Storage used</span>
                <span class="text-[10px] font-bold text-primary">24.8 GB / 100 GB</span>
            </div>
            <div class="w-full bg-white dark:bg-gray-800 rounded-full h-2 border border-gray-100 dark:border-gray-700 p-0.5">
                <div class="bg-gradient-to-r from-primary to-[#A855F7] h-full rounded-full" style="width: 24.8%"></div>
            </div>
            <button class="w-full mt-4 py-3 rounded-xl text-[10px] font-black text-primary border border-primary/20 hover:bg-primary/5 transition-colors uppercase tracking-[0.2em]">
                Upgrade Storage
            </button>
        </div>
    </aside>"""

new_content = re.sub(old_sidebar_pattern, new_sidebar_code, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Right sidebar updated.")

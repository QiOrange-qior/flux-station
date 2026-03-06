import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

tabs_html = """                <div class="flex gap-6 border-b border-gray-200 dark:border-gray-700">
                    <button id="tab-all-gens" onclick="switchVaultTab('all')" class="pb-3 text-sm font-semibold text-primary border-b-2 border-primary">所有生成 (All Generations)</button>
                    <button id="tab-history" onclick="switchVaultTab('history')" class="pb-3 text-sm font-medium text-gray-500 hover:text-gray-800 dark:hover:text-gray-200 transition-colors">历史 (History)</button>
                    <button id="tab-favorites" onclick="switchVaultTab('favorites')" class="pb-3 text-sm font-medium text-gray-500 hover:text-gray-800 dark:hover:text-gray-200 transition-colors">收藏夹 (Favorites)</button>
                    <button id="tab-videos" onclick="switchVaultTab('videos')" class="pb-3 text-sm font-medium text-gray-500 hover:text-gray-800 dark:hover:text-gray-200 transition-colors">视频资产 (Videos)</button>
                </div>"""

# Replace tabs
html = re.sub(
    r'<div class="flex gap-6 border-b border-gray-200 dark:border-gray-700">[\s\S]*?视频资产 \(Videos\)</button>\s*</div>',
    tabs_html,
    html
)

# Replace the columns container to have an ID
html = html.replace('<div class="columns-1 sm:columns-2 lg:columns-3 xl:columns-4 gap-6 space-y-6">', '<div id="vault-all-gens" class="columns-1 sm:columns-2 lg:columns-3 xl:columns-4 gap-6 space-y-6">')

# Add the history container after the vault-all-gens div closes.
history_html = """
                <!-- History Module -->
                <div id="vault-history" class="hidden flex-col gap-10">
                    <div class="space-y-4">
                        <h3 class="text-sm font-bold text-gray-800 dark:text-gray-200 border-b border-gray-100 dark:border-gray-800 pb-2">今天 (Today)</h3>
                        <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
                            <!-- History Item -->
                            <div class="group relative rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-all border border-gray-100 dark:border-gray-800 aspect-square">
                                <img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAjDTJ_TDCOqlVAOFTjJ1PTZhF48F8a0oW0-A2yoWUCJEY5cHOr0ag8UuyP6l_ajopHOkRhplhxSoJ-oBv-scj5xTW57reVwjQZAhoBprTK_g-m0uO-9pzSSw3H0Wtw45PqhS8kSCxtMZsGjQo21wY8b2b1r1Qi8NmBmopBpI5Fm-Z6noTiHsjeaQFC3eVX-Y-5aGYxsPwGS0cipQrEjETV-3XRvHgJ8NjmVHkKtKmtvqkV7cisLA48vAh_hP4MxHrg93OPDw8e0uTj" alt="History Item">
                                <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-between p-2">
                                    <div class="flex justify-end">
                                        <button class="bg-white/20 hover:bg-white/40 backdrop-blur-sm rounded-lg p-1 text-white transition-colors"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                    </div>
                                    <p class="text-[10px] text-white/90 truncate">A futuristic city...</p>
                                </div>
                            </div>
                            <!-- History Item -->
                            <div class="group relative rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-all border border-gray-100 dark:border-gray-800 aspect-square">
                                <img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDhuGajJtnXR1sorOl6O549zjHT_8aMphzK-NSigaX5SlHpZEIF6yXl9BOv1CE7f9XrqiPNSqu5hrl04IK9UeN9D3vkdwSsrNvp-URHL3MgPuNZB9-XjrPkeslL034y8G5r6yeTUK5fMx2IFE8qSVY6XRu2Wy5WYuGR2SwEOokLdWONxbfk_YXmaqRmqVF0WGeqZRQ22geyasbY7UdkiNgeuRjK_wBR14aoEVy6-rANke-WrM07Jq0nB-4S6gVu0Ez3kCBu8uZa_1QQ" alt="History Item">
                                <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-between p-2">
                                    <div class="flex justify-end">
                                        <button class="bg-white/20 hover:bg-white/40 backdrop-blur-sm rounded-lg p-1 text-white transition-colors"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                    </div>
                                    <p class="text-[10px] text-white/90 truncate">Abstract digital art...</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="space-y-4">
                        <h3 class="text-sm font-bold text-gray-800 dark:text-gray-200 border-b border-gray-100 dark:border-gray-800 pb-2">昨天 (Yesterday)</h3>
                        <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
                            <!-- History Item -->
                            <div class="group relative rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-all border border-gray-100 dark:border-gray-800 aspect-square">
                                <img class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCBwlXCdeDU2DlLOBQdLdj5MjQMMR9R1yYJBGv05_VL3_UYGDJbtpPKvbCLp-ALK7e-KQKF4gdzJyDSjlNylsL5vigFFu_IDIkkNulDROGaRJsYJwlKw-stLhfp3YaVLxIhwJiLo1gTkB10W1wWvvz_oUlHVphq1B0XX1QnGzUq2OCUTF6Fn2peILXG3gUR6SCfYhqGd7bUdZcG9R-NpG3WAc-29gJ-BAS5PdRIB2TaNrRuhGx7jj0t9LlXXlrVVOwbUvV3NDe-b8E3" alt="History Item">
                                <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col justify-between p-2">
                                    <div class="flex justify-end">
                                        <button class="bg-white/20 hover:bg-white/40 backdrop-blur-sm rounded-lg p-1 text-white transition-colors"><span class="material-symbols-outlined text-[16px]">more_horiz</span></button>
                                    </div>
                                    <p class="text-[10px] text-white/90 truncate">Iridescent oil slick...</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
"""

# We need to find the end of vault-all-gens.
# It's at the end of the p-10 div before </main>
# Actually, the structure is:
# <div class="p-10">
#     <div id="vault-all-gens" ...>
#        ...
#     </div>
# </div>
# </main>
# Let's just insert it before `</main>` and make sure it's inside `p-10` by regex.
# Wait, let's insert it right after the closing tag of vault-all-gens.
html = re.sub(r'(<div id="vault-all-gens"[^>]*>[\s\S]*?<!-- Asset 6 \(1:1\) -->[\s\S]*?</div>\s*</div>\s*</div>)', r'\1' + history_html, html)


script_addition = """
        function switchVaultTab(tab) {
            const tabs = ['all-gens', 'history', 'favorites', 'videos'];

            // Default classes
            const activeClass = 'pb-3 text-sm font-semibold text-primary border-b-2 border-primary'.split(' ');
            const inactiveClass = 'pb-3 text-sm font-medium text-gray-500 hover:text-gray-800 dark:hover:text-gray-200 transition-colors'.split(' ');

            tabs.forEach(t => {
                const tabEl = document.getElementById('tab-' + t);
                const contentEl = document.getElementById('vault-' + t);

                if (t === tab) {
                    if(tabEl) {
                        tabEl.classList.remove(...inactiveClass);
                        tabEl.classList.add(...activeClass);
                    }
                    if(contentEl) contentEl.classList.remove('hidden');
                } else {
                    if(tabEl) {
                        tabEl.classList.remove(...activeClass);
                        tabEl.classList.add(...inactiveClass);
                        // Make sure to add pb-3 text-sm etc back
                        tabEl.className = 'pb-3 text-sm font-medium text-gray-500 hover:text-gray-800 dark:hover:text-gray-200 transition-colors';
                    }
                    if(contentEl) contentEl.classList.add('hidden');
                }
            });
        }
"""

html = html.replace('function switchView(viewId) {', script_addition + '\n        function switchView(viewId) {')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done")

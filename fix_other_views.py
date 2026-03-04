import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add IDs to navigation links
content = content.replace(
    '<a class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)">\n                <span class="material-symbols-outlined mr-3 text-[20px]">movie</span>\n                视频生成\n            </a>',
    '<a id="nav-video" class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)" onclick="switchView(\'video\')">\n                <span class="material-symbols-outlined mr-3 text-[20px]">movie</span>\n                视频生成\n            </a>'
)

content = content.replace(
    '<a class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)">\n                <span class="material-symbols-outlined mr-3 text-[20px]">api</span>\n                API管理\n            </a>',
    '<a id="nav-api" class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)" onclick="switchView(\'api\')">\n                <span class="material-symbols-outlined mr-3 text-[20px]">api</span>\n                API管理\n            </a>'
)

content = content.replace(
    '<a class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)">\n                <span class="material-symbols-outlined mr-3 text-[20px]">folder_special</span>\n                资产\n            </a>',
    '<a id="nav-vault" class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)" onclick="switchView(\'vault\')">\n                <span class="material-symbols-outlined mr-3 text-[20px]">folder_special</span>\n                资产\n            </a>'
)

# Append new view divs
views = """
<div id="video-view" class="flex-1 flex w-full h-full hidden">
<main class="flex-1 relative flex flex-col h-full overflow-hidden bg-[#FFFCFC] dark:bg-[#09090b] transition-colors"><div class="absolute inset-0 z-0 pointer-events-none overflow-hidden"><div class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-purple-100/40 dark:bg-purple-900/10 rounded-full blur-[120px]"></div></div><div class="flex-1 z-10 flex flex-col h-full w-full relative overflow-y-auto overflow-x-hidden p-10"><h2 class="font-serif text-5xl text-text-main-light dark:text-text-main-dark tracking-tight mb-6">视频生成 (Video Gen)</h2><p class="text-gray-500">Coming soon...</p></div></main>
</div>

<div id="api-view" class="flex-1 flex w-full h-full hidden">
<main class="flex-1 relative flex flex-col h-full overflow-hidden bg-[#FFFCFC] dark:bg-[#09090b] transition-colors"><div class="absolute inset-0 z-0 pointer-events-none overflow-hidden"><div class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-purple-100/40 dark:bg-purple-900/10 rounded-full blur-[120px]"></div></div><div class="flex-1 z-10 flex flex-col h-full w-full relative overflow-y-auto overflow-x-hidden p-10"><h2 class="font-serif text-5xl text-text-main-light dark:text-text-main-dark tracking-tight mb-6">API管理 (API Settings)</h2><p class="text-gray-500">Coming soon...</p></div></main>
</div>

<div id="vault-view" class="flex-1 flex w-full h-full hidden">
<main class="flex-1 relative flex flex-col h-full overflow-hidden bg-[#FFFCFC] dark:bg-[#09090b] transition-colors"><div class="absolute inset-0 z-0 pointer-events-none overflow-hidden"><div class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-purple-100/40 dark:bg-purple-900/10 rounded-full blur-[120px]"></div></div><div class="flex-1 z-10 flex flex-col h-full w-full relative overflow-y-auto overflow-x-hidden p-10"><h2 class="font-serif text-5xl text-text-main-light dark:text-text-main-dark tracking-tight mb-6">资产 (Project Vault)</h2><p class="text-gray-500">Coming soon...</p></div></main>
</div>
"""

content = content.replace('<!-- Configuration Modal Overlay -->', views + '\n<!-- Configuration Modal Overlay -->')

# Update JS function
old_js = """function switchView(view) {
    const genView = document.getElementById('generation-view');
    const plazaView = document.getElementById('plaza-view');
    const navGen = document.getElementById('nav-gen');
    const navPlaza = document.getElementById('nav-plaza');

    const activeClasses = ['bg-white', 'dark:bg-gray-800', 'shadow-sm', 'border', 'border-gray-100', 'dark:border-gray-700', 'text-primary'];
    const inactiveClasses = ['nav-link', 'text-text-muted-light', 'dark:text-text-muted-dark', 'hover:bg-gray-50', 'dark:hover:bg-gray-800', 'hover:text-text-main-light', 'dark:hover:text-text-main-dark', 'relative', 'overflow-hidden'];

    if (view === 'gen') {
        genView.classList.remove('hidden');
        plazaView.classList.add('hidden');

        navGen.classList.add(...activeClasses);
        navGen.classList.remove(...inactiveClasses);

        navPlaza.classList.add(...inactiveClasses);
        navPlaza.classList.remove(...activeClasses);
    } else if (view === 'plaza') {
        plazaView.classList.remove('hidden');
        genView.classList.add('hidden');

        navPlaza.classList.add(...activeClasses);
        navPlaza.classList.remove(...inactiveClasses);

        navGen.classList.add(...inactiveClasses);
        navGen.classList.remove(...activeClasses);
    }
}"""

new_js = """function switchView(view) {
    const views = ['gen', 'video', 'plaza', 'api', 'vault'];

    const activeClasses = ['bg-white', 'dark:bg-gray-800', 'shadow-sm', 'border', 'border-gray-100', 'dark:border-gray-700', 'text-primary'];
    const inactiveClasses = ['nav-link', 'text-text-muted-light', 'dark:text-text-muted-dark', 'hover:bg-gray-50', 'dark:hover:bg-gray-800', 'hover:text-text-main-light', 'dark:hover:text-text-main-dark', 'relative', 'overflow-hidden'];

    views.forEach(v => {
        const viewEl = document.getElementById(v === 'gen' ? 'generation-view' : v + '-view');
        const navEl = document.getElementById('nav-' + v);

        if (!viewEl || !navEl) return;

        if (v === view) {
            viewEl.classList.remove('hidden');
            navEl.classList.add(...activeClasses);
            navEl.classList.remove(...inactiveClasses);
        } else {
            viewEl.classList.add('hidden');
            navEl.classList.add(...inactiveClasses);
            navEl.classList.remove(...activeClasses);
        }
    });
}"""

content = content.replace(old_js, new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

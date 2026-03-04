import re

# Read the old index (with generation UI)
with open('old_index.html', 'r', encoding='utf-8') as f:
    old_content = f.read()

# Read the current index (with model plaza UI)
with open('index.html', 'r', encoding='utf-8') as f:
    plaza_content = f.read()

# Extract the main generation UI from old_content
gen_main_start = old_content.find('<main class="flex-1 relative flex flex-col h-full overflow-hidden bg-[#FFFCFC] dark:bg-[#09090b] transition-colors">')
gen_main_end = old_content.find('</main>', gen_main_start) + 7
gen_main_html = old_content[gen_main_start:gen_main_end]

gen_aside_start = old_content.find('<aside class="w-80 flex-shrink-0 border-l border-gray-200 dark:border-gray-800 bg-surface-light/50 dark:bg-surface-dark/50 backdrop-blur-md z-20 flex flex-col h-full">')
gen_aside_end = old_content.find('</aside>', gen_aside_start) + 8
gen_aside_html = old_content[gen_aside_start:gen_aside_end]

gen_modal_start = old_content.find('<!-- Configuration Modal Overlay -->')
gen_modal_end = old_content.find('</script>', old_content.find('<script>', gen_modal_start)) + 9
if gen_modal_start != -1:
     # actually, the modal and script in old_index.html goes until the end before </body>
     gen_modal_end = old_content.find('</body>', gen_modal_start)
     gen_modal_html = old_content[gen_modal_start:gen_modal_end]
else:
     gen_modal_html = ""


# Extract the plaza UI from plaza_content
plaza_main_start = plaza_content.find('<main class="flex-1 relative flex flex-col h-full overflow-hidden bg-[#FFFCFC] dark:bg-[#09090b] transition-colors">')
plaza_main_end = plaza_content.find('</main>', plaza_main_start) + 7
plaza_main_html = plaza_content[plaza_main_start:plaza_main_end]

# Wrap them in divs
gen_view_html = f'<div id="generation-view" class="flex-1 flex w-full h-full">\n{gen_main_html}\n{gen_aside_html}\n</div>'
plaza_view_html = f'<div id="plaza-view" class="flex-1 flex w-full h-full hidden">\n{plaza_main_html}\n</div>'

# We will inject this into a clean skeleton. We can use plaza_content as the base and replace its <main> and <aside>
# Find the start of <main> in plaza_content
main_start_idx = plaza_content.find('<main class="flex-1')
# Find the end of <aside> in plaza_content
aside_end_idx = plaza_content.find('</aside>', main_start_idx) + 8

# Replace the content between main_start and aside_end with our two views
new_body_content = gen_view_html + '\n' + plaza_view_html

# Update sidebar active states to use IDs
sidebar_html = plaza_content[:main_start_idx]
sidebar_html = sidebar_html.replace('href="#"', 'href="javascript:void(0)"')
sidebar_html = sidebar_html.replace('nav-link flex items-center', 'nav-link flex items-center sidebar-nav-item')
sidebar_html = sidebar_html.replace('flex items-center px-3 py-2.5 text-sm font-medium rounded-xl transition-all bg-white dark:bg-gray-800 shadow-sm border border-gray-100 dark:border-gray-700 text-primary group', 'nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden sidebar-nav-item')

# Let's cleanly rebuild the sidebar navigation
nav_start = sidebar_html.find('<nav class="space-y-1">')
nav_end = sidebar_html.find('</nav>', nav_start) + 6

new_nav = """<nav class="space-y-1">
            <a id="nav-gen" class="flex items-center px-3 py-2.5 text-sm font-medium rounded-xl bg-white dark:bg-gray-800 shadow-sm border border-gray-100 dark:border-gray-700 text-primary group transition-all" href="javascript:void(0)" onclick="switchView('gen')">
                <span class="material-symbols-outlined mr-3 text-[20px]">auto_awesome</span>
                素材生成
            </a>
            <a class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)">
                <span class="material-symbols-outlined mr-3 text-[20px]">movie</span>
                视频生成
            </a>
            <a id="nav-plaza" class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)" onclick="switchView('plaza')">
                <span class="material-symbols-outlined mr-3 text-[20px]">grid_view</span>
                模型广场
            </a>
            <a class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)">
                <span class="material-symbols-outlined mr-3 text-[20px]">api</span>
                API管理
            </a>
            <a class="nav-link flex items-center px-3 py-2.5 text-sm font-medium rounded-xl text-text-muted-light dark:text-text-muted-dark hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-text-main-light dark:hover:text-text-main-dark transition-all relative overflow-hidden" href="javascript:void(0)">
                <span class="material-symbols-outlined mr-3 text-[20px]">folder_special</span>
                资产
            </a>
        </nav>"""

sidebar_html = sidebar_html[:nav_start] + new_nav + sidebar_html[nav_end:]


# JavaScript for view switching
view_switcher_js = """
<script>
function switchView(view) {
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
}
</script>
"""

# Extract script tags from both to ensure we keep them
scripts_start = plaza_content.find('<script>', aside_end_idx)
plaza_scripts = plaza_content[scripts_start:] if scripts_start != -1 else "</body></html>"

final_html = sidebar_html + new_body_content + '\n' + gen_modal_html + '\n' + view_switcher_js + '\n' + plaza_scripts

# Replace duplicated body/html tags
final_html = final_html.replace('</body>\n</html>\n</body></html>', '</body></html>')
final_html = final_html.replace('</body></html>\n</body></html>', '</body></html>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully merged UI views.")

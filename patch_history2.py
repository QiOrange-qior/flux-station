import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# I need to check where it injected the history module
if 'id="vault-history"' not in html:
    print("History container not found, patching manually.")
    # Find the end of vault-all-gens container

    parts = html.split('id="vault-all-gens"')

    # Actually let's just insert it by finding <!-- Asset 6 (1:1) -->
    p1, p2 = html.split('<!-- Asset 6 (1:1) -->')

    # p2 has the closing divs
    closing_divs = p2.find('</div>', p2.find('</div>') + 1)

    # Actually wait. Let's just find <div class="p-10"> in vault-view
    vault_p10_idx = html.rfind('<div class="p-10">', 0, html.find('</main>'))
    if vault_p10_idx != -1:
        # let's just replace inside p-10
        print("Found p-10")

    # Wait, the history was not injected, let's inject it.
    history_html = """
                <!-- History Module -->
                <div id="vault-history" class="hidden flex-col gap-8">
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
    # Insert it right before the closing div of <div class="p-10"> in vault-view
    # Wait, the vault-view <div class="p-10"> has id="vault-all-gens" inside.
    # So finding <div id="vault-all-gens" and its closing tag is tricky without a proper parser.
    # Let's just find "<!-- Asset 6 (1:1) -->" and the two `</div>`s that follow it.
    idx = html.find('<!-- Asset 6 (1:1) -->')
    if idx != -1:
        # find the next two </div>
        end_idx = html.find('</div>', idx)
        end_idx = html.find('</div>', end_idx + 1)
        # Add the history_html right after the end_idx + 6
        end_idx += 6
        html = html[:end_idx] + history_html + html[end_idx:]

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Patched history html.")

import re

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Re-apply vault view carefully, handling exact matching from current index.html
    # We will search for <div id="vault-view" and the next <!-- RESULTS VIEW to replace it.

    vault_content = """<div id="vault-view" class="flex-1 flex h-full min-w-0 hidden">
    <main class="flex-1 relative flex flex-col h-full overflow-hidden bg-[#F9F9FB] dark:bg-[#09090b] transition-colors">
        <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
            <div class="absolute top-1/4 right-1/4 w-[600px] h-[600px] bg-indigo-100/40 dark:bg-indigo-900/10 rounded-full blur-[120px]"></div>
        </div>

        <div class="flex-1 z-10 flex flex-col h-full w-full relative overflow-y-auto overflow-x-hidden custom-scrollbar">
            <div class="sticky top-0 z-30 pt-10 pb-6 px-10 bg-[#F9F9FB]/80 dark:bg-[#09090b]/80 backdrop-blur-xl border-b border-gray-100/50 dark:border-gray-800/50 flex flex-col gap-6">
                <div class="flex items-end justify-between">
                    <h2 class="font-serif text-5xl text-text-main-light dark:text-text-main-dark tracking-tight">Project <span class="text-iris-gradient italic">Vault</span>.</h2>
                    <div class="flex gap-3">
                        <button class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-200 text-sm font-medium rounded-xl px-4 py-2.5 transition-colors shadow-sm hover:shadow-md flex items-center gap-2">
                            <span class="material-symbols-outlined text-[18px]">filter_list</span>筛选
                        </button>
                        <button class="bg-[#6366F1] hover:bg-[#5558e3] text-white text-sm font-medium rounded-xl px-5 py-2.5 transition-colors shadow-glow-primary flex items-center gap-2">
                            <span class="material-symbols-outlined text-[18px]">create_new_folder</span>新建合集
                        </button>
                    </div>
                </div>

                <div class="flex gap-6 border-b border-gray-200 dark:border-gray-700">
                    <button class="pb-3 text-sm font-semibold text-primary border-b-2 border-primary">所有生成 (All Generations)</button>
                    <button class="pb-3 text-sm font-medium text-gray-500 hover:text-gray-800 dark:hover:text-gray-200 transition-colors">收藏夹 (Favorites)</button>
                    <button class="pb-3 text-sm font-medium text-gray-500 hover:text-gray-800 dark:hover:text-gray-200 transition-colors">视频资产 (Videos)</button>
                </div>
            </div>

            <div class="p-10">
                <div class="columns-1 sm:columns-2 lg:columns-3 xl:columns-4 gap-6 space-y-6">
                    <!-- Asset 1 (16:9) -->
                    <div class="break-inside-avoid relative group rounded-[24px] overflow-hidden shadow-sm hover:shadow-floating transition-all duration-500 hover:-translate-y-1 bg-white border border-gray-100 dark:border-gray-800">
                        <img class="w-full h-auto object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBMbFP54OkePxxiyR89odXu1KverWJTEfXFuGy1OduAQns-Nf1CfCul2f4SuSDIKbsqq4HXMFd3pFpShn1F6u-nmf14ClWZlhNpAtnYsG3hmMKQln0mxulIxeF8DXsy53Vh9eXJc-zD9kuHK5vdG3kXcYA4QJ1RoT3HGSTTaPjWc9UnK3souRNjxHQIMaFpH8wLD1RAbBNktv5i7mCfePS1FgBppiR7RmfGZB3HlHunRehix9hfgpSqmdI3Xw0EHPW3HxQ0xbrj7PU7" alt="Cinematic 16:9">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        <div class="absolute top-3 right-3 bg-black/50 backdrop-blur-md px-2.5 py-1 rounded-full border border-white/20 shadow-sm opacity-0 group-hover:opacity-100 transition-all translate-y-2 group-hover:translate-y-0">
                            <span class="text-[10px] font-bold text-white tracking-wider">16:9</span>
                        </div>
                        <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                            <div class="bg-white/90 dark:bg-black/60 backdrop-blur-md rounded-2xl p-2 flex gap-2 shadow-2xl scale-95 group-hover:scale-100 transition-transform">
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700" title="下载"><span class="material-symbols-outlined text-[18px]">download</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700" title="重新生成"><span class="material-symbols-outlined text-[18px]">replay</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-pink-500 hover:text-white transition-colors text-gray-700" title="收藏"><span class="material-symbols-outlined text-[18px]">favorite</span></button>
                            </div>
                        </div>
                    </div>

                    <!-- Asset 2 (4:5) -->
                    <div class="break-inside-avoid relative group rounded-[24px] overflow-hidden shadow-sm hover:shadow-floating transition-all duration-500 hover:-translate-y-1 bg-white border border-gray-100 dark:border-gray-800">
                        <img class="w-full h-auto object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDv4xkKxRrWob2cDxas59tYImxsvr706WnvVWMQM1ql1KywOpcN3iNpuhCRVhJQGwkzTyvZ9CcZQPgJZubgR76DaGpulfqV8FiNRYWzGFagWzxP7WguN2LSz0rRpvDPo1HXN_fArch8exoTT-K2Fmnapai9UFgM8-Bd8lQcfrydWh-QwtjDgKb9KWo5PngnXjSJ_HglLoyZnUj_QthOsd6UHTr-s6c4j2QsYeHJpdcLEVwUlqr8U_HXpT19bBStNELTycGirWOHH6JI" alt="Portrait">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        <div class="absolute top-3 right-3 bg-black/50 backdrop-blur-md px-2.5 py-1 rounded-full border border-white/20 shadow-sm opacity-0 group-hover:opacity-100 transition-all translate-y-2 group-hover:translate-y-0">
                            <span class="text-[10px] font-bold text-white tracking-wider">4:5</span>
                        </div>
                        <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                            <div class="bg-white/90 dark:bg-black/60 backdrop-blur-md rounded-2xl p-2 flex gap-2 shadow-2xl scale-95 group-hover:scale-100 transition-transform">
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">download</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">replay</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-pink-500 hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">favorite</span></button>
                            </div>
                        </div>
                    </div>

                    <!-- Asset 3 (1:1) -->
                    <div class="break-inside-avoid relative group rounded-[24px] overflow-hidden shadow-sm hover:shadow-floating transition-all duration-500 hover:-translate-y-1 bg-white border border-gray-100 dark:border-gray-800">
                        <img class="w-full h-auto object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCBwlXCdeDU2DlLOBQdLdj5MjQMMR9R1yYJBGv05_VL3_UYGDJbtpPKvbCLp-ALK7e-KQKF4gdzJyDSjlNylsL5vigFFu_IDIkkNulDROGaRJsYJwlKw-stLhfp3YaVLxIhwJiLo1gTkB10W1wWvvz_oUlHVphq1B0XX1QnGzUq2OCUTF6Fn2peILXG3gUR6SCfYhqGd7bUdZcG9R-NpG3WAc-29gJ-BAS5PdRIB2TaNrRuhGx7jj0t9LlXXlrVVOwbUvV3NDe-b8E3" alt="Square">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        <div class="absolute top-3 right-3 bg-black/50 backdrop-blur-md px-2.5 py-1 rounded-full border border-white/20 shadow-sm opacity-0 group-hover:opacity-100 transition-all translate-y-2 group-hover:translate-y-0">
                            <span class="text-[10px] font-bold text-white tracking-wider">1:1</span>
                        </div>
                        <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                            <div class="bg-white/90 dark:bg-black/60 backdrop-blur-md rounded-2xl p-2 flex gap-2 shadow-2xl scale-95 group-hover:scale-100 transition-transform">
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">download</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">replay</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-pink-500 hover:text-white transition-colors text-pink-500"><span class="material-symbols-outlined text-[18px] fill-current">favorite</span></button>
                            </div>
                        </div>
                    </div>

                    <!-- Asset 4 (3:4) -->
                    <div class="break-inside-avoid relative group rounded-[24px] overflow-hidden shadow-sm hover:shadow-floating transition-all duration-500 hover:-translate-y-1 bg-white border border-gray-100 dark:border-gray-800">
                        <img class="w-full h-auto object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDhuGajJtnXR1sorOl6O549zjHT_8aMphzK-NSigaX5SlHpZEIF6yXl9BOv1CE7f9XrqiPNSqu5hrl04IK9UeN9D3vkdwSsrNvp-URHL3MgPuNZB9-XjrPkeslL034y8G5r6yeTUK5fMx2IFE8qSVY6XRu2Wy5WYuGR2SwEOokLdWONxbfk_YXmaqRmqVF0WGeqZRQ22geyasbY7UdkiNgeuRjK_wBR14aoEVy6-rANke-WrM07Jq0nB-4S6gVu0Ez3kCBu8uZa_1QQ" alt="Vertical">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        <div class="absolute top-3 right-3 bg-black/50 backdrop-blur-md px-2.5 py-1 rounded-full border border-white/20 shadow-sm opacity-0 group-hover:opacity-100 transition-all translate-y-2 group-hover:translate-y-0">
                            <span class="text-[10px] font-bold text-white tracking-wider">3:4</span>
                        </div>
                        <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                            <div class="bg-white/90 dark:bg-black/60 backdrop-blur-md rounded-2xl p-2 flex gap-2 shadow-2xl scale-95 group-hover:scale-100 transition-transform">
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">download</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">replay</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-pink-500 hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">favorite</span></button>
                            </div>
                        </div>
                    </div>

                    <!-- Asset 5 (16:9 Video placeholder) -->
                    <div class="break-inside-avoid relative group rounded-[24px] overflow-hidden shadow-sm hover:shadow-floating transition-all duration-500 hover:-translate-y-1 bg-gray-900 border border-gray-800">
                        <div class="w-full aspect-video flex items-center justify-center bg-gradient-to-tr from-indigo-900/50 to-purple-900/50">
                            <span class="material-symbols-outlined text-white/50 text-6xl">play_circle</span>
                        </div>
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        <div class="absolute top-3 right-3 bg-primary/80 backdrop-blur-md px-2.5 py-1 rounded-full border border-white/20 shadow-sm opacity-0 group-hover:opacity-100 transition-all translate-y-2 group-hover:translate-y-0 flex items-center gap-1">
                            <span class="material-symbols-outlined text-[12px] text-white">movie</span>
                            <span class="text-[10px] font-bold text-white tracking-wider">0:04</span>
                        </div>
                        <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                            <div class="bg-white/90 dark:bg-black/60 backdrop-blur-md rounded-2xl p-2 flex gap-2 shadow-2xl scale-95 group-hover:scale-100 transition-transform">
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">download</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-pink-500 hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">favorite</span></button>
                            </div>
                        </div>
                    </div>

                    <!-- Asset 6 (1:1) -->
                    <div class="break-inside-avoid relative group rounded-[24px] overflow-hidden shadow-sm hover:shadow-floating transition-all duration-500 hover:-translate-y-1 bg-white border border-gray-100 dark:border-gray-800">
                        <img class="w-full h-auto object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDacAJ-yhHGgISLQJxTkny7rtBqoJtNIPHYkP4Kg1or6xl4E6I3q2mfpOE3y58emF5xdVEM5fjR5u3-F4PZB-7zxifGjarFF7h2eTIZx45sguRV_07VV8LNxT5BsFJms4BUXbXaGUeGETmFSmQZeztGhgGacuyyP2V_L3Rh5thBRH7pYqy_cA_JBjdHoJbxyBMyCQm2_xAhnZaDA9PQQJ0MlRkMOYYQZoX5rk4kg1vZcbUXrJCGmG7QDCwCiwXC7Dgj7doDQ-W-KCOA" alt="Neon">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        <div class="absolute top-3 right-3 bg-black/50 backdrop-blur-md px-2.5 py-1 rounded-full border border-white/20 shadow-sm opacity-0 group-hover:opacity-100 transition-all translate-y-2 group-hover:translate-y-0">
                            <span class="text-[10px] font-bold text-white tracking-wider">1:1</span>
                        </div>
                        <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                            <div class="bg-white/90 dark:bg-black/60 backdrop-blur-md rounded-2xl p-2 flex gap-2 shadow-2xl scale-95 group-hover:scale-100 transition-transform">
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">download</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-primary hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">replay</span></button>
                                <button class="p-2.5 rounded-xl bg-white/80 hover:bg-pink-500 hover:text-white transition-colors text-gray-700"><span class="material-symbols-outlined text-[18px]">favorite</span></button>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </main>
</div>"""

    # Replace old vault-view with new vault-view
    html = re.sub(
        r'<div id="vault-view" class="flex-1 flex h-full min-w-0 hidden">.*?</div>\n\n<!-- RESULTS VIEW',
        f'{vault_content}\n\n<!-- RESULTS VIEW',
        html,
        flags=re.DOTALL
    )

    sidebar_tabs_html = """
            <div class="flex gap-2 mb-6">
                <button class="flex items-center justify-center gap-2 px-4 py-2 rounded-xl bg-white dark:bg-gray-800 shadow-sm border border-gray-200 dark:border-gray-700 text-sm font-semibold text-text-main-light dark:text-white z-10 hover:shadow-md transition-all">
                    <span class="material-symbols-outlined text-[18px]">folder_open</span>
                    My Files
                </button>
                <button class="flex items-center justify-center gap-1.5 px-3 py-2 text-[13px] font-medium text-gray-500 dark:text-gray-400 hover:text-text-main-light dark:hover:text-white z-10 transition-colors">
                    <span class="material-symbols-outlined text-[18px]">history</span>
                    History
                </button>
                <button class="flex items-center justify-center gap-1.5 px-3 py-2 text-[13px] font-medium text-gray-500 dark:text-gray-400 hover:text-text-main-light dark:hover:text-white z-10 transition-colors">
                    <span class="material-symbols-outlined text-[18px]">favorite_border</span>
                    Saved
                </button>
            </div>
"""

    html = re.sub(
        r'<div class="flex gap-2 mb-6">.*?</div>\n\s*<div class="grid grid-cols-2 gap-3 overflow-y-auto',
        f'{sidebar_tabs_html}            <div class="grid grid-cols-2 gap-3 overflow-y-auto',
        html,
        flags=re.DOTALL
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    update_index()

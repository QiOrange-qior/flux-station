import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

styles = """
        /* Result Grid Styles */
        .reveal-delay-1 { animation-delay: 0.1s; }
        .reveal-delay-2 { animation-delay: 0.25s; }
        .reveal-delay-3 { animation-delay: 0.4s; }
        .reveal-delay-4 { animation-delay: 0.55s; }
        .reveal-delay-5 { animation-delay: 0.7s; }
        .reveal-delay-6 { animation-delay: 0.85s; }
        .reveal-sweep { animation: revealSweep 2s ease-out forwards; }
        @keyframes revealSweep {
            0% { clip-path: polygon(0 0, 0 0, 0 100%, 0% 100%); }
            100% { clip-path: polygon(0 0, 150% 0, 100% 150%, 0% 100%); }
        }
        @keyframes successFlash {
            0% { box-shadow: 0 0 0 rgba(99, 102, 241, 0); }
            30% { box-shadow: 0 0 30px rgba(99, 102, 241, 0.6), inset 0 0 20px rgba(99, 102, 241, 0.3); }
            100% { box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); }
        }
        .animate-success-flash { animation: successFlash 1s ease-out forwards; }
        @keyframes revealFade {
            0% { opacity: 0; transform: scale(0.95) translateY(10px); filter: blur(10px); }
            100% { opacity: 1; transform: scale(1) translateY(0); filter: blur(0); }
        }
        .animate-reveal-fade { animation: revealFade 0.8s ease-out forwards; }
"""

content = content.replace('</style>', styles + '\n</style>')

# Add the results view section
results_view = """
<div id="results-view" class="flex-1 flex w-full h-full hidden">
<main class="flex-1 relative flex flex-col h-full overflow-hidden bg-[#FFFCFC] dark:bg-[#09090b] transition-colors"><div class="absolute inset-0 z-0 pointer-events-none overflow-hidden"><div class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-purple-100/40 dark:bg-purple-900/10 rounded-full blur-[120px]"></div></div>

    <header class="h-16 flex items-center justify-between px-8 z-10 shrink-0 border-b border-gray-100 dark:border-gray-800 bg-white/50 dark:bg-gray-900/50 backdrop-blur-md">
        <div class="flex items-center gap-2">
            <span class="text-xs font-medium text-gray-400">Workspace / </span>
            <span class="text-xs font-bold text-primary">Untitled Generation #04</span>
        </div>
        <div class="flex items-center gap-4">
            <button class="text-xs font-bold px-4 py-2 rounded-full border border-gray-200 dark:border-gray-700 bg-white/80 dark:bg-gray-800 hover:bg-white dark:hover:bg-gray-700 transition-colors">Share</button>
            <button class="text-xs font-bold px-4 py-2 rounded-full bg-primary text-white shadow-lg shadow-primary/20 hover:scale-105 transition-transform">Export All</button>
            <button onclick="switchView('gen')" class="text-xs font-bold px-4 py-2 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"><span class="material-symbols-outlined text-[14px] align-middle">close</span></button>
        </div>
    </header>

    <div class="flex-1 overflow-y-auto overflow-x-hidden p-8 pb-32 z-10 custom-scrollbar">
        <div class="max-w-6xl mx-auto">
            <div class="mb-10 text-center">
                <h2 class="font-serif text-5xl mb-3 text-text-main-light dark:text-text-main-dark tracking-tight">
                    Truly <span class="text-iris-gradient italic animate-shimmer-sweep bg-clip-text">vivid</span> results.
                </h2>
                <p class="text-gray-400 font-light max-w-md mx-auto text-sm">Reviewing generated assets from your prompt.</p>
            </div>

            <div class="masonry-grid">
                <div class="masonry-item relative w-full aspect-[4/5] rounded-xl overflow-hidden shadow-floating bg-white/50 dark:bg-gray-800/50 backdrop-blur-sm border border-gray-200 dark:border-gray-700 group opacity-0 animate-reveal-fade animate-success-flash reveal-delay-1 cursor-pointer">
                    <img onclick="openAssetDetail(this.src)" alt="Portrait of a futuristic city" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDv4xkKxRrWob2cDxas59tYImxsvr706WnvVWMQM1ql1KywOpcN3iNpuhCRVhJQGwkzTyvZ9CcZQPgJZubgR76DaGpulfqV8FiNRYWzGFagWzxP7WguN2LSz0rRpvDPo1HXN_fArch8exoTT-K2Fmnapai9UFgM8-Bd8lQcfrydWh-QwtjDgKb9KWo5PngnXjSJ_HglLoyZnUj_QthOsd6UHTr-s6c4j2QsYeHJpdcLEVwUlqr8U_HXpT19bBStNELTycGirWOHH6JI"/>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
                    <div class="absolute bottom-0 left-0 w-full p-4 transform translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300 pointer-events-none">
                        <p class="text-xs font-medium text-white/90">Portrait 4:5</p>
                    </div>
                </div>

                <div class="masonry-item relative w-full aspect-square rounded-xl overflow-hidden shadow-floating bg-white/50 dark:bg-gray-800/50 backdrop-blur-sm border border-gray-200 dark:border-gray-700 group opacity-0 animate-reveal-fade animate-success-flash reveal-delay-2 cursor-pointer">
                    <img onclick="openAssetDetail(this.src)" alt="Iridescent oil slick texture" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCBwlXCdeDU2DlLOBQdLdj5MjQMMR9R1yYJBGv05_VL3_UYGDJbtpPKvbCLp-ALK7e-KQKF4gdzJyDSjlNylsL5vigFFu_IDIkkNulDROGaRJsYJwlKw-stLhfp3YaVLxIhwJiLo1gTkB10W1wWvvz_oUlHVphq1B0XX1QnGzUq2OCUTF6Fn2peILXG3gUR6SCfYhqGd7bUdZcG9R-NpG3WAc-29gJ-BAS5PdRIB2TaNrRuhGx7jj0t9LlXXlrVVOwbUvV3NDe-b8E3"/>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
                    <div class="absolute bottom-0 left-0 w-full p-4 transform translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300 pointer-events-none">
                        <p class="text-xs font-medium text-white/90">Square 1:1</p>
                    </div>
                </div>

                <div class="masonry-item relative w-full aspect-[16/9] rounded-xl overflow-hidden shadow-floating bg-white/50 dark:bg-gray-800/50 backdrop-blur-sm border border-gray-200 dark:border-gray-700 group opacity-0 animate-reveal-fade animate-success-flash reveal-delay-3 cursor-pointer">
                    <img onclick="openAssetDetail(this.src)" alt="Cinematic obsidian building" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBMbFP54OkePxxiyR89odXu1KverWJTEfXFuGy1OduAQns-Nf1CfCul2f4SuSDIKbsqq4HXMFd3pFpShn1F6u-nmf14ClWZlhNpAtnYsG3hmMKQln0mxulIxeF8DXsy53Vh9eXJc-zD9kuHK5vdG3kXcYA4QJ1RoT3HGSTTaPjWc9UnK3souRNjxHQIMaFpH8wLD1RAbBNktv5i7mCfePS1FgBppiR7RmfGZB3HlHunRehix9hfgpSqmdI3Xw0EHPW3HxQ0xbrj7PU7"/>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
                    <div class="absolute bottom-0 left-0 w-full p-4 transform translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300 pointer-events-none">
                        <p class="text-xs font-medium text-white/90">Cinematic 16:9</p>
                    </div>
                </div>

                <div class="masonry-item relative w-full aspect-[3/4] rounded-xl overflow-hidden shadow-floating bg-white/50 dark:bg-gray-800/50 backdrop-blur-sm border border-gray-200 dark:border-gray-700 group opacity-0 animate-reveal-fade animate-success-flash reveal-delay-4 cursor-pointer">
                    <img onclick="openAssetDetail(this.src)" alt="Abstract digital art" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDhuGajJtnXR1sorOl6O549zjHT_8aMphzK-NSigaX5SlHpZEIF6yXl9BOv1CE7f9XrqiPNSqu5hrl04IK9UeN9D3vkdwSsrNvp-URHL3MgPuNZB9-XjrPkeslL034y8G5r6yeTUK5fMx2IFE8qSVY6XRu2Wy5WYuGR2SwEOokLdWONxbfk_YXmaqRmqVF0WGeqZRQ22geyasbY7UdkiNgeuRjK_wBR14aoEVy6-rANke-WrM07Jq0nB-4S6gVu0Ez3kCBu8uZa_1QQ"/>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
                    <div class="absolute bottom-0 left-0 w-full p-4 transform translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300 pointer-events-none">
                        <p class="text-xs font-medium text-white/90">Vertical 3:4</p>
                    </div>
                </div>

                <div class="masonry-item relative w-full aspect-square rounded-xl overflow-hidden shadow-floating bg-white/50 dark:bg-gray-800/50 backdrop-blur-sm border border-gray-200 dark:border-gray-700 group opacity-0 animate-reveal-fade animate-success-flash reveal-delay-5 cursor-pointer">
                    <img onclick="openAssetDetail(this.src)" alt="Neon city reflection" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDacAJ-yhHGgISLQJxTkny7rtBqoJtNIPHYkP4Kg1or6xl4E6I3q2mfpOE3y58emF5xdVEM5fjR5u3-F4PZB-7zxifGjarFF7h2eTIZx45sguRV_07VV8LNxT5BsFJms4BUXbXaGUeGETmFSmQZeztGhgGacuyyP2V_L3Rh5thBRH7pYqy_cA_JBjdHoJbxyBMyCQm2_xAhnZaDA9PQQJ0MlRkMOYYQZoX5rk4kg1vZcbUXrJCGmG7QDCwCiwXC7Dgj7doDQ-W-KCOA"/>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
                    <div class="absolute bottom-0 left-0 w-full p-4 transform translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300 pointer-events-none">
                        <p class="text-xs font-medium text-white/90">Square 1:1</p>
                    </div>
                </div>

                <div class="masonry-item relative w-full aspect-[2/3] rounded-xl overflow-hidden shadow-floating bg-white/50 dark:bg-gray-800/50 backdrop-blur-sm border border-gray-200 dark:border-gray-700 group opacity-0 animate-reveal-fade animate-success-flash reveal-delay-6 cursor-pointer">
                    <img onclick="openAssetDetail(this.src)" alt="Futuristic fashion portrait" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC4diuvTX4OOq3A6E7kZXBMbbVv8NfCUV66Bl4B2BZJGJ4zhzwbxdEYTlJyz83mwWieXmhQY3Tgw0V_t_yInYdve5w-Uf8QqFXq-2eiKxAIJKPCynLK493Z33o6gIYLlBn8h05Fc3RAX7yjgpOyjDnYO4zJOcFbcOLemKrg3u95nu2AbUIrYu5QCZOdO66Bjx1wpXHWxWzD436_J5gSmNakUIrOrlpiq6gWAzGKoPhCW2VHyHKoNuDjZhfM3sbqUVPNyrN-yudEdztN"/>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
                    <div class="absolute bottom-0 left-0 w-full p-4 transform translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300 pointer-events-none">
                        <p class="text-xs font-medium text-white/90">Portrait 2:3</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="absolute bottom-10 left-1/2 -translate-x-1/2 w-full max-w-2xl px-4 z-30">
            <div class="bg-white/90 dark:bg-gray-800/90 backdrop-blur-2xl border border-gray-200 dark:border-gray-700 rounded-full p-2 pr-2.5 shadow-floating flex items-center gap-2 focus-within:ring-2 focus-within:ring-primary/20 transition-all border border-white dark:border-gray-700">
                <div class="flex items-center gap-2 px-4 py-3 bg-primary/10 rounded-2xl border border-primary/20">
                    <span class="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
                    <span class="text-[10px] font-black text-primary uppercase tracking-widest">Modifying</span>
                </div>
                <input class="flex-1 bg-transparent border-none focus:ring-0 text-text-main-light dark:text-text-main-dark placeholder-gray-400 text-sm py-2 px-2" placeholder="Describe your creation..." type="text" value="A futuristic city with iridescent oil slick texture on obsidian buildings...">
                <div class="flex items-center gap-2">
                    <button class="bg-primary hover:bg-[#5558e3] text-white font-bold rounded-2xl px-5 py-3 transition-all flex items-center gap-2 group shadow-lg shadow-primary/30">
                        <span class="">Regenerate</span>
                        <span class="material-symbols-outlined text-[18px]">auto_fix_high</span>
                    </button>
                </div>
            </div>
        </div>
    </div>
</main>
</div>
"""

content = content.replace('<!-- Configuration Modal Overlay -->', results_view + '\n<!-- Configuration Modal Overlay -->')

# Change "Ignite" button in 'gen' view to switch to 'results' view
content = content.replace(
    '<button class="bg-[#6366F1] hover:bg-[#5558e3] text-white font-medium rounded-full px-6 py-3 transition-colors flex items-center gap-2 group">',
    '<button onclick="switchView(\'results\')" class="bg-[#6366F1] hover:bg-[#5558e3] text-white font-medium rounded-full px-6 py-3 transition-colors flex items-center gap-2 group">'
)

# Update switchView JS to handle 'results'
old_js = "const views = ['gen', 'video', 'plaza', 'api', 'vault'];"
new_js = "const views = ['gen', 'video', 'plaza', 'api', 'vault', 'results'];"
content = content.replace(old_js, new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

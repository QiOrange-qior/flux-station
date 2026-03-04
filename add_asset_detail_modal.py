import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add styles for Asset Detail
styles = """
        /* Screen 4 Modal Styles */
        .iris-border {
            position: relative;
        }
        .iris-border::before {
            content: '';
            position: absolute;
            inset: -2px;
            border-radius: inherit;
            padding: 2px;
            background: linear-gradient(45deg, #6366F1, #A855F7);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
            opacity: 0.6;
        }
        .shadow-glass-light {
            box-shadow: 0 8px 32px 0 rgba(99, 102, 241, 0.1);
        }
        .shadow-glow-iris {
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.2), 0 0 40px rgba(168, 85, 247, 0.1);
        }
"""
content = content.replace('</style>', styles + '\n</style>')

asset_modal = """
<!-- Asset Detail Modal -->
<div id="asset-detail-modal" class="fixed inset-0 z-[110] hidden flex items-center justify-center bg-white/80 dark:bg-black/80 backdrop-blur-xl transition-opacity">
    <button id="close-asset-btn" class="absolute top-8 right-8 z-50 p-3 rounded-full bg-white/50 dark:bg-black/50 hover:bg-white dark:hover:bg-gray-800 text-gray-800 dark:text-gray-200 shadow-sm border border-gray-100 dark:border-gray-800 backdrop-blur-sm transition-all duration-300 group">
        <span class="material-symbols-outlined text-3xl group-hover:rotate-90 transition-transform duration-300 text-primary">close</span>
    </button>
    <button class="absolute left-8 top-1/2 -translate-y-1/2 p-4 rounded-full bg-white/40 dark:bg-black/40 hover:bg-white dark:hover:bg-gray-800 text-gray-600 dark:text-gray-400 hover:text-primary border border-white/50 dark:border-gray-800 shadow-sm backdrop-blur-sm transition-all duration-300 z-40">
        <span class="material-symbols-outlined text-4xl">chevron_left</span>
    </button>
    <button class="absolute right-[400px] top-1/2 -translate-y-1/2 p-4 rounded-full bg-white/40 dark:bg-black/40 hover:bg-white dark:hover:bg-gray-800 text-gray-600 dark:text-gray-400 hover:text-primary border border-white/50 dark:border-gray-800 shadow-sm backdrop-blur-sm transition-all duration-300 z-40 hidden lg:block">
        <span class="material-symbols-outlined text-4xl">chevron_right</span>
    </button>

    <div class="w-full h-full flex flex-row">
        <!-- Image Area -->
        <div class="flex-1 h-full flex flex-col items-center justify-center relative p-12">
            <div class="relative group max-w-4xl w-full aspect-[4/3] flex items-center justify-center">
                <div class="absolute inset-8 bg-primary/10 rounded-3xl blur-3xl transform group-hover:scale-105 transition-transform duration-700"></div>
                <div class="relative w-full h-full rounded-2xl overflow-hidden shadow-2xl bg-white dark:bg-gray-900 iris-border shadow-glow-iris">
                    <img id="detail-main-img" alt="Generated Output" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform ease-out duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAjDTJ_TDCOqlVAOFTjJ1PTZhF48F8a0oW0-A2yoWUCJEY5cHOr0ag8UuyP6l_ajopHOkRhplhxSoJ-oBv-scj5xTW57reVwjQZAhoBprTK_g-m0uO-9pzSSw3H0Wtw45PqhS8kSCxtMZsGjQo21wY8b2b1r1Qi8NmBmopBpI5Fm-Z6noTiHsjeaQFC3eVX-Y-5aGYxsPwGS0cipQrEjETV-3XRvHgJ8NjmVHkKtKmtvqkV7cisLA48vAh_hP4MxHrg93OPDw8e0uTj">
                </div>
            </div>

            <div class="absolute bottom-10 z-50">
                <div class="flex items-center gap-2 p-2 bg-white/70 dark:bg-gray-800/70 backdrop-blur-xl border border-white/60 dark:border-gray-700 rounded-full shadow-floating transform translate-y-0 transition-transform duration-300 ring-1 ring-black/5 dark:ring-white/5">
                    <button class="flex items-center gap-2 px-5 py-2.5 rounded-full text-sm font-medium text-gray-700 dark:text-gray-200 hover:bg-white/50 dark:hover:bg-gray-700 hover:text-primary transition-colors">
                        <span class="material-symbols-outlined text-[18px]">download</span>
                        Download
                    </button>
                    <div class="w-px h-4 bg-gray-300/50 dark:bg-gray-600"></div>
                    <button class="flex items-center gap-2 px-5 py-2.5 rounded-full text-sm font-medium text-gray-700 dark:text-gray-200 hover:bg-white/50 dark:hover:bg-gray-700 hover:text-primary transition-colors">
                        <span class="material-symbols-outlined text-[18px]">content_copy</span>
                        Copy Prompt
                    </button>
                    <button class="flex items-center gap-2 px-6 py-2.5 rounded-full text-sm font-semibold text-white bg-primary hover:bg-[#4F46E5] transition-colors shadow-lg shadow-primary/20 ml-2">
                        <span class="material-symbols-outlined text-[18px]">auto_fix_high</span>
                        Remix
                    </button>
                </div>
            </div>
        </div>

        <!-- Sidebar Info -->
        <div class="w-96 h-full bg-white/80 dark:bg-gray-900/80 backdrop-blur-2xl border-l border-white/60 dark:border-gray-800 flex flex-col z-50 shadow-glass-light relative hidden lg:flex">
            <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-primary via-purple-400 to-pink-400 opacity-80"></div>
            <div class="p-8 flex-1 overflow-y-auto custom-scrollbar">
                <div class="flex items-center justify-between mb-8">
                    <h3 class="font-serif text-3xl text-gray-900 dark:text-white tracking-wide">Asset Details</h3>
                    <div class="flex gap-2">
                        <button class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 text-gray-400 hover:text-primary transition-colors">
                            <span class="material-symbols-outlined text-[20px]">share</span>
                        </button>
                        <button class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 text-gray-400 hover:text-pink-500 transition-colors">
                            <span class="material-symbols-outlined text-[20px]">favorite</span>
                        </button>
                    </div>
                </div>

                <div class="mb-8">
                    <label class="text-xs uppercase tracking-widest text-primary/80 dark:text-primary font-semibold mb-3 block">Prompt</label>
                    <p class="text-gray-700 dark:text-gray-300 text-sm leading-relaxed font-normal border-l-2 border-primary/30 pl-4 bg-gray-50/50 dark:bg-gray-800/50 py-2 rounded-r-lg">
                        "Ethereal abstract smoke, voluminous swirls of vibrant iris violet and deep magenta, soft volumetric lighting, cinematic atmosphere, obsidian background, iridescent oil slick textures, 8k resolution, photorealistic render."
                    </p>
                </div>

                <div class="grid grid-cols-2 gap-y-6 gap-x-4 mb-8">
                    <div>
                        <label class="text-xs uppercase tracking-widest text-gray-400 font-semibold mb-1 block">Model</label>
                        <div class="flex items-center gap-2 text-gray-800 dark:text-gray-200">
                            <span class="material-symbols-outlined text-[18px] text-primary">tune</span>
                            <span class="text-sm font-medium">FLUX 1.1</span>
                        </div>
                    </div>
                    <div>
                        <label class="text-xs uppercase tracking-widest text-gray-400 font-semibold mb-1 block">Resolution</label>
                        <div class="flex items-center gap-2 text-gray-800 dark:text-gray-200">
                            <span class="material-symbols-outlined text-[18px] text-primary">aspect_ratio</span>
                            <span class="text-sm font-medium">2048 x 1536</span>
                        </div>
                    </div>
                </div>

                <div class="mb-8">
                    <label class="text-xs uppercase tracking-widest text-gray-400 font-semibold mb-2 block">Negative Prompt</label>
                    <p class="text-gray-500 text-xs leading-relaxed italic bg-gray-50/50 dark:bg-gray-800/50 p-3 rounded-lg border border-gray-100 dark:border-gray-700">
                        blur, distortion, low quality, pixelated, watermark, text, signature, bad anatomy
                    </p>
                </div>

                <div class="pt-6 border-t border-gray-100 dark:border-gray-800">
                    <div class="flex items-center justify-between text-xs text-gray-400 font-medium">
                        <span>Created just now</span>
                    </div>
                </div>
            </div>

            <div class="p-6 border-t border-gray-100 dark:border-gray-800 bg-white/40 dark:bg-gray-900/40">
                <button class="w-full py-3 rounded-xl border border-primary/20 bg-primary/5 hover:bg-primary/10 text-primary font-semibold text-sm transition-all flex items-center justify-center gap-2 group">
                    <span class="material-symbols-outlined text-[18px] group-hover:-rotate-12 transition-transform">history_edu</span>
                    View Evolution History
                </button>
            </div>
        </div>
    </div>
</div>
"""

content = content.replace('<!-- Configuration Modal Overlay -->', asset_modal + '\n<!-- Configuration Modal Overlay -->')

# Let's attach this modal to the generated image in the generation view
content = content.replace(
    '<button class="group relative w-48 h-56 rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2 dark:focus:ring-offset-gray-900">\n<img alt="Abstract colorful smoke"',
    '<button onclick="openAssetDetail(\'https://lh3.googleusercontent.com/aida-public/AB6AXuAjDTJ_TDCOqlVAOFTjJ1PTZhF48F8a0oW0-A2yoWUCJEY5cHOr0ag8UuyP6l_ajopHOkRhplhxSoJ-oBv-scj5xTW57reVwjQZAhoBprTK_g-m0uO-9pzSSw3H0Wtw45PqhS8kSCxtMZsGjQo21wY8b2b1r1Qi8NmBmopBpI5Fm-Z6noTiHsjeaQFC3eVX-Y-5aGYxsPwGS0cipQrEjETV-3XRvHgJ8NjmVHkKtKmtvqkV7cisLA48vAh_hP4MxHrg93OPDw8e0uTj\')" class="group relative w-48 h-56 rounded-3xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2 dark:focus:ring-offset-gray-900">\n<img alt="Abstract colorful smoke"'
)

# And attach it to the images in Model Plaza too, so there's interactivity
content = content.replace(
    '<img alt="Gemini 3 Pro Image"',
    '<img onclick="openAssetDetail(this.src)" alt="Gemini 3 Pro Image"'
)
content = content.replace(
    '<img alt="Gemini 3.1 Flash"',
    '<img onclick="openAssetDetail(this.src)" alt="Gemini 3.1 Flash"'
)
content = content.replace(
    '<img alt="Seedream 5.0"',
    '<img onclick="openAssetDetail(this.src)" alt="Seedream 5.0"'
)
content = content.replace(
    '<img alt="Seedream 4.5"',
    '<img onclick="openAssetDetail(this.src)" alt="Seedream 4.5"'
)
content = content.replace(
    '<img alt="Imagen 3"',
    '<img onclick="openAssetDetail(this.src)" alt="Imagen 3"'
)

js_logic = """
<script>
    function openAssetDetail(imgSrc) {
        const modal = document.getElementById('asset-detail-modal');
        const mainImg = document.getElementById('detail-main-img');
        if (modal && mainImg) {
            mainImg.src = imgSrc;
            modal.classList.remove('hidden');
        }
    }

    document.addEventListener('DOMContentLoaded', () => {
        const closeAssetBtn = document.getElementById('close-asset-btn');
        const assetModal = document.getElementById('asset-detail-modal');
        if (closeAssetBtn && assetModal) {
            closeAssetBtn.addEventListener('click', () => {
                assetModal.classList.add('hidden');
            });
        }
    });
</script>
"""

content = content.replace('</body>', js_logic + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

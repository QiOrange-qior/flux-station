import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

config_modal = """
<!-- Configuration Modal Overlay -->
<div id="config-modal" class="fixed inset-0 z-[100] hidden items-center justify-center p-4 bg-black/5 backdrop-blur-[2px]">
    <div class="glass-panel w-full max-w-5xl rounded-[32px] flex flex-col shadow-floating relative overflow-hidden max-h-[90vh]">
        <div class="px-10 py-8 flex items-center justify-between shrink-0 relative z-20">
            <div>
                <h2 class="font-serif text-4xl text-iris-gradient tracking-tight">Configuration</h2>
                <p class="text-xs text-gray-500 mt-1 font-medium tracking-wide uppercase">Generation Settings</p>
            </div>
            <button id="close-config-btn" class="w-12 h-12 flex items-center justify-center rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors group">
                <span class="material-symbols-outlined text-3xl font-light text-gray-400 group-hover:text-gray-800 dark:group-hover:text-gray-200 transition-colors">close</span>
            </button>
        </div>
        <div class="flex-1 overflow-y-auto px-10 pb-10 custom-scrollbar">
            <div class="grid grid-cols-12 gap-12">
                <!-- Left Column -->
                <div class="col-span-12 lg:col-span-5 space-y-8">
                    <div>
                        <label class="block text-[11px] font-bold tracking-widest text-gray-400 uppercase mb-3 ml-1">AI Model</label>
                        <div class="relative">
                            <button id="model-select-btn" class="w-full text-left bg-white/60 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700 rounded-2xl px-5 py-4 flex items-center justify-between hover:border-primary/50 transition-all shadow-sm">
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-primary to-[#A855F7] flex items-center justify-center text-white shadow-md shadow-primary/20">
                                        <span class="material-symbols-outlined text-lg">stars</span>
                                    </div>
                                    <div>
                                        <span id="selected-model-name" class="text-gray-900 dark:text-white font-semibold block">Gemini 3.1 Flash Image</span>
                                        <span id="selected-model-desc" class="text-[10px] text-gray-500 uppercase tracking-wide">ZENMUX</span>
                                    </div>
                                </div>
                                <span class="material-symbols-outlined text-gray-400">expand_more</span>
                            </button>
                            <div id="model-dropdown" class="absolute top-full left-0 right-0 mt-2 bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 rounded-2xl shadow-floating z-50 hidden overflow-hidden">
                                <ul id="model-list" class="max-h-60 overflow-y-auto p-2">
                                    <!-- Populated by JS -->
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div>
                        <label class="block text-[11px] font-bold tracking-widest text-gray-400 uppercase mb-3 ml-1">Platform / Provider</label>
                        <div id="platform-selector" class="segmented-control p-1.5 bg-gray-100/80 dark:bg-gray-800/80 rounded-2xl border border-gray-200/50 dark:border-gray-700/50">
                            <div class="segmented-option selected" data-platform="zenmux">ZenMux</div>
                            <div class="segmented-option" data-platform="nebula">Nebula</div>
                            <div class="segmented-option" data-platform="huoshan">火山</div>
                        </div>
                    </div>
                    <div>
                        <label class="block text-[11px] font-bold tracking-widest text-gray-400 uppercase mb-3 ml-1">Generation Mode</label>
                        <div class="segmented-control master-switch p-1.5 bg-gray-100/80 dark:bg-gray-800/80 rounded-2xl border border-gray-200/50 dark:border-gray-700/50">
                            <div class="segmented-option selected" onclick="toggleMode('txt2img')">Text → Img</div>
                            <div class="segmented-option" onclick="toggleMode('img2img')">Img → Img</div>
                        </div>
                        <p class="text-[10px] text-gray-400 mt-2 ml-2 italic">Select mode to reveal specific options</p>
                    </div>
                    <div id="reference-section" class="">
                        <label class="block text-[11px] font-bold tracking-widest text-gray-400 uppercase mb-3 ml-1">Reference Imagery</label>
                        <div class="dashed-upload w-full h-32 rounded-2xl flex flex-col items-center justify-center cursor-pointer hover:bg-primary/5 transition-colors group">
                            <div class="w-10 h-10 rounded-full bg-white shadow-sm flex items-center justify-center mb-2 group-hover:scale-110 transition-transform">
                                <span class="material-symbols-outlined text-primary text-xl">add_photo_alternate</span>
                            </div>
                            <p class="text-xs font-medium text-gray-600 dark:text-gray-300">Upload Reference Image</p>
                            <p class="text-[10px] text-gray-400 mt-1">JPG, PNG, WEBP up to 5MB</p>
                        </div>
                    </div>
                </div>

                <!-- Right Column -->
                <div class="col-span-12 lg:col-span-7 space-y-8 pl-0 lg:pl-4 border-l border-gray-100 dark:border-gray-800/50">
                    <div>
                        <div class="flex justify-between items-center mb-4">
                            <label class="block text-[11px] font-bold tracking-widest text-gray-400 uppercase ml-1">Aspect Ratio</label>
                            <div class="bg-indigo-50 dark:bg-indigo-900/30 rounded-full px-3 py-1 text-[10px] font-bold text-indigo-600 dark:text-indigo-300 tracking-wide border border-indigo-100 dark:border-indigo-800">2K 1664x2080</div>
                        </div>
                        <div class="grid grid-cols-5 gap-3">
                            <button class="ratio-btn bg-white/50">1:1</button>
                            <button class="ratio-btn bg-white/50">3:2</button>
                            <button class="ratio-btn bg-white/50">2:3</button>
                            <button class="ratio-btn bg-white/50">3:4</button>
                            <button class="ratio-btn bg-white/50">4:3</button>
                            <button class="ratio-btn selected">4:5</button>
                            <button class="ratio-btn bg-white/50">5:4</button>
                            <button class="ratio-btn bg-white/50">9:16</button>
                            <button class="ratio-btn bg-white/50">16:9</button>
                            <button class="ratio-btn bg-white/50">21:9</button>
                        </div>
                    </div>
                    <div>
                        <label class="block text-[11px] font-bold tracking-widest text-gray-400 uppercase mb-4 ml-1">Aesthetic Blueprint</label>
                        <div class="grid grid-cols-3 gap-3">
                            <div class="aesthetic-card bg-gradient-cinematic cursor-pointer">Cinematic</div>
                            <div class="aesthetic-card bg-gradient-ethereal cursor-pointer">Ethereal</div>
                            <div class="aesthetic-card bg-gradient-fluid cursor-pointer">Fluid 3D</div>
                            <div class="aesthetic-card bg-gradient-minimal cursor-pointer">Minimal</div>
                            <div class="aesthetic-card bg-gradient-fantasy cursor-pointer">Fantasy</div>
                            <div class="aesthetic-card bg-gradient-cyber cursor-pointer">Cyberpunk</div>
                            <div class="aesthetic-card bg-no-style cursor-pointer selected">
                                <span class="material-symbols-outlined text-[20px] mb-1 opacity-60">block</span>
                                <span>No Style</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="h-1.5 w-full bg-gradient-to-r from-primary to-[#A855F7] absolute bottom-0 left-0"></div>
    </div>
</div>
"""

content = content.replace('<!-- Configuration Modal Overlay -->', config_modal)

# Update gen view button to open modal
content = content.replace(
    '<button class="flex items-center gap-1.5 px-4 py-3 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors text-sm font-bold text-text-main-light dark:text-text-main-dark">\n<span class="material-symbols-outlined text-[18px] text-gray-500 dark:text-gray-400">tune</span>\n<span>FLUX 1.1</span>\n<span class="material-symbols-outlined text-[14px] text-gray-400">arrow_drop_down</span>\n</button>',
    '<button id="open-config-btn" class="flex items-center gap-1.5 px-4 py-3 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors text-sm font-bold text-text-main-light dark:text-text-main-dark">\n<span class="material-symbols-outlined text-[18px] text-gray-500 dark:text-gray-400">tune</span>\n<span>FLUX 1.1</span>\n<span class="material-symbols-outlined text-[14px] text-gray-400">arrow_drop_down</span>\n</button>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

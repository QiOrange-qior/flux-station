import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the content inside id="models-grid"
start_str = '<div class="masonry-grid-models" id="models-grid">'
end_str = '</div></div></div></main>'

new_cards = """
<div class="masonry-grid-models" id="models-grid">
    <!-- Card 1: Gemini 3 Pro -->
    <div class="masonry-item-models mb-6 group relative rounded-3xl overflow-hidden shadow-sm hover:shadow-2xl hover:shadow-primary/20 transition-all duration-500 hover:-translate-y-1 bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 opacity-0 animate-[floatIn_0.6s_ease-out_forwards]" style="animation-delay: 0.0s;">
        <div class="relative w-full aspect-[3/4] overflow-hidden">
            <img alt="Gemini 3 Pro Image" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDv4xkKxRrWob2cDxas59tYImxsvr706WnvVWMQM1ql1KywOpcN3iNpuhCRVhJQGwkzTyvZ9CcZQPgJZubgR76DaGpulfqV8FiNRYWzGFagWzxP7WguN2LSz0rRpvDPo1HXN_fArch8exoTT-K2Fmnapai9UFgM8-Bd8lQcfrydWh-QwtjDgKb9KWo5PngnXjSJ_HglLoyZnUj_QthOsd6UHTr-s6c4j2QsYeHJpdcLEVwUlqr8U_HXpT19bBStNELTycGirWOHH6JI"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            <div class="absolute top-4 left-4 flex gap-2">
                <span class="px-2.5 py-1 rounded-lg bg-black/50 backdrop-blur-md text-white text-[10px] font-bold tracking-wider uppercase border border-white/20 shadow-sm">风格</span>
            </div>
            <div class="absolute inset-0 flex flex-col justify-end p-5 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300">
                <p class="text-white/90 text-xs mb-2 line-clamp-2">专为专业视觉资产设计，利用高级推理完成复杂指令，支持高保真文字渲染与 4K 输出。</p>
                <button class="w-full bg-white/20 hover:bg-white/40 backdrop-blur-md text-white font-medium rounded-xl py-2.5 transition-colors border border-white/30 flex items-center justify-center gap-2"><span class="material-symbols-outlined text-[18px]">auto_fix_high</span>使用模型</button>
            </div>
        </div>
        <div class="p-4">
            <div class="flex justify-between items-start mb-1">
                <h3 class="font-semibold text-text-main-light dark:text-text-main-dark text-base truncate pr-2">Gemini 3 Pro Image</h3>
            </div>
            <p class="text-xs text-text-muted-light dark:text-text-muted-dark flex items-center gap-1.5 mt-1"><div class="w-4 h-4 rounded-full bg-gradient-to-tr from-primary to-pink-500"></div>@GoogleDeepMind</p>
            <div class="flex items-center justify-between mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
                <div class="flex items-center gap-1 text-[11px] text-gray-500 dark:text-gray-400"><span class="material-symbols-outlined text-[14px]">download</span>124K</div>
                <button class="text-gray-400 hover:text-pink-500 transition-colors"><span class="material-symbols-outlined text-[16px]">favorite_border</span></button>
            </div>
        </div>
    </div>

    <!-- Card 2: Gemini 3.1 Flash -->
    <div class="masonry-item-models mb-6 group relative rounded-3xl overflow-hidden shadow-sm hover:shadow-2xl hover:shadow-primary/20 transition-all duration-500 hover:-translate-y-1 bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 opacity-0 animate-[floatIn_0.6s_ease-out_forwards]" style="animation-delay: 0.1s;">
        <div class="relative w-full aspect-video overflow-hidden">
            <img alt="Gemini 3.1 Flash" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBMbFP54OkePxxiyR89odXu1KverWJTEfXFuGy1OduAQns-Nf1CfCul2f4SuSDIKbsqq4HXMFd3pFpShn1F6u-nmf14ClWZlhNpAtnYsG3hmMKQln0mxulIxeF8DXsy53Vh9eXJc-zD9kuHK5vdG3kXcYA4QJ1RoT3HGSTTaPjWc9UnK3souRNjxHQIMaFpH8wLD1RAbBNktv5i7mCfePS1FgBppiR7RmfGZB3HlHunRehix9hfgpSqmdI3Xw0EHPW3HxQ0xbrj7PU7"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            <div class="absolute top-4 left-4 flex gap-2">
                <span class="px-2.5 py-1 rounded-lg bg-black/50 backdrop-blur-md text-white text-[10px] font-bold tracking-wider uppercase border border-white/20 shadow-sm">场景</span>
            </div>
            <div class="absolute inset-0 flex flex-col justify-end p-5 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300">
                <p class="text-white/90 text-xs mb-2 line-clamp-2">为速度与高并发优化，支持多达 14 张参考图混合输入，并首创 Google 搜索图片接地能力。</p>
                <button class="w-full mt-3 bg-white/20 hover:bg-white/40 backdrop-blur-md text-white font-medium rounded-xl py-2.5 transition-colors border border-white/30 flex items-center justify-center gap-2"><span class="material-symbols-outlined text-[18px]">auto_fix_high</span>使用模型</button>
            </div>
        </div>
        <div class="p-4">
            <div class="flex justify-between items-start mb-1">
                <h3 class="font-semibold text-text-main-light dark:text-text-main-dark text-base truncate pr-2">Gemini 3.1 Flash Image</h3>
            </div>
            <p class="text-xs text-text-muted-light dark:text-text-muted-dark flex items-center gap-1.5 mt-1"><div class="w-4 h-4 rounded-full bg-gradient-to-tr from-primary to-pink-500"></div>@GoogleDeepMind</p>
            <div class="flex items-center justify-between mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
                <div class="flex items-center gap-1 text-[11px] text-gray-500 dark:text-gray-400"><span class="material-symbols-outlined text-[14px]">download</span>312K</div>
                <button class="text-gray-400 hover:text-pink-500 transition-colors"><span class="material-symbols-outlined text-[16px]">favorite_border</span></button>
            </div>
        </div>
    </div>

    <!-- Card 3: Doubao Seedream 5.0 -->
    <div class="masonry-item-models mb-6 group relative rounded-3xl overflow-hidden shadow-sm hover:shadow-2xl hover:shadow-primary/20 transition-all duration-500 hover:-translate-y-1 bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 opacity-0 animate-[floatIn_0.6s_ease-out_forwards]" style="animation-delay: 0.2s;">
        <div class="relative w-full aspect-square overflow-hidden">
            <img alt="Seedream 5.0" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAjDTJ_TDCOqlVAOFTjJ1PTZhF48F8a0oW0-A2yoWUCJEY5cHOr0ag8UuyP6l_ajopHOkRhplhxSoJ-oBv-scj5xTW57reVwjQZAhoBprTK_g-m0uO-9pzSSw3H0Wtw45PqhS8kSCxtMZsGjQo21wY8b2b1r1Qi8NmBmopBpI5Fm-Z6noTiHsjeaQFC3eVX-Y-5aGYxsPwGS0cipQrEjETV-3XRvHgJ8NjmVHkKtKmtvqkV7cisLA48vAh_hP4MxHrg93OPDw8e0uTj"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            <div class="absolute top-4 left-4 flex gap-2">
                <span class="px-2.5 py-1 rounded-lg bg-black/50 backdrop-blur-md text-white text-[10px] font-bold tracking-wider uppercase border border-white/20 shadow-sm">角色</span>
            </div>
            <div class="absolute inset-0 flex flex-col justify-end p-5 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300">
                <p class="text-white/90 text-xs mb-2 line-clamp-2">火山引擎旗舰视觉生成模型，擅长商业摄影、角色一致性控制及高动态范围的艺术创作。</p>
                <button class="w-full mt-3 bg-white/20 hover:bg-white/40 backdrop-blur-md text-white font-medium rounded-xl py-2.5 transition-colors border border-white/30 flex items-center justify-center gap-2"><span class="material-symbols-outlined text-[18px]">auto_fix_high</span>使用模型</button>
            </div>
        </div>
        <div class="p-4">
            <div class="flex justify-between items-start mb-1">
                <h3 class="font-semibold text-text-main-light dark:text-text-main-dark text-base truncate pr-2">豆包·Seedream 5.0</h3>
            </div>
            <p class="text-xs text-text-muted-light dark:text-text-muted-dark flex items-center gap-1.5 mt-1"><div class="w-4 h-4 rounded-full bg-gradient-to-tr from-blue-500 to-indigo-400"></div>@Volcengine</p>
            <div class="flex items-center justify-between mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
                <div class="flex items-center gap-1 text-[11px] text-gray-500 dark:text-gray-400"><span class="material-symbols-outlined text-[14px]">download</span>85K</div>
                <button class="text-gray-400 hover:text-pink-500 transition-colors"><span class="material-symbols-outlined text-[16px]">favorite_border</span></button>
            </div>
        </div>
    </div>

    <!-- Card 4: Doubao Seedream 4.5 -->
    <div class="masonry-item-models mb-6 group relative rounded-3xl overflow-hidden shadow-sm hover:shadow-2xl hover:shadow-primary/20 transition-all duration-500 hover:-translate-y-1 bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 opacity-0 animate-[floatIn_0.6s_ease-out_forwards]" style="animation-delay: 0.3s;">
        <div class="relative w-full aspect-square overflow-hidden">
            <img alt="Seedream 4.5" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCBwlXCdeDU2DlLOBQdLdj5MjQMMR9R1yYJBGv05_VL3_UYGDJbtpPKvbCLp-ALK7e-KQKF4gdzJyDSjlNylsL5vigFFu_IDIkkNulDROGaRJsYJwlKw-stLhfp3YaVLxIhwJiLo1gTkB10W1wWvvz_oUlHVphq1B0XX1QnGzUq2OCUTF6Fn2peILXG3gUR6SCfYhqGd7bUdZcG9R-NpG3WAc-29gJ-BAS5PdRIB2TaNrRuhGx7jj0t9LlXXlrVVOwbUvV3NDe-b8E3"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            <div class="absolute top-4 left-4 flex gap-2">
                <span class="px-2.5 py-1 rounded-lg bg-black/50 backdrop-blur-md text-white text-[10px] font-bold tracking-wider uppercase border border-white/20 shadow-sm">微调</span>
            </div>
            <div class="absolute inset-0 flex flex-col justify-end p-5 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300">
                <p class="text-white/90 text-xs mb-2 line-clamp-2">火山方舟稳定版本，极佳的构图理解能力与二次元风格支持，适用于广泛的泛化场景。</p>
                <button class="w-full mt-3 bg-white/20 hover:bg-white/40 backdrop-blur-md text-white font-medium rounded-xl py-2.5 transition-colors border border-white/30 flex items-center justify-center gap-2"><span class="material-symbols-outlined text-[18px]">auto_fix_high</span>使用模型</button>
            </div>
        </div>
        <div class="p-4">
            <div class="flex justify-between items-start mb-1">
                <h3 class="font-semibold text-text-main-light dark:text-text-main-dark text-base truncate pr-2">豆包·Seedream 4.5</h3>
            </div>
            <p class="text-xs text-text-muted-light dark:text-text-muted-dark flex items-center gap-1.5 mt-1"><div class="w-4 h-4 rounded-full bg-gradient-to-tr from-blue-500 to-indigo-400"></div>@Volcengine</p>
            <div class="flex items-center justify-between mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
                <div class="flex items-center gap-1 text-[11px] text-gray-500 dark:text-gray-400"><span class="material-symbols-outlined text-[14px]">download</span>192K</div>
                <button class="text-gray-400 hover:text-pink-500 transition-colors"><span class="material-symbols-outlined text-[16px]">favorite_border</span></button>
            </div>
        </div>
    </div>

    <!-- Card 5: Imagen 3 -->
    <div class="masonry-item-models mb-6 group relative rounded-3xl overflow-hidden shadow-sm hover:shadow-2xl hover:shadow-primary/20 transition-all duration-500 hover:-translate-y-1 bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 opacity-0 animate-[floatIn_0.6s_ease-out_forwards]" style="animation-delay: 0.4s;">
        <div class="relative w-full aspect-[2/3] overflow-hidden">
            <img alt="Imagen 3" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC4diuvTX4OOq3A6E7kZXBMbbVv8NfCUV66Bl4B2BZJGJ4zhzwbxdEYTlJyz83mwWieXmhQY3Tgw0V_t_yInYdve5w-Uf8QqFXq-2eiKxAIJKPCynLK493Z33o6gIYLlBn8h05Fc3RAX7yjgpOyjDnYO4zJOcFbcOLemKrg3u95nu2AbUIrYu5QCZOdO66Bjx1wpXHWxWzD436_J5gSmNakUIrOrlpiq6gWAzGKoPhCW2VHyHKoNuDjZhfM3sbqUVPNyrN-yudEdztN"/>
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            <div class="absolute top-4 left-4 flex gap-2">
                <span class="px-2.5 py-1 rounded-lg bg-black/50 backdrop-blur-md text-white text-[10px] font-bold tracking-wider uppercase border border-white/20 shadow-sm">角色</span>
            </div>
            <div class="absolute inset-0 flex flex-col justify-end p-5 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-300">
                <p class="text-white/90 text-xs mb-2 line-clamp-2">Google 的专业图像生成模型，具备无与伦比的照片级真实感及细节控制能力。</p>
                <button class="w-full mt-3 bg-white/20 hover:bg-white/40 backdrop-blur-md text-white font-medium rounded-xl py-2.5 transition-colors border border-white/30 flex items-center justify-center gap-2"><span class="material-symbols-outlined text-[18px]">auto_fix_high</span>使用模型</button>
            </div>
        </div>
        <div class="p-4">
            <div class="flex justify-between items-start mb-1">
                <h3 class="font-semibold text-text-main-light dark:text-text-main-dark text-base truncate pr-2">Imagen 3</h3>
            </div>
            <p class="text-xs text-text-muted-light dark:text-text-muted-dark flex items-center gap-1.5 mt-1"><div class="w-4 h-4 rounded-full bg-gradient-to-tr from-primary to-pink-500"></div>@Google</p>
            <div class="flex items-center justify-between mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
                <div class="flex items-center gap-1 text-[11px] text-gray-500 dark:text-gray-400"><span class="material-symbols-outlined text-[14px]">download</span>2M+</div>
                <button class="text-gray-400 hover:text-pink-500 transition-colors"><span class="material-symbols-outlined text-[16px]">favorite_border</span></button>
            </div>
        </div>
    </div>
"""

start_index = content.find(start_str)
end_index = content.find(end_str)

if start_index != -1 and end_index != -1:
    updated_content = content[:start_index] + new_cards + content[end_index:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("Content updated successfully.")
else:
    print("Could not find the target section.")

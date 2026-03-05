import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate API view block
start_str = '<!-- API VIEW -->'
end_str = '<!-- VAULT VIEW -->'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

new_api_view = """
<!-- API VIEW -->
<div id="api-view" class="flex-1 flex w-full h-full hidden">
<main class="flex-1 relative flex flex-col h-full overflow-hidden bg-[#F9F9FB] dark:bg-[#09090b] transition-colors">
    <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <div class="absolute bottom-0 left-0 w-[600px] h-[600px] bg-emerald-100/40 dark:bg-emerald-900/10 rounded-full blur-[120px] translate-y-1/3 -translate-x-1/3"></div>
    </div>

    <div class="flex-1 z-10 flex flex-col p-10 overflow-y-auto custom-scrollbar w-full">
        <div class="flex justify-between items-end mb-10 max-w-5xl">
            <div>
                <h2 class="font-serif text-5xl mb-3 text-text-main-light dark:text-text-main-dark">模型配置</h2>
                <p class="text-text-muted-light dark:text-text-muted-dark text-lg font-light">配置您的模型供应商 API 密钥，以便在工作流中调用不同模型。</p>
            </div>
        </div>

        <!-- Provider Configuration -->
        <div class="space-y-6 max-w-5xl">
            <h3 class="text-xl font-semibold text-text-main-light dark:text-text-main-dark mb-4">供应商配置</h3>

            <!-- Google Card -->
            <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-3xl p-6 shadow-sm transition-all hover:shadow-md">
                <div class="flex flex-col lg:flex-row gap-6">
                    <!-- Left: Info -->
                    <div class="flex-1">
                        <div class="flex items-center gap-3 mb-2">
                            <div class="w-10 h-10 rounded-xl bg-gray-100 dark:bg-gray-700 flex items-center justify-center text-primary shrink-0">
                                <svg viewBox="0 0 24 24" width="24" height="24" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
                                    <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                                    <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
                                    <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
                                </svg>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-text-main-light dark:text-text-main-dark flex items-center gap-2">
                                    Google
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300">
                                        未配置
                                    </span>
                                </h4>
                                <p class="text-xs text-text-muted-light dark:text-text-muted-dark mt-0.5">Google 官方提供的 Gemini 视觉大模型。</p>
                            </div>
                        </div>

                        <div class="mt-4 pl-[52px]">
                            <p class="text-xs font-semibold text-gray-500 dark:text-gray-400 mb-2 uppercase tracking-wider">支持的模型</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono">
                                    gemini-3-pro-image-preview
                                </span>
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono">
                                    gemini-3.1-flash-image-preview
                                </span>
                            </div>
                        </div>
                    </div>

                    <!-- Right: API Key Input -->
                    <div class="lg:w-1/3 flex flex-col justify-center border-t lg:border-t-0 lg:border-l border-gray-100 dark:border-gray-700 pt-4 lg:pt-0 lg:pl-6">
                        <label class="block text-xs font-semibold text-gray-500 dark:text-gray-400 mb-2 uppercase tracking-wider">API 密钥</label>
                        <div class="space-y-3">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span>尚未配置密钥</span>
                            </div>
                            <button class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2 group">
                                <span class="material-symbols-outlined text-[18px]">add</span>
                                添加密钥
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Nebula Card -->
            <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-3xl p-6 shadow-sm transition-all hover:shadow-md">
                <div class="flex flex-col lg:flex-row gap-6">
                    <!-- Left: Info -->
                    <div class="flex-1">
                        <div class="flex items-center gap-3 mb-2">
                            <div class="w-10 h-10 rounded-xl bg-indigo-50 dark:bg-gray-700 flex items-center justify-center text-primary shrink-0">
                                <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-indigo-500">
                                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z" />
                                    <path d="M3.3 7l8.7 5 8.7-5" />
                                    <path d="M12 22V12" />
                                </svg>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-text-main-light dark:text-text-main-dark flex items-center gap-2">
                                    Nebula
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400">
                                        已连接
                                    </span>
                                </h4>
                                <p class="text-xs text-text-muted-light dark:text-text-muted-dark mt-0.5">提供 Gemini 和 Doubao 系列的高性能图像生成模型。</p>
                            </div>
                        </div>

                        <div class="mt-4 pl-[52px]">
                            <p class="text-xs font-semibold text-gray-500 dark:text-gray-400 mb-2 uppercase tracking-wider">支持的模型</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono">gemini-3-pro-image-preview</span>
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono">gemini-3.1-flash-image-preview</span>
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono">doubao-seedream-4-5-251128</span>
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono mt-1 lg:mt-0">doubao-seedream-4-0-250828</span>
                            </div>
                        </div>
                    </div>

                    <!-- Right: API Key Input -->
                    <div class="lg:w-1/3 flex flex-col justify-center border-t lg:border-t-0 lg:border-l border-gray-100 dark:border-gray-700 pt-4 lg:pt-0 lg:pl-6">
                        <label class="block text-xs font-semibold text-gray-500 dark:text-gray-400 mb-2 uppercase tracking-wider">API 密钥</label>
                        <div class="space-y-3">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span>••••••••••••••••cdef</span>
                                <span class="material-symbols-outlined text-[16px] text-emerald-500">check_circle</span>
                            </div>
                            <button class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2">
                                <span class="material-symbols-outlined text-[18px]">edit</span>
                                修改密钥
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ZenMux Card -->
            <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-3xl p-6 shadow-sm transition-all hover:shadow-md">
                <div class="flex flex-col lg:flex-row gap-6">
                    <!-- Left: Info -->
                    <div class="flex-1">
                        <div class="flex items-center gap-3 mb-2">
                            <div class="w-10 h-10 rounded-xl bg-cyan-50 dark:bg-gray-700 flex items-center justify-center text-primary shrink-0">
                                <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-cyan-500">
                                    <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
                                </svg>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-text-main-light dark:text-text-main-dark flex items-center gap-2">
                                    ZenMux
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300">
                                        未配置
                                    </span>
                                </h4>
                                <p class="text-xs text-text-muted-light dark:text-text-muted-dark mt-0.5">专注 Google Gemini 图像模型的稳定代理服务。</p>
                            </div>
                        </div>

                        <div class="mt-4 pl-[52px]">
                            <p class="text-xs font-semibold text-gray-500 dark:text-gray-400 mb-2 uppercase tracking-wider">支持的模型</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono">google/gemini-3.1-flash-image-preview</span>
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono">google/gemini-3-pro-image-preview</span>
                            </div>
                        </div>
                    </div>

                    <!-- Right: API Key Input -->
                    <div class="lg:w-1/3 flex flex-col justify-center border-t lg:border-t-0 lg:border-l border-gray-100 dark:border-gray-700 pt-4 lg:pt-0 lg:pl-6">
                        <label class="block text-xs font-semibold text-gray-500 dark:text-gray-400 mb-2 uppercase tracking-wider">API 密钥</label>
                        <div class="space-y-3">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span>尚未配置密钥</span>
                            </div>
                            <button class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2">
                                <span class="material-symbols-outlined text-[18px]">add</span>
                                添加密钥
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Volcengine Card -->
            <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-3xl p-6 shadow-sm transition-all hover:shadow-md">
                <div class="flex flex-col lg:flex-row gap-6">
                    <!-- Left: Info -->
                    <div class="flex-1">
                        <div class="flex items-center gap-3 mb-2">
                            <div class="w-10 h-10 rounded-xl bg-blue-50 dark:bg-gray-700 flex items-center justify-center text-primary shrink-0">
                                <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-[#1A55FF]">
                                    <path d="M12 3L2 20h20L12 3z" />
                                    <path d="M12 11l-3 6h6l-3-6z" fill="currentColor" />
                                </svg>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-text-main-light dark:text-text-main-dark flex items-center gap-2">
                                    火山引擎 (Volcengine)
                                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300">
                                        未配置
                                    </span>
                                </h4>
                                <p class="text-xs text-text-muted-light dark:text-text-muted-dark mt-0.5">字节跳动旗下的云服务，提供最新版 Doubao 视觉模型。</p>
                            </div>
                        </div>

                        <div class="mt-4 pl-[52px]">
                            <p class="text-xs font-semibold text-gray-500 dark:text-gray-400 mb-2 uppercase tracking-wider">支持的模型</p>
                            <div class="flex flex-wrap gap-2">
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono">doubao-seedream-5-0-260128</span>
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono">doubao-seedream-4-5-251128</span>
                                <span class="text-[11px] px-2.5 py-1 rounded-lg bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-mono">doubao-seedream-4-0-250828</span>
                            </div>
                        </div>
                    </div>

                    <!-- Right: API Key Input -->
                    <div class="lg:w-1/3 flex flex-col justify-center border-t lg:border-t-0 lg:border-l border-gray-100 dark:border-gray-700 pt-4 lg:pt-0 lg:pl-6">
                        <label class="block text-xs font-semibold text-gray-500 dark:text-gray-400 mb-2 uppercase tracking-wider">API 密钥</label>
                        <div class="space-y-3">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span>尚未配置密钥</span>
                            </div>
                            <button class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2">
                                <span class="material-symbols-outlined text-[18px]">add</span>
                                添加密钥
                            </button>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</main>
</div>
"""

content = content[:start_idx] + new_api_view + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

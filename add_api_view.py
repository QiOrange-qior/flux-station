import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

api_view_content = """
<div id="api-view" class="flex-1 flex w-full h-full hidden">
<main class="flex-1 relative flex flex-col h-full overflow-hidden bg-[#0F111A] transition-colors"><div class="absolute inset-0 z-0 pointer-events-none overflow-hidden"><div class="absolute top-1/4 left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-blue-900/10 rounded-full blur-[120px]"></div></div><div class="flex-1 z-10 flex flex-col h-full w-full relative overflow-y-auto overflow-x-hidden p-10 max-w-5xl mx-auto"><h2 class="font-bold text-2xl text-white tracking-tight mb-8">供应商配置</h2>

    <div class="space-y-6">
        <!-- Google Card -->
        <div class="bg-[#242A38] rounded-xl border border-gray-700/50 p-6 flex flex-col md:flex-row gap-6">
            <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                    <div class="w-10 h-10 rounded-full bg-white flex items-center justify-center overflow-hidden shrink-0">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google" class="w-6 h-6 object-contain">
                    </div>
                    <div class="flex items-center gap-2">
                        <h3 class="text-lg font-bold text-white">Google</h3>
                        <span class="px-2 py-0.5 rounded text-[10px] font-medium bg-gray-700 text-gray-300">未配置</span>
                    </div>
                </div>
                <p class="text-sm text-gray-400 mb-4 pl-[52px]">Google 官方提供的 Gemini 视觉大模型。</p>
                <div class="pl-[52px]">
                    <p class="text-xs text-gray-500 mb-2">支持的模型</p>
                    <div class="flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono">gemini-3-pro-image-preview</span>
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono">gemini-3.1-flash-image-preview</span>
                    </div>
                </div>
            </div>
            <div class="w-full md:w-80 shrink-0 border-t md:border-t-0 md:border-l border-gray-700/50 pt-4 md:pt-0 md:pl-6 flex flex-col justify-center">
                <p class="text-xs text-gray-400 mb-2">API 密钥</p>
                <div class="w-full bg-[#1A1F2B] border border-gray-700 rounded-lg px-4 py-2.5 mb-3 text-sm text-gray-500">
                    尚未配置密钥
                </div>
                <button class="w-full py-2.5 rounded-lg border border-gray-600 hover:bg-gray-700/50 transition-colors flex items-center justify-center gap-2 text-sm text-gray-300">
                    <span class="material-symbols-outlined text-[18px]">add</span>
                    添加密钥
                </button>
            </div>
        </div>

        <!-- Nebula Card -->
        <div class="bg-[#242A38] rounded-xl border border-gray-700/50 p-6 flex flex-col md:flex-row gap-6">
            <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                    <div class="w-10 h-10 rounded-xl bg-indigo-500/20 flex items-center justify-center overflow-hidden shrink-0">
                        <span class="material-symbols-outlined text-indigo-400 text-2xl">hexagon</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <h3 class="text-lg font-bold text-white">Nebula</h3>
                        <span class="px-2 py-0.5 rounded text-[10px] font-medium bg-emerald-500/10 text-emerald-400">已连接</span>
                    </div>
                </div>
                <p class="text-sm text-gray-400 mb-4 pl-[52px]">提供 Gemini 和 Doubao 系列的高性能图像生成模型。</p>
                <div class="pl-[52px]">
                    <p class="text-xs text-gray-500 mb-2">支持的模型</p>
                    <div class="flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono">gemini-3-pro-image-preview</span>
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono">gemini-3.1-flash-image-preview</span>
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono">doubao-seedream-4-5-251128</span>
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono mt-1">doubao-seedream-4-0-250828</span>
                    </div>
                </div>
            </div>
            <div class="w-full md:w-80 shrink-0 border-t md:border-t-0 md:border-l border-gray-700/50 pt-4 md:pt-0 md:pl-6 flex flex-col justify-center">
                <p class="text-xs text-gray-400 mb-2">API 密钥</p>
                <div class="w-full bg-[#1A1F2B] border border-gray-700 rounded-lg px-4 py-2.5 mb-3 text-sm text-gray-400 flex items-center justify-between">
                    <span>•••••••••••••••••cdef</span>
                    <span class="material-symbols-outlined text-[18px] text-emerald-500">check_circle</span>
                </div>
                <button class="w-full py-2.5 rounded-lg border border-gray-600 hover:bg-gray-700/50 transition-colors flex items-center justify-center gap-2 text-sm text-gray-300">
                    <span class="material-symbols-outlined text-[18px]">edit</span>
                    修改密钥
                </button>
            </div>
        </div>

        <!-- ZenMux Card -->
        <div class="bg-[#242A38] rounded-xl border border-gray-700/50 p-6 flex flex-col md:flex-row gap-6">
            <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                    <div class="w-10 h-10 rounded-xl bg-teal-500/20 flex items-center justify-center overflow-hidden shrink-0">
                        <span class="material-symbols-outlined text-teal-400 text-2xl">layers</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <h3 class="text-lg font-bold text-white">ZenMux</h3>
                        <span class="px-2 py-0.5 rounded text-[10px] font-medium bg-gray-700 text-gray-300">未配置</span>
                    </div>
                </div>
                <p class="text-sm text-gray-400 mb-4 pl-[52px]">专注 Google Gemini 图像模型的稳定代理服务。</p>
                <div class="pl-[52px]">
                    <p class="text-xs text-gray-500 mb-2">支持的模型</p>
                    <div class="flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono">google/gemini-3.1-flash-image-preview</span>
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono">google/gemini-3-pro-image-preview</span>
                    </div>
                </div>
            </div>
            <div class="w-full md:w-80 shrink-0 border-t md:border-t-0 md:border-l border-gray-700/50 pt-4 md:pt-0 md:pl-6 flex flex-col justify-center">
                <p class="text-xs text-gray-400 mb-2">API 密钥</p>
                <div class="w-full bg-[#1A1F2B] border border-gray-700 rounded-lg px-4 py-2.5 mb-3 text-sm text-gray-500">
                    尚未配置密钥
                </div>
                <button class="w-full py-2.5 rounded-lg border border-gray-600 hover:bg-gray-700/50 transition-colors flex items-center justify-center gap-2 text-sm text-gray-300">
                    <span class="material-symbols-outlined text-[18px]">add</span>
                    添加密钥
                </button>
            </div>
        </div>

        <!-- Volcengine Card -->
        <div class="bg-[#242A38] rounded-xl border border-gray-700/50 p-6 flex flex-col md:flex-row gap-6">
            <div class="flex-1">
                <div class="flex items-center gap-3 mb-2">
                    <div class="w-10 h-10 rounded-xl bg-blue-500/20 flex items-center justify-center overflow-hidden shrink-0">
                        <span class="material-symbols-outlined text-blue-500 text-2xl">change_history</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <h3 class="text-lg font-bold text-white">火山引擎 (Volcengine)</h3>
                        <span class="px-2 py-0.5 rounded text-[10px] font-medium bg-gray-700 text-gray-300">未配置</span>
                    </div>
                </div>
                <p class="text-sm text-gray-400 mb-4 pl-[52px]">字节跳动旗下的云服务，提供最新版 Doubao 视觉模型。</p>
                <div class="pl-[52px]">
                    <p class="text-xs text-gray-500 mb-2">支持的模型</p>
                    <div class="flex flex-wrap gap-2">
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono">doubao-seedream-5-0-260128</span>
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono">doubao-seedream-4-5-251128</span>
                        <span class="px-2.5 py-1 rounded-md border border-gray-700 bg-[#1D222D] text-xs text-gray-300 font-mono">doubao-seedream-4-0-250828</span>
                    </div>
                </div>
            </div>
            <div class="w-full md:w-80 shrink-0 border-t md:border-t-0 md:border-l border-gray-700/50 pt-4 md:pt-0 md:pl-6 flex flex-col justify-center">
                <p class="text-xs text-gray-400 mb-2">API 密钥</p>
                <div class="w-full bg-[#1A1F2B] border border-gray-700 rounded-lg px-4 py-2.5 mb-3 text-sm text-gray-500">
                    尚未配置密钥
                </div>
                <button class="w-full py-2.5 rounded-lg border border-gray-600 hover:bg-gray-700/50 transition-colors flex items-center justify-center gap-2 text-sm text-gray-300">
                    <span class="material-symbols-outlined text-[18px]">add</span>
                    添加密钥
                </button>
            </div>
        </div>

    </div>
</div></main>
</div>
"""

start_str = '<div id="api-view" class="flex-1 flex w-full h-full hidden">'
end_str = '</div>\n\n<div id="vault-view"'
start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + api_view_content + content[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("API Settings view updated")
else:
    print("Could not find API Settings view section")

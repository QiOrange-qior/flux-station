import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# For Google
google_static = """<div class="space-y-3">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span>尚未配置密钥</span>
                            </div>
                            <button class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2 group">
                                <span class="material-symbols-outlined text-[18px]">add</span>
                                添加密钥
                            </button>
                        </div>"""

google_dynamic = """<div class="space-y-3" id="api-display-google">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span id="api-key-text-google">尚未配置密钥</span>
                                <span id="api-key-check-google" class="material-symbols-outlined text-[16px] text-emerald-500 hidden">check_circle</span>
                            </div>
                            <button onclick="toggleApiEdit('google')" class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2 group">
                                <span id="api-btn-icon-google" class="material-symbols-outlined text-[18px]">add</span>
                                <span id="api-btn-text-google">添加密钥</span>
                            </button>
                        </div>
                        <div class="space-y-3 hidden" id="api-edit-google">
                            <input id="api-input-google" type="text" placeholder="输入您的 API Key..." class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-primary/50 focus:border-primary focus:ring-2 focus:ring-primary/20 text-sm text-text-main-light dark:text-text-main-dark outline-none transition-all font-mono" />
                            <div class="flex gap-2">
                                <button onclick="saveApiKey('google')" class="flex-1 bg-primary hover:bg-[#5558e3] text-white text-sm font-medium py-2 rounded-xl transition-colors">
                                    保存
                                </button>
                                <button onclick="cancelApiEdit('google')" class="flex-1 bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-200 text-sm font-medium py-2 rounded-xl transition-colors">
                                    取消
                                </button>
                            </div>
                        </div>"""
content = content.replace(google_static, google_dynamic)

# For Nebula
nebula_static = """<div class="space-y-3">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span>••••••••••••••••cdef</span>
                                <span class="material-symbols-outlined text-[16px] text-emerald-500">check_circle</span>
                            </div>
                            <button class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2">
                                <span class="material-symbols-outlined text-[18px]">edit</span>
                                修改密钥
                            </button>
                        </div>"""

nebula_dynamic = """<div class="space-y-3" id="api-display-nebula">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span id="api-key-text-nebula">••••••••••••••••cdef</span>
                                <span id="api-key-check-nebula" class="material-symbols-outlined text-[16px] text-emerald-500">check_circle</span>
                            </div>
                            <button onclick="toggleApiEdit('nebula')" class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2">
                                <span id="api-btn-icon-nebula" class="material-symbols-outlined text-[18px]">edit</span>
                                <span id="api-btn-text-nebula">修改密钥</span>
                            </button>
                        </div>
                        <div class="space-y-3 hidden" id="api-edit-nebula">
                            <input id="api-input-nebula" type="text" value="sk-nebula-1234567890abcdef" placeholder="输入您的 API Key..." class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-primary/50 focus:border-primary focus:ring-2 focus:ring-primary/20 text-sm text-text-main-light dark:text-text-main-dark outline-none transition-all font-mono" />
                            <div class="flex gap-2">
                                <button onclick="saveApiKey('nebula')" class="flex-1 bg-primary hover:bg-[#5558e3] text-white text-sm font-medium py-2 rounded-xl transition-colors">
                                    保存
                                </button>
                                <button onclick="cancelApiEdit('nebula')" class="flex-1 bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-200 text-sm font-medium py-2 rounded-xl transition-colors">
                                    取消
                                </button>
                            </div>
                        </div>"""
content = content.replace(nebula_static, nebula_dynamic)

# For ZenMux
zenmux_static = """<div class="space-y-3">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span>尚未配置密钥</span>
                            </div>
                            <button class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2">
                                <span class="material-symbols-outlined text-[18px]">add</span>
                                添加密钥
                            </button>
                        </div>"""

zenmux_dynamic = """<div class="space-y-3" id="api-display-zenmux">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span id="api-key-text-zenmux">尚未配置密钥</span>
                                <span id="api-key-check-zenmux" class="material-symbols-outlined text-[16px] text-emerald-500 hidden">check_circle</span>
                            </div>
                            <button onclick="toggleApiEdit('zenmux')" class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2">
                                <span id="api-btn-icon-zenmux" class="material-symbols-outlined text-[18px]">add</span>
                                <span id="api-btn-text-zenmux">添加密钥</span>
                            </button>
                        </div>
                        <div class="space-y-3 hidden" id="api-edit-zenmux">
                            <input id="api-input-zenmux" type="text" placeholder="输入您的 API Key..." class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-primary/50 focus:border-primary focus:ring-2 focus:ring-primary/20 text-sm text-text-main-light dark:text-text-main-dark outline-none transition-all font-mono" />
                            <div class="flex gap-2">
                                <button onclick="saveApiKey('zenmux')" class="flex-1 bg-primary hover:bg-[#5558e3] text-white text-sm font-medium py-2 rounded-xl transition-colors">
                                    保存
                                </button>
                                <button onclick="cancelApiEdit('zenmux')" class="flex-1 bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-200 text-sm font-medium py-2 rounded-xl transition-colors">
                                    取消
                                </button>
                            </div>
                        </div>"""
content = content.replace(zenmux_static, zenmux_dynamic)

# For Volcengine
volcengine_static = """<div class="space-y-3">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span>尚未配置密钥</span>
                            </div>
                            <button class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2">
                                <span class="material-symbols-outlined text-[18px]">add</span>
                                添加密钥
                            </button>
                        </div>"""

volcengine_dynamic = """<div class="space-y-3" id="api-display-volcengine">
                            <div class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400 font-mono flex items-center justify-between">
                                <span id="api-key-text-volcengine">尚未配置密钥</span>
                                <span id="api-key-check-volcengine" class="material-symbols-outlined text-[16px] text-emerald-500 hidden">check_circle</span>
                            </div>
                            <button onclick="toggleApiEdit('volcengine')" class="w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 hover:border-primary dark:hover:border-primary text-text-main-light dark:text-text-main-dark hover:text-primary dark:hover:text-primary text-sm font-medium py-2 rounded-xl transition-colors flex items-center justify-center gap-2">
                                <span id="api-btn-icon-volcengine" class="material-symbols-outlined text-[18px]">add</span>
                                <span id="api-btn-text-volcengine">添加密钥</span>
                            </button>
                        </div>
                        <div class="space-y-3 hidden" id="api-edit-volcengine">
                            <input id="api-input-volcengine" type="text" placeholder="输入您的 API Key..." class="w-full px-4 py-2.5 rounded-xl bg-gray-50 dark:bg-gray-900 border border-primary/50 focus:border-primary focus:ring-2 focus:ring-primary/20 text-sm text-text-main-light dark:text-text-main-dark outline-none transition-all font-mono" />
                            <div class="flex gap-2">
                                <button onclick="saveApiKey('volcengine')" class="flex-1 bg-primary hover:bg-[#5558e3] text-white text-sm font-medium py-2 rounded-xl transition-colors">
                                    保存
                                </button>
                                <button onclick="cancelApiEdit('volcengine')" class="flex-1 bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-200 text-sm font-medium py-2 rounded-xl transition-colors">
                                    取消
                                </button>
                            </div>
                        </div>"""
content = content.replace(volcengine_static, volcengine_dynamic)

# Add status tags for all (id setup)
# Google
content = content.replace(
    """<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300">
                                        未配置
                                    </span>""",
    """<span id="api-status-google" class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300">
                                        未配置
                                    </span>"""
)

# Nebula
content = content.replace(
    """<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400">
                                        已连接
                                    </span>""",
    """<span id="api-status-nebula" class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400">
                                        已连接
                                    </span>"""
)

# ZenMux
# Only replace first matching "未配置" inside ZenMux block
zenmux_start = content.find('ZenMux')
zenmux_end = content.find('尚未配置密钥', zenmux_start)
block = content[zenmux_start:zenmux_end]
new_block = block.replace(
    """<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300">
                                        未配置
                                    </span>""",
    """<span id="api-status-zenmux" class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300">
                                        未配置
                                    </span>"""
)
content = content[:zenmux_start] + new_block + content[zenmux_end:]

# Volcengine
volc_start = content.find('火山引擎')
volc_end = content.find('尚未配置密钥', volc_start)
block = content[volc_start:volc_end]
new_block = block.replace(
    """<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300">
                                        未配置
                                    </span>""",
    """<span id="api-status-volcengine" class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300">
                                        未配置
                                    </span>"""
)
content = content[:volc_start] + new_block + content[volc_end:]


# JS Logic
js_logic = """
function toggleApiEdit(provider) {
    document.getElementById(`api-display-${provider}`).classList.add('hidden');
    document.getElementById(`api-edit-${provider}`).classList.remove('hidden');
    document.getElementById(`api-input-${provider}`).focus();
}

function cancelApiEdit(provider) {
    document.getElementById(`api-display-${provider}`).classList.remove('hidden');
    document.getElementById(`api-edit-${provider}`).classList.add('hidden');
}

function saveApiKey(provider) {
    const inputVal = document.getElementById(`api-input-${provider}`).value.trim();

    const displayBlock = document.getElementById(`api-display-${provider}`);
    const editBlock = document.getElementById(`api-edit-${provider}`);
    const textNode = document.getElementById(`api-key-text-${provider}`);
    const checkNode = document.getElementById(`api-key-check-${provider}`);
    const btnIcon = document.getElementById(`api-btn-icon-${provider}`);
    const btnText = document.getElementById(`api-btn-text-${provider}`);
    const statusTag = document.getElementById(`api-status-${provider}`);

    if (inputVal) {
        // Connected state
        textNode.textContent = '••••••••••••••••' + inputVal.slice(-4);
        checkNode.classList.remove('hidden');
        btnIcon.textContent = 'edit';
        btnText.textContent = '修改密钥';

        statusTag.className = 'inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400';
        statusTag.textContent = '已连接';
    } else {
        // Unconfigured state
        textNode.textContent = '尚未配置密钥';
        checkNode.classList.add('hidden');
        btnIcon.textContent = 'add';
        btnText.textContent = '添加密钥';

        statusTag.className = 'inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300';
        statusTag.textContent = '未配置';
    }

    displayBlock.classList.remove('hidden');
    editBlock.classList.add('hidden');
}
</script>
</body></html>
"""

content = content.replace("</script>\n</body></html>", js_logic)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

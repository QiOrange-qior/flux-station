import re

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Current padding on the wrapper is p-1
    # Let's make it look like the image:
    # 1. wrapper has rounded-2xl (maybe more round) and taller padding
    # 2. the button itself has rounded-xl, padding
    # 3. the font is heavier/different color.

    # Let's change:
    # <div class="flex gap-2 p-1 bg-[#F5F3FF] dark:bg-gray-800 rounded-xl mb-6 border border-[#EDE9FE] dark:border-gray-700">
    # to:
    # <div class="flex p-1.5 bg-[#F8F7FF] dark:bg-gray-800 rounded-[20px] mb-6">

    # And buttons:
    # <button class="flex-1 py-2 px-2 rounded-lg bg-white dark:bg-gray-700 shadow-sm text-[11px] font-bold text-[#6366F1] dark:text-white flex items-center justify-center gap-1.5 uppercase tracking-wide border border-[#EDE9FE] dark:border-gray-600">
    #     Recent
    # </button>
    # to:
    # <button class="flex-1 py-3 px-4 rounded-[16px] bg-white dark:bg-gray-700 shadow-sm text-[12px] font-bold text-[#6366F1] dark:text-white flex items-center justify-center gap-1.5 uppercase tracking-wider border border-[#EDE9FE] dark:border-gray-600">
    #     RECENT
    # </button>
    # <button class="flex-1 py-3 px-4 rounded-[16px] text-[12px] font-bold text-[#6B7280] dark:text-gray-400 hover:text-[#6366F1] dark:hover:text-white transition-colors flex items-center justify-center gap-1.5 uppercase tracking-wider">
    #     COLLECTIONS
    # </button>

    old_div = '''<div class="flex gap-2 p-1 bg-[#F5F3FF] dark:bg-gray-800 rounded-xl mb-6 border border-[#EDE9FE] dark:border-gray-700">
                <button class="flex-1 py-2 px-2 rounded-lg bg-white dark:bg-gray-700 shadow-sm text-[11px] font-bold text-[#6366F1] dark:text-white flex items-center justify-center gap-1.5 uppercase tracking-wide border border-[#EDE9FE] dark:border-gray-600">
                    Recent
                </button>
                <button class="flex-1 py-2 px-2 rounded-lg text-[11px] font-bold text-[#6B7280] dark:text-gray-400 hover:text-[#6366F1] dark:hover:text-white transition-colors flex items-center justify-center gap-1.5 uppercase tracking-wide">
                    Collections
                </button>
            </div>'''

    new_div = '''<div class="flex p-1.5 bg-[#F8F7FF] dark:bg-gray-800 rounded-[20px] mb-6 border border-white dark:border-gray-700 shadow-sm">
                <button class="flex-1 py-2.5 px-4 rounded-[14px] bg-white dark:bg-gray-700 shadow-sm text-[12px] font-bold text-[#6366F1] dark:text-white flex items-center justify-center uppercase tracking-[0.05em] border border-white dark:border-gray-600">
                    RECENT
                </button>
                <button class="flex-1 py-2.5 px-4 rounded-[14px] text-[12px] font-bold text-[#6B7280] dark:text-gray-400 hover:text-[#6366F1] dark:hover:text-white transition-colors flex items-center justify-center uppercase tracking-[0.05em]">
                    COLLECTIONS
                </button>
            </div>'''

    if old_div in content:
        content = content.replace(old_div, new_div)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated tab buttons.")
    else:
        print("Could not find old_div.")

if __name__ == '__main__':
    update_file('index.html')

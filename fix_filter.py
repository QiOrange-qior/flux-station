with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the js filtering logic
old_logic = """
                        if (filter === '全部') {
                            shouldShow = true;
                        } else if (filter === '微调' && tag === 'lora') {
                            shouldShow = true;
                        } else if (filter === '风格' && tag === 'style') {
                            shouldShow = true;
                        } else if (filter === '角色' && tag === 'character') {
                            shouldShow = true;
                        } else if (filter === '场景' && tag === 'environment') {
                            shouldShow = true;
                        } else if (filter === 'checkpoint' && tag === 'checkpoint') {
                            shouldShow = true;
                        } else if (filter === 'texture' && tag === 'texture') {
                            shouldShow = true;
                        }
"""

new_logic = """
                        if (filter === '全部') {
                            shouldShow = true;
                        } else if (filter === '微调' && tag === 'lora') {
                            shouldShow = true;
                        } else if (filter === '风格' && (tag === '风格' || tag === 'style')) {
                            shouldShow = true;
                        } else if (filter === '角色' && (tag === '角色' || tag === 'character')) {
                            shouldShow = true;
                        } else if (filter === '场景' && (tag === '场景' || tag === 'environment')) {
                            shouldShow = true;
                        } else if (filter === 'checkpoint' && tag === 'checkpoint') {
                            shouldShow = true;
                        } else if (filter === 'texture' && tag === 'texture') {
                            shouldShow = true;
                        }
"""

content = content.replace(old_logic, new_logic)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

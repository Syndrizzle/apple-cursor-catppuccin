import os
import re

CORRECT_ORDER = [
    "pointer", "help", "work", "busy", "cross", "text", "hand", "unavailable", 
    "vert", "horz", "dgn1", "dgn2", "move", "alternate", "link"
]

CURSOR_NAME_MAP = {
    "handwriting": "hand",
    "unavailiable": "unavailable",  # Fix typo in original
    "dng1": "dgn1",
    "dng2": "dgn2"
}

def fix_inf_file(inf_path):
    with open(inf_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    scheme_cur_match = re.search(r'\[Scheme\.Cur\](.*?)(?=\[|$)', content, re.DOTALL)
    if not scheme_cur_match:
        return
    
    cursor_files = [x.strip() for x in scheme_cur_match.group(1).strip().split('\n') if x.strip()]
    
    cursor_map = {}
    cursor_pattern = re.compile(r'(\w+)\s*=\s*["\']?(.*?\.(?:cur|ani))["\']?$')
    
    for line in content.split('\n'):
        match = cursor_pattern.search(line)
        if match:
            name, file = match.groups()
            name = name.strip()
            if name in CURSOR_NAME_MAP:
                name = CURSOR_NAME_MAP[name]
            cursor_map[name] = file

    new_scheme_cur = ['[Scheme.Cur]']
    for cursor_type in CORRECT_ORDER:
        if cursor_type in cursor_map:
            new_scheme_cur.append(cursor_map[cursor_type])
    
    remaining_cursors = set(cursor_map.values()) - set(new_scheme_cur[1:] if len(new_scheme_cur) > 1 else [])
    new_scheme_cur.extend(sorted(remaining_cursors))
    
    new_content = re.sub(
        r'\[Scheme\.Cur\].*?(?=\[|$)',
        '\n'.join(new_scheme_cur) + '\n\n',
        content,
        flags=re.DOTALL
    )
    
    with open(inf_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def process_themes_directory(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('install.inf'):
                inf_path = os.path.join(root, file)
                fix_inf_file(inf_path)

if __name__ == '__main__':
    process_themes_directory('themes')
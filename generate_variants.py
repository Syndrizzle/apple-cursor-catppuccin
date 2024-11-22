import json
from pathlib import Path
from catppuccin import PALETTE
import unicodedata

"""
Note: This script generates only Mauve accent variants.
To generate other accent colors, modify the ACCENT_COLOR const to any of:
- rosewater, flamingo, pink, mauve, red, maroon, peach, yellow
- green, teal, sky, sapphire, blue, lavender
"""

ACCENT_COLOR = 'mauve'

def normalize_name(name):
    # Replace Frappé with Frappe
    if name == "Frappé":
        return "Frappe"
    return name

def generate_variants():
    # Load existing render.json
    render_json_path = Path('render.json')
    try:
        with open(render_json_path, 'r') as f:
            render_config = json.load(f)
    except FileNotFoundError:
        render_config = {}

    # Keep only the original macOS entries
    filtered_config = {k: v for k, v in render_config.items() 
                      if not k.startswith('macOS-Catppuccin-')}

    # Generate variants for each flavor
    for flavor in PALETTE:
        base_color = getattr(flavor.colors, 'base').hex
        accent_color = getattr(flavor.colors, ACCENT_COLOR).hex
        
        normalized_name = normalize_name(flavor.name)
            
        # Dark variant (base background, accent outline)
        dark_key = f"macOS-Catppuccin-{normalized_name}-Dark"
        filtered_config[dark_key] = {
            "dir": "svg",
            "out": f"bitmaps/{dark_key}",
            "colors": [
                {"match": "#00FF00", "replace": base_color},
                {"match": "#0000FF", "replace": accent_color}
            ]
        }

        # Light variant (accent background, base outline)
        light_key = f"macOS-Catppuccin-{normalized_name}"
        filtered_config[light_key] = {
            "dir": "svg",
            "out": f"bitmaps/{light_key}",
            "colors": [
                {"match": "#00FF00", "replace": accent_color},
                {"match": "#0000FF", "replace": base_color}
            ]
        }

    # Save updated render.json
    with open(render_json_path, 'w') as f:
        json.dump(filtered_config, f, indent=2)

    # Update build.sh
    build_sh_path = Path('build.sh')
    if not build_sh_path.exists():
        print("build.sh not found!")
        return

    # Read build.sh content
    with open(build_sh_path, 'r') as f:
        content = f.read()

    names_start = content.find('declare -A names')
    names_end = content.find('# Cleanup old builds')
    
    if names_start == -1 or names_end == -1:
        print("Could not find names declaration section in build.sh!")
        return
    new_names = ['declare -A names']
    
    # Add Catppuccin variants
    for flavor in PALETTE:
        normalized_name = normalize_name(flavor.name)
        new_names.append(f'names["macOS-Catppuccin-{normalized_name}-Dark"]=$(with_version "Catppuccin {normalized_name} Dark")')
        new_names.append(f'names["macOS-Catppuccin-{normalized_name}"]=$(with_version "Catppuccin {normalized_name}")')

    # Replace the names section in build.sh
    new_content = (
        content[:names_start] +
        '\n'.join(new_names) +
        '\n\n' +
        content[names_end:]
    )

    with open(build_sh_path, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    generate_variants()
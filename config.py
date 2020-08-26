import tempfile
import json

# Build Config
delay = 35
name = "macOSBigSur"
sizes = [24, 28, 32, 40, 48, 56, 64, 72, 80, 88, 96]

bitmaps_dir = "./bitmaps"
temp_folder = tempfile.mkdtemp()

# Cleanup Configs
x11_out = name
win_out = name + "_Windows"

# getting author name
with open("./package.json") as f:
    data = json.loads(f.read())
    author = data["author"]

# Windows Cursors Config
windows_cursors = {
    "all-scroll.cur": "move.cur",
    "bd_double_arrow.cur": "diagonal-resize-1.cur",
    "bottom_left_corner.cur": "diagonal-resize-2.cur",
    "bottom_side.cur": "vertical-resize.cur",
    "circle.cur": "unavailable.cur",
    "crosshair.cur": "precision-select.cur",
    "dnd-ask.cur": "help-select.cur",
    "hand2.cur": "link-select.cur",
    "left_ptr.cur": "normal-select.cur",
    "left_ptr_watch.ani": "working-in-background.ani",
    "pencil.cur": "handwriting.cur",
    "right_side.cur": "horizontal-resize.cur",
    "sb_up_arrow.cur": "alt-select.cur",
    "wait.ani": "busy.ani",
    "x_cursor.cur": "pirate.cur",
    "xterm.cur": "text-select.cur"
}

# Windows install.inf file content
with open("./scripts/windows.inf") as f:
    data = f.read()
    window_install_inf_content = data.replace(
        "<inject_theme_name>", name+" Cursors").replace("<inject_author_name>", author)

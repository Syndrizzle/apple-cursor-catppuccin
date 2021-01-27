#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, List, Tuple

# Info
THEME_NAME = "macOSBigSur"
COMMENT = "macOS Big Sur Pointers"
AUTHOR = "Kaiz Khatri"
URL = "https://github.com/ful1e5/apple_cursor"

# XCursor
X_DELAY: int = 10
X_SIZES: List[Tuple[int, int]] = [(24, 24), (32, 32)]


# Windows Cursor
CANVAS_SIZE = (32, 32)
SIZE = (24, 24)
WIN_DELAY = 3

X_CURSORS_CFG: Dict[str, Dict[str, int]] = {
    #
    # Static
    #
    "all_scroll.png": {"xhot": 100, "yhot": 100},
    "bottom_left_corner.png": {"xhot": 100, "yhot": 100},
    "fd_double_arrow.png": {"xhot": 100, "yhot": 100},
    "top_right_corner.png": {"xhot": 100, "yhot": 100},
    "bottom_right_corner.png": {"xhot": 100, "yhot": 100},
    "bd_double_arrow.png": {"xhot": 100, "yhot": 100},
    "top_left_corner.png": {"xhot": 100, "yhot": 100},
    "bottom_tee.png": {"xhot": 141, "yhot": 99},
    "center_ptr.png": {"xhot": 61, "yhot": 100},
    "circle.png": {"xhot": 47, "yhot": 39},
    "crossed_circle.png": {"xhot": 47, "yhot": 39},
    "dnd_no_drop.png": {"xhot": 47, "yhot": 39},
    "context_menu.png": {"xhot": 61, "yhot": 58},
    "copy.png": {"xhot": 47, "yhot": 39},
    "dnd_copy.png": {"xhot": 47, "yhot": 39},
    "cross.png": {"xhot": 100, "yhot": 100},
    "tcross.png": {"xhot": 100, "yhot": 100},
    "crosshair.png": {"xhot": 100, "yhot": 100},
    "dotbox.png": {"xhot": 100, "yhot": 100},
    "hand1.png": {"xhot": 94, "yhot": 105},
    "hand2.png": {"xhot": 66, "yhot": 34},
    "left_ptr.png": {"xhot": 68, "yhot": 41},
    "left_side.png": {"xhot": 100, "yhot": 100},
    "right_side.png": {"xhot": 100, "yhot": 100},
    "left_tee.png": {"xhot": 100, "yhot": 58},
    "link.png": {"xhot": 61, "yhot": 105},
    "dnd_link.png": {"xhot": 61, "yhot": 105},
    "ll_angle.png": {"xhot": 141, "yhot": 58},
    "lr_angle.png": {"xhot": 141, "yhot": 138},
    "move.png": {"xhot": 80, "yhot": 106},
    "dnd_move.png": {"xhot": 80, "yhot": 106},
    "dnd_none.png": {"xhot": 80, "yhot": 106},
    "grabbing.png": {"xhot": 80, "yhot": 106},
    "pointer_move.png": {"xhot": 80, "yhot": 106},
    "pencil.png": {"xhot": 141, "yhot": 58},
    "plus.png": {"xhot": 100, "yhot": 100},
    "question_arrow.png": {"xhot": 105, "yhot": 105},
    "dnd_ask.png": {"xhot": 105, "yhot": 105},
    "right_ptr.png": {"xhot": 61, "yhot": 138},
    "right_tee.png": {"xhot": 100, "yhot": 138},
    "sb_down_arrow.png": {"xhot": 133, "yhot": 99},
    "sb_h_double_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_left_arrow.png": {"xhot": 100, "yhot": 68},
    "sb_right_arrow.png": {"xhot": 100, "yhot": 138},
    "sb_up_arrow.png": {"xhot": 68, "yhot": 99},
    "sb_v_double_arrow.png": {"xhot": 100, "yhot": 100},
    "top_side.png": {"xhot": 100, "yhot": 100},
    "bottom_side.png": {"xhot": 100, "yhot": 100},
    "top_tee.png": {"xhot": 61, "yhot": 99},
    "ul_angle.png": {"xhot": 61, "yhot": 65},
    "ur_angle.png": {"xhot": 61, "yhot": 138},
    "vertical_text.png": {"xhot": 100, "yhot": 102},
    "wayland_cursor.png": {"xhot": 100, "yhot": 100},
    "x_cursor.png": {"xhot": 100, "yhot": 100},
    "xterm.png": {"xhot": 97, "yhot": 97},
    "zoom_in.png": {"xhot": 76, "yhot": 78},
    "zoom_out.png": {"xhot": 76, "yhot": 78},
    #
    # Animated
    #
    # Note: Animated cursors not need any extension & frames number
    "wait": {"xhot": 104, "yhot": 105},
    "left_ptr_watch": {"xhot": 104, "yhot": 105},
}

WIN_CURSORS_CFG: Dict[str, Dict[str, str]] = {
    #
    # Static
    #
    "right_ptr.png": {"to": "Alternate", "position": "top_left"},
    "cross.png": {"to": "Cross"},
    "left_ptr.png": {"to": "Default", "position": "top_left"},
    "fd_double_arrow.png": {"to": "Diagonal_1"},
    "bd_double_arrow.png": {"to": "Diagonal_2"},
    "pencil.png": {"to": "Handwriting"},
    "question_arrow.png": {"to": "Help", "position.png": "top_left"},
    "sb_h_double_arrow.png": {"to": "Horizontal"},
    "xterm.png": {"to": "IBeam", "position": "top_left"},
    "hand2.png": {"to": "Link", "position": "top_left"},
    "hand1.png": {"to": "Move"},
    "circle.png": {"to": "Unavailiable", "position": "top_left"},
    "sb_v_double_arrow.png": {"to": "Vertical"},
    #
    # Animated
    #
    # Note: Animated cursors not need any extension & frames number
    "wait": {"to": "Busy", "size": (28, 28)},
    "left_ptr_watch": {"to": "Work", "position": "top_left", "size": (28, 28)},
}

print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.hid import HIDModes
from kmk.scanners import DiodeOrientation
# from kmk.modules.power import Power


keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.row_pins = (board.P0_22, board.P0_24, board.P0_09, board.P0_11, board.P1_04)
keyboard.col_pins = (board.P0_31, board.P1_11, board.P1_00, board.P1_06)
# keyboard.debug_enabled = True

keyboard.keymap = [
    [
        KC.BSPACE, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS,
        KC.N7,   KC.N8,     KC.N9,        KC.KP_PLUS,
        KC.N4,   KC.N5,     KC.N6,        KC.KP_PLUS,
        KC.N1,   KC.N2,     KC.N3,        KC.ENTER,
        KC.N0,   KC.N0,     KC.DOT,      KC.ENTER,
    
    ]
]

# power = Power()
# keyboard.modules.append(power)

if __name__ == "__main__":
    keyboard.go()
    # keyboard.go()
import mido
from pynput.keyboard import Controller
import time

KEY_MAP = {
    72: 'q',  # Middle C
    73: '2',
    74: 'w',
    75: '3',
    76: 'e', # D
    77: 'r',  # E
    78: '5',
    79: 't',  # F
    80: '6',
    81: 'y',  # G
    82: '7',
    83: 'u',
    84: 'i',
    48: ',',
    49: 'l',
    50: '.',
    51: ';',
    52: '/',
    53: 'o',
    54: '0',
    55: 'p',
    56: '-',
    57: '[',
    58: '=',
    59: ']',
    60: 'z',
    61: 's',
    62: 'x',
    63: 'd',
    64: 'c',
    65: 'v',
    66: 'g',
    67: 'b',
    68: 'h',
    69: 'n',
    70: 'j',
    71: 'm',
}

keyboard = Controller()
try:
    with mido.open_input('Yamaha PSR-K1-1 0') as inport:
        print("Ready! Play your piano.")
        for msg in inport:
            if msg.type == 'note_on' and msg.velocity > 0:
                if msg.note in KEY_MAP:
                    target_key = KEY_MAP[msg.note]
                    keyboard.press(target_key)
                    time.sleep(0.05)
                    keyboard.release(target_key)
                    
                    print(f"MIDI {msg.note} -> Typed '{target_key}'")
except KeyboardInterrupt:
    print("\nScript Stopped.")

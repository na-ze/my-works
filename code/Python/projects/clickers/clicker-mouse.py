import keyboard
import time
from pynput.mouse import Button, Controller

mouse = Controller()
clicker_enabled = False

def on_keypress(event):
    global clicker_enabled
    
    if event.name == 's':  
        clicker_enabled = not clicker_enabled
        
        if clicker_enabled:
            print('Кликер включен')
        else:
            print('Кликер выключен')

keyboard.on_press(on_keypress)

while True:
    if clicker_enabled:
        mouse.click(Button.left)
        #mouse.press(Button.left)
    time.sleep(0.5)


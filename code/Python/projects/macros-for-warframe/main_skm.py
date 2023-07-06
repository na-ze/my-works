import keyboard
from time import sleep

def perform_combination():
    keyboard.press('p')
    sleep(0.2)
    keyboard.press('ctrl')
    sleep(0.2)
    keyboard.send('o')
    sleep(0.2)
    keyboard.release('ctrl')
    sleep(0.2)
    keyboard.release('p')
    
is_combination_triggered = False

def on_key_press(event):
    global is_combination_triggered

    if event.name == 'v' and not is_combination_triggered:
        perform_combination()
        is_combination_triggered = True

    if event.name == 'v' and is_combination_triggered:
        is_combination_triggered = False

keyboard.on_press(on_key_press)

while True:
    if keyboard.is_pressed('y'):  # Проверяем, нажата ли клавиша "Esc"
        break


import keyboard

def on_keypress(event):
    # ваш код для обработки события
    print('Нажата клавиша:', event.name)

# Переопределение функции on_press
keyboard.on_press(on_keypress)

# Дальнейший код вашей программы...




import keyboard

def on_keypress(event):
    if event.name == 'a':
        print('Вы нажали клавишу A')
        # Добавьте ваш код для обработки нажатия клавиши A
    elif event.name == 'b':
        print('Вы нажали клавишу B')
        # Добавьте ваш код для обработки нажатия клавиши B
    else:
        print('Вы нажали другую клавишу:', event.name)
        # Добавьте ваш код для обработки других клавиш

# Переопределение функции on_press
keyboard.on_press(on_keypress)

# Дальнейший код вашей программы...


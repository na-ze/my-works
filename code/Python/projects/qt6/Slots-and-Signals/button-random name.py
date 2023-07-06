from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
from random import choice
import sys

# Description
#Данный код использует библиотеку PyQt6 для создания оконного приложения. 
#Он создает окно с кнопкой "Press Me!", которая изменяет заголовок окна случайным образом и выводит сообщения в консоль при нажатии на нее и изменении заголовка окна. 
#Если заголовок становится равным "Something went wrong", то кнопка блокируется и становится неактивной. Размер окна установлен на 400x300 пикселей.


window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

# Создадим подкласс:
class MainWindow(QMainWindow):
    def __init__(self):
        # Это база - вызывает конструктор родительского класса QMainWindow
        super(MainWindow, self).__init__()
        
        # Называем наше приложение(его заголовок)
        self.setWindowTitle("My app")

        self.n_times_clicked = 0

        # Создаём и настраиваем кнопку, self - потому, что мы её будем изменять в другой функции
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        # Сигнал windowTitleChanged при установке заголовка окна выдаётся не всегда.
        # Он срабатывает, только если новый заголовок отличается от предыдущего
        self.windowTitleChanged.connect(self.the_window_title_changed) # Изменяет заголовок окна

        # Устанавливаем кнопку по середине экрана
        self.setCentralWidget(self.button)

        # Устанавливаем размер окна
        self.setFixedSize(QSize(400, 300))

    # Создаём функции
    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print(f"Setting title: {new_window_title}")
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print(f"Window title changed: {window_title}")

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)  # Если заголовок становится равным "Something went wrong", то мы отключаем кнопку
            #self.button.setEnabled(False)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


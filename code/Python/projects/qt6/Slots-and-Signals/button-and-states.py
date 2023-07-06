from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
import sys 

# Description:
#Данный код представляет собой пример использования библиотеки PyQt6 для создания оконного приложения.
#Он создает окно с фиксированным размером и содержит кнопку, которая может переключаться между двумя состояниями. 
#Таким образом, код создает окно с кнопкой, которая меняет свое состояние при нажатии, и выводит информацию о текущем состоянии кнопки в консоль.

# Создадим подкласс:
class MainWindow(QMainWindow):
    def __init__(self):
# Это база - вызывает конструктор родительского класса QMainWindow
        super(MainWindow, self).__init__()
# Называем наше приложение(его заголовок)
        self.setWindowTitle("My app")


# Устанавливаем состояние кнопки
        self.button_is_checked = True


# Создаём и настраиваем кнопки
        button = QPushButton("Press Me!")
        button.setCheckable(True) #делает кнопку переключаемой (checkable)
        #button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled) # Устанавливаем что будет происходить с кнопкой при нажатии
        button.setChecked(self.button_is_checked) # Устанавливаем начальное состояние кнопки


# Устанавливаем кнопку по середине экрана
        self.setCentralWidget(button)


# Устанавливаем размер окна
        self.setFixedSize(QSize(400, 300))
        #self.setMinimumSize(QSize(200, 100))  # Установка минимального размера
        #self.setMaximumSize(QSize(400, 300))  # Установка максимального размера


# Созздаём функции
    def the_button_was_clicked(self):
        print("CLicked!")

    # Каждый раз когда кнопка будет нажата, она будет менять своё состоение, и выводить "Pressed?" вместе со своим состоянием
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Pressed?", checked)

    







app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()

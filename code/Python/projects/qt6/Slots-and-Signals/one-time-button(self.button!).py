from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
import sys 

# Description
#Данный код использует библиотеку PyQt6 для создания оконного приложения. 
#Он создает окно с кнопкой "Press Me!", которая меняет свой текст и состояние после нажатия, блокируется для повторных нажатий, а также изменяется заголовок окна.

# Создадим подкласс:
class MainWindow(QMainWindow):
    def __init__(self):
# Это база - вызывает конструктор родительского класса QMainWindow
        super(MainWindow, self).__init__()
# Называем наше приложение(его заголовок)
        self.setWindowTitle("My app")


# Создаём и настраиваем кнопки
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)


# Устанавливаем кнопку по середине экрана
        self.setCentralWidget(self.button)


# Созздаём функции
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.") #Меняем текст кнопки
        self.button.setEnabled(False) #Делаем кнопку не осязаемой, ну тип не доступной, блочим её после нажатия крч
        self.setWindowTitle("My Oneshot App") # Также меняем заголовок окна.


#Крч брат, тут очень важная фигня есть    
#Вот смотрим, если ты не будешь работать с кнопкой, то создаёшь переменную просто - button
#А если будешь, тип там имя её меня, блокировать и т.д. ТО обязательно создаёшь вот так - self.button
#это позволяет тебе использовать(изменять) её не только в __init__, но и в других функция
#Удачи тебе брат


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()

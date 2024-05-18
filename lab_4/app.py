from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QPixmap

import sys

from functions import json_reader
from constants import PATHS, DATA

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Programm")
        self.setFixedSize(1200, 900)
        self.setStyleSheet(f'background-color: #272424;')

        widget = QWidget()
        widget.setGeometry(200, 0, 1000, 0)
        self.setCentralWidget(widget)
        widget.setStyleSheet(f'background-color: #81A3A7; margin: 0 150px 0 150px;')
        
        css_label = f'font-size: 18px; border-radius: 10px 10px; background-color: #C2D3DA; padding: 10px;'
        css_button = f'font-size: 18px; padding: 10px; background-color: #C2D3DA; border: 5px solid #585A56; border-radius:10px'
        css_edit = f'{css_label} color: hsla(0, 0%, 0%, 0.5);'

        card_id_label = QLabel('Узнать номер карты', self)
        card_id_label.setGeometry(250, 60, 194, 50)
        card_id_label.setStyleSheet(css_label)

        card_id_button = QPushButton('УЗНАТЬ', self)
        card_id_button.setGeometry(250, 130, 100, 50)
        card_id_button.setStyleSheet(css_button)

        luhn_label = QLabel('Проверить номер карты по алгоритму Луна', self)
        luhn_label.setGeometry(250, 250, 390, 50)
        luhn_label.setStyleSheet(css_label)

        luhn_button = QPushButton('ПРОВЕРИТЬ', self)
        luhn_button.setGeometry(250, 320, 140, 50)
        luhn_button.setStyleSheet(css_button)

        pic_label = QLabel('Построить график зависимости времени на поиск коллизий', self)
        pic_label.setGeometry(250, 430, 524, 50)
        pic_label.setStyleSheet(css_label)

        pic_button = QPushButton('ПОСТРОИТЬ', self)
        pic_button.setGeometry(250, 500, 140, 50)
        pic_button.setStyleSheet(css_button)

        hash = QLineEdit('Хэш', self)
        hash.setGeometry(514, 60, 100, 50)
        hash.setStyleSheet(css_edit)

        last_digits = QLineEdit('Последние цифры', self)
        last_digits.setGeometry(620, 60, 174, 50)
        last_digits.setStyleSheet(css_edit)
        
        bin = QLineEdit('БИН-номер', self)
        bin.setGeometry(800, 60, 174, 50)
        bin.setStyleSheet(css_edit)

        card_id = QLabel('Полученный номер карты', self)
        card_id.setGeometry(514, 130, 460, 50)
        card_id.setStyleSheet(css_edit)

        card_id_luhn = QLineEdit('Номер карты', self)
        card_id_luhn.setGeometry(680, 250, 294, 50)
        card_id_luhn.setStyleSheet(css_edit)

        card_validity = QLabel('Действительность карты', self)
        card_validity.setGeometry(514, 320, 460, 50)
        card_validity.setStyleSheet(css_edit)

        exit_button = QPushButton('Выход', self)
        exit_button.setGeometry(1085, 20, 90, 50)
        exit_button.setStyleSheet(css_button)
        #exit_button.clicked().connect(self.close)

class ImageDisplay(QWidget):
    def __init__(self, image_path: str):
        super().__init__()
        self.initUI(image_path)
        self.image_path = image_path

    def initUI(self, image_path: str):
        self.setWindowTitle('Image Display')
        self.setFixedSize(1500, 500)
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.show()


def application(image_path: str):
    app = QApplication(sys.argv)
    application = MainWindow()
    image = ImageDisplay(image_path)
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    paths = json_reader(PATHS)
    data = json_reader(DATA)
    application(paths["picture_path"])
 
import sys
import logging
import re

from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QWidget,
    QLabel,
    QLineEdit,
)
from PyQt5.QtGui import QPixmap

from card_hash_operate import HashOperating


from functions import ReadWrite
from constants import PATHS, DATA


class MainWindow(QMainWindow):
    """UI Class for operating with HashOperating class functions"""

    def __init__(self):
        """Initialises MainWindow object.
        :return: None.
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initialises UI elements and links with functions.
        :return: None.
        """

        self.setWindowTitle("Programm")
        self.setFixedSize(1200, 900)
        self.setStyleSheet(f"background-color: #272424;")

        self.widget_back = QWidget()
        self.widget_back.setGeometry(200, 0, 1000, 0)
        self.setCentralWidget(self.widget_back)
        self.widget_back.setStyleSheet(
            f"background-color: #81A3A7; margin: 0 150px 0 150px;"
        )

        self.css_label = f"font-size: 18px; border-radius: 10px 10px; background-color: #C2D3DA; padding: 10px;"
        self.css_button = f"font-size: 18px; padding: 10px; background-color: #C2D3DA; border: 5px solid #585A56; border-radius:10px"
        self.css_edit = f"{self.css_label} color: hsla(0, 0%, 0%, 0.5);"

        self.card_id_label = QLabel("Узнать номер карты", self)
        self.card_id_label.setGeometry(250, 60, 194, 50)
        self.card_id_label.setStyleSheet(self.css_label)

        self.card_id_button = QPushButton("УЗНАТЬ", self)
        self.card_id_button.setGeometry(250, 130, 100, 50)
        self.card_id_button.setStyleSheet(self.css_button)

        self.luhn_label = QLabel("Проверить номер карты по алгоритму Луна", self)
        self.luhn_label.setGeometry(250, 250, 390, 50)
        self.luhn_label.setStyleSheet(self.css_label)

        self.luhn_button = QPushButton("ПРОВЕРИТЬ", self)
        self.luhn_button.setGeometry(250, 320, 140, 50)
        self.luhn_button.setStyleSheet(self.css_button)

        self.pic_label = QLabel(
            "Построить график зависимости времени на поиск коллизий", self
        )
        self.pic_label.setGeometry(250, 430, 524, 50)
        self.pic_label.setStyleSheet(self.css_label)

        self.pic_button = QPushButton("ПОСТРОИТЬ", self)
        self.pic_button.setGeometry(250, 500, 140, 50)
        self.pic_button.setStyleSheet(self.css_button)

        self.hash = QLineEdit("Хэш", self)
        self.hash.setGeometry(514, 60, 100, 50)
        self.hash.setStyleSheet(self.css_edit)

        self.last_digits = QLineEdit("Последние цифры", self)
        self.last_digits.setGeometry(620, 60, 174, 50)
        self.last_digits.setStyleSheet(self.css_edit)

        self.bin = QLineEdit("БИН-номер", self)
        self.bin.setGeometry(800, 60, 174, 50)
        self.bin.setStyleSheet(self.css_edit)

        self.card_id = QLabel("Полученный номер карты", self)
        self.card_id.setGeometry(514, 130, 460, 50)
        self.card_id.setStyleSheet(self.css_edit)

        self.card_id_luhn = QLineEdit("Номер карты", self)
        self.card_id_luhn.setGeometry(680, 250, 294, 50)
        self.card_id_luhn.setStyleSheet(self.css_edit)

        self.card_validity = QLabel("Действительность карты", self)
        self.card_validity.setGeometry(514, 320, 460, 50)
        self.card_validity.setStyleSheet(self.css_edit)

        self.image = QLabel(self)

        self.exit_button = QPushButton("Выход", self)
        self.exit_button.setGeometry(1085, 20, 90, 50)
        self.exit_button.setStyleSheet(self.css_button)

        self.exit_button.clicked.connect(self.close)
        self.card_id_button.clicked.connect(self.card_id_calculate_click)
        self.luhn_button.clicked.connect(self.luhn_algorithm_click)
        self.pic_button.clicked.connect(self.draw_picture_click)

    class ImageDisplay(QWidget):
        """Class for displaying image"""

        def __init__(self):
            """Initialises ImageDisplay object.
            :return: None.
            """
            super().__init__()
            self.initUI()

        def initUI(self):
            """Initialises picture window.
            :return: None.
            """
            self.setWindowTitle("Image Display")
            self.setFixedSize(1500, 500)
            self.image_label = QLabel(self)
            pixmap = QPixmap(ReadWrite.json_reader(PATHS)["picture_path"])
            self.image_label.setPixmap(pixmap)
            self.show()

    def card_id_calculate_click(self):
        """Triggers card id calculation.
        :return: None.
        """
        try:
            hash = self.hash.text()
            last_digits = self.last_digits.text()
            bin = self.bin.text()

            card_id = HashOperating.get_id_by_hash(hash, last_digits, tuple(bin))
            if card_id == None:
                self.card_id.setText("Не удалось найти номер карты")
            else:
                self.card_id.setText(card_id)
        except Exception as exc:
            logging.error(f"Card id button click error: {exc}\n")

    def luhn_algorithm_click(self):
        """Triggers card id validity luhn test.
        :return: None.
        """
        try:
            card_id = self.card_id_luhn.text()
            is_valid = HashOperating.luhn_alg(card_id)
            if is_valid:
                self.card_validity.setText("Карта действительна")
            else:
                self.card_validity.setText("Карта недействительна")
        except Exception as exc:
            logging.error(f"luhn button click error: {exc}\n")

    def draw_picture_click(self):
        """Triggers collision time picture draw and show.
        :return: None.
        """
        try:
            paths = ReadWrite.json_reader(PATHS)
            data = ReadWrite.json_reader(DATA)
            HashOperating.collision_time(
                data["hash"], data["last_digits"], data["bin"], paths["picture_path"]
            )
            pixmap = QPixmap(paths["picture_path"])
            self.image.setGeometry(250, 570, 724, 241)
            pixmap = pixmap.scaled(724, 241)
            self.image.setPixmap(pixmap)
        except Exception as exc:
            logging.error(f"Draw button click error: {exc}\n")


def application():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()

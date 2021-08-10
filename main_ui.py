from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import src.segment as sg

import src.main_window  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = src.main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_choise_image.clicked.connect(self.btn_choise_image_clicked)

    def btn_choise_image_clicked(self):
        file_path = QFileDialog.getOpenFileName(self, "Выберите файл", "data/input_images")
        self.ui.path_to_image.setText(file_path[0])

        pixmap = QPixmap(file_path[0])
        smaller_pixmap = pixmap.scaled(350, 350)
        self.ui.input_image.setPixmap(smaller_pixmap)

        print(file_path[0])
        segment = sg.segment(file_path[0])
        segment.create_histogram()

        pixmap2 = QPixmap(sg.segment.path_to_histogram)
        # w =450
        # smaller_pixmap2 = pixmap2.scaled(w, w/1.333)
        self.ui.histogram.setPixmap(pixmap2)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())

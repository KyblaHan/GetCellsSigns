# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(720, 10, 631, 187))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mins = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.mins.setText("")
        self.mins.setObjectName("mins")
        self.gridLayout_2.addWidget(self.mins, 2, 1, 1, 1)
        self.label_max = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.label_max.setObjectName("label_max")
        self.gridLayout_2.addWidget(self.label_max, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.hist_sense = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.hist_sense.setObjectName("hist_sense")
        self.gridLayout_2.addWidget(self.hist_sense, 1, 1, 1, 1)
        self.path_to_image = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.path_to_image.setObjectName("path_to_image")
        self.gridLayout_2.addWidget(self.path_to_image, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.slider_max = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.slider_max.setMaximum(100)
        self.slider_max.setOrientation(QtCore.Qt.Horizontal)
        self.slider_max.setObjectName("slider_max")
        self.gridLayout_2.addWidget(self.slider_max, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_min = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.label_min.setObjectName("label_min")
        self.gridLayout_2.addWidget(self.label_min, 3, 2, 1, 1)
        self.btn_calc_mins = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_calc_mins.setObjectName("btn_calc_mins")
        self.gridLayout_2.addWidget(self.btn_calc_mins, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.btn_choise_image = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_choise_image.setObjectName("btn_choise_image")
        self.gridLayout_2.addWidget(self.btn_choise_image, 0, 2, 1, 1)
        self.slider_min = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.slider_min.setMaximum(100)
        self.slider_min.setSingleStep(1)
        self.slider_min.setOrientation(QtCore.Qt.Horizontal)
        self.slider_min.setObjectName("slider_min")
        self.gridLayout_2.addWidget(self.slider_min, 3, 1, 1, 1)
        self.btn_contour = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_contour.setObjectName("btn_contour")
        self.gridLayout_2.addWidget(self.btn_contour, 5, 0, 1, 1)
        self.btn_segment = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_segment.setObjectName("btn_segment")
        self.gridLayout_2.addWidget(self.btn_segment, 5, 1, 1, 1)
        self.btn_sings = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_sings.setObjectName("btn_sings")
        self.gridLayout_2.addWidget(self.btn_sings, 6, 0, 1, 1)
        self.histogram = QtWidgets.QLabel(self.centralwidget)
        self.histogram.setGeometry(QtCore.QRect(720, 240, 640, 480))
        self.histogram.setFrameShape(QtWidgets.QFrame.Box)
        self.histogram.setObjectName("histogram")
        self.segmented_image = QtWidgets.QLabel(self.centralwidget)
        self.segmented_image.setGeometry(QtCore.QRect(20, 370, 350, 350))
        self.segmented_image.setFrameShape(QtWidgets.QFrame.Box)
        self.segmented_image.setObjectName("segmented_image")
        self.input_image = QtWidgets.QLabel(self.centralwidget)
        self.input_image.setGeometry(QtCore.QRect(20, 10, 350, 350))
        self.input_image.setFrameShape(QtWidgets.QFrame.Box)
        self.input_image.setObjectName("input_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Путь к изображению:"))
        self.hist_sense.setText(_translate("MainWindow", "25"))
        self.path_to_image.setText(_translate("MainWindow", "C:\\_Programming\\_DataSets\\for segment\\F0000005.png"))
        self.label_5.setText(_translate("MainWindow", "Минимумы:"))
        self.label_2.setText(_translate("MainWindow", "Чувствительность оценки гистограммы:"))
        self.btn_calc_mins.setText(_translate("MainWindow", "Перерасчет минимумов"))
        self.label_4.setText(_translate("MainWindow", "Верхняя граница:"))
        self.label_3.setText(_translate("MainWindow", "Нижняя граница:"))
        self.btn_choise_image.setText(_translate("MainWindow", "Выбрать"))
        self.btn_contour.setText(_translate("MainWindow", "Найти контура"))
        self.btn_segment.setText(_translate("MainWindow", "Сегментировать"))
        self.btn_sings.setText(_translate("MainWindow", "Расчет признаков"))
        self.histogram.setText(_translate("MainWindow", "Histogram"))
        self.segmented_image.setText(_translate("MainWindow", "segmented"))
        self.input_image.setText(_translate("MainWindow", "Input image"))

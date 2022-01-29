from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtGui import QPainter
from test5 import cases
import threading
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(900,500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(270, 230, 161, 41))
        self.pushButton.setStyleSheet(
                                      "QPushButton:hover {background-color: rgb(85, 200, 255);}"
                                      "QPushButton:pressed { background-color: rgb(85, 170, 255); }"
                                      "QPushButton{\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"    border:none;\n"
"    border-radius:17px;\n"
"    color: #FFF\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(300, 30, 86, 38))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"font: 25 22pt \"Microsoft YaHei Light\";\n"
"\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(55, 80, 800, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.move(40,110)
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 15pt \"Microsoft YaHei Light\";\n"
"\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"font: 25 15pt \"Microsoft YaHei Light\";\n"
"\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"font: 25 15pt \"Microsoft YaHei Light\";\n"
"\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"font: 25 15pt \"Microsoft YaHei Light\";\n"
"\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Microsoft YaHei Light\";\n"
"\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Microsoft YaHei Light\";\n"
"\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Microsoft YaHei Light\";\n"
"\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Microsoft YaHei Light\";\n"
"\n"
"border:none;\n"
"border-radius:15px;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
      #  self.label.setText(_translate("MainWindow", "CASES"))
        self.label.setText(_translate("MainWindow", "TRACKER"))
        self.label_3.setText(_translate("MainWindow", "Cases Across India"))
        self.label_2.setText(_translate("MainWindow", "Deaths"))
        self.label_5.setText(_translate("MainWindow", "Discharged"))
        self.label_4.setText(_translate("MainWindow", "Total Cases"))
        self.label_8.setText(_translate("MainWindow", "3,22,50,679"))
        self.label_9.setText(_translate("MainWindow", "3,69,846"))
        self.label_7.setText(_translate("MainWindow", "3,14,48,754"))
        self.label_6.setText(_translate("MainWindow", "4,32,079"))
        self.label.move(360,20)
        self.pushButton.move(360,350)
        self.label.adjustSize()
        self.label_2.adjustSize()
        self.label_3.adjustSize()
        self.label_4.adjustSize()
        self.label_5.adjustSize()
        self.label_6.adjustSize()
        self.label_7.adjustSize()
        self.label_8.adjustSize()
        self.label_9.adjustSize()

    def clicked(self):
    #    _translate = QtCore.QCoreApplication.translate
    #    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        case=cases()
        self.label_8.setText(case["Cases Across India"])
        self.label_9.setText(case["Total Cases "])
        self.label_7.setText(case["Discharged "])
        self.label_6.setText(case["Deaths"])


""" def thread(self):
        t1 = threading.Thread(target=self.clicked)
        t1.start()"""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

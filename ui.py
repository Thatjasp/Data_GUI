# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AIAA.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import pyqtgraph as pg
import time
from PyQt5 import QtCore, QtGui, QtWidgets

import serial
import numpy as np

NUMBER_GRAPHS = 3
# PORT_NAME = "COM1"
# BAUD_RATE = "9600"

# ser = serial.Serial(PORT_NAME, BAUD_RATE)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 877)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)

        # Central Window Policies
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")

        # Horizontal Layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Main Layout 
        self.vertical_main = QtWidgets.QHBoxLayout()
        self.vertical_main.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.vertical_main.setObjectName("vertical_main")

        # Raw Data Layout
        self.raw_data_layout = QtWidgets.QVBoxLayout()
        self.raw_data_layout.setObjectName("raw_data_layout")

        # Data Label Frame
        self.data_label_frame = QtWidgets.QFrame(self.centralwidget)
        self.data_label_frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.data_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_label_frame.setObjectName("data_label_frame")

        # Vertical Layout for Raw Data
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.data_label_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.raw_data_label = QtWidgets.QLabel(self.data_label_frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setKerning(True)

        # Raw Data Label
        self.raw_data_label.setFont(font)
        self.raw_data_label.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_data_label.setObjectName("raw_data_label")
        self.verticalLayout_3.addWidget(self.raw_data_label)
        self.raw_data_layout.addWidget(self.data_label_frame)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        # Raw Data Text Browser
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(100, 100))
        self.textBrowser.setMaximumSize(QtCore.QSize(1000, 1000))
        self.textBrowser.setObjectName("textBrowser")


        self.verticalLayout_5.addWidget(self.textBrowser)
        self.raw_data_layout.addLayout(self.verticalLayout_5)
        self.vertical_main.addLayout(self.raw_data_layout)
        self.current_val_layout = QtWidgets.QVBoxLayout()
        self.current_val_layout.setObjectName("current_val_layout")
        self.curr_val_label_frame = QtWidgets.QFrame(self.centralwidget)
        self.curr_val_label_frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.curr_val_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.curr_val_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.curr_val_label_frame.setObjectName("curr_val_label_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.curr_val_label_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.current_values_label = QtWidgets.QLabel(self.curr_val_label_frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setKerning(True)
        self.current_values_label.setFont(font)
        self.current_values_label.setScaledContents(True)
        self.current_values_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_values_label.setObjectName("current_values_label")
        self.horizontalLayout_3.addWidget(self.current_values_label)
        self.current_val_layout.addWidget(self.curr_val_label_frame)
        self.curr_val_section = QtWidgets.QVBoxLayout()
        self.curr_val_section.setObjectName("curr_val_section")
        self.val1_frame = QtWidgets.QFrame(self.centralwidget)
        self.val1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.val1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.val1_frame.setObjectName("val1_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.val1_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.curr_val1 = QtWidgets.QLabel(self.val1_frame)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.curr_val1.setFont(font)
        self.curr_val1.setObjectName("curr_val1")
        self.horizontalLayout_2.addWidget(self.curr_val1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.curr_val_section.addWidget(self.val1_frame)
        self.val2_frame = QtWidgets.QFrame(self.centralwidget)
        self.val2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.val2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.val2_frame.setObjectName("val2_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.val2_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.curr_val2 = QtWidgets.QLabel(self.val2_frame)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.curr_val2.setFont(font)
        self.curr_val2.setObjectName("curr_val2")
        self.horizontalLayout_4.addWidget(self.curr_val2, 0, QtCore.Qt.AlignHCenter)
        self.curr_val_section.addWidget(self.val2_frame)
        self.val4_frame = QtWidgets.QFrame(self.centralwidget)
        self.val4_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.val4_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.val4_frame.setObjectName("val4_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.val4_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.curr_val4 = QtWidgets.QLabel(self.val4_frame)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.curr_val4.setFont(font)
        self.curr_val4.setObjectName("curr_val4")
        self.horizontalLayout_5.addWidget(self.curr_val4, 0, QtCore.Qt.AlignHCenter)
        self.curr_val_section.addWidget(self.val4_frame)
        self.val3_frame = QtWidgets.QFrame(self.centralwidget)
        self.val3_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.val3_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.val3_frame.setObjectName("val3_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.val3_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.curr_val3 = QtWidgets.QLabel(self.val3_frame)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.curr_val3.setFont(font)
        self.curr_val3.setObjectName("curr_val3")
        self.horizontalLayout_6.addWidget(self.curr_val3, 0, QtCore.Qt.AlignHCenter)
        self.curr_val_section.addWidget(self.val3_frame)
        self.current_val_layout.addLayout(self.curr_val_section)
        self.vertical_main.addLayout(self.current_val_layout)
        self.graph_layout = QtWidgets.QVBoxLayout()
        self.graph_layout.setObjectName("graph_layout")
        self.graph_label_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_label_frame.sizePolicy().hasHeightForWidth())
        self.graph_label_frame.setSizePolicy(sizePolicy)
        self.graph_label_frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.graph_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_label_frame.setObjectName("graph_label_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.graph_label_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graph_label = QtWidgets.QLabel(self.graph_label_frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setKerning(True)
        self.graph_label.setFont(font)
        self.graph_label.setAlignment(QtCore.Qt.AlignCenter)
        self.graph_label.setObjectName("graph_label")
        self.verticalLayout_2.addWidget(self.graph_label)
        self.graph_layout.addWidget(self.graph_label_frame)
        self.graph_section = QtWidgets.QVBoxLayout()
        self.graph_section.setObjectName("graph_section")
        self.graph_layout.addLayout(self.graph_section)
        self.vertical_main.addLayout(self.graph_layout)
        self.horizontalLayout.addLayout(self.vertical_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 27))
        self.menubar.setObjectName("menubar")
        self.menuBruh = QtWidgets.QMenu(self.menubar)
        self.menuBruh.setObjectName("menuBruh")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuBruh.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.raw_data_label.setText(_translate("MainWindow", "Raw Data"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.current_values_label.setText(_translate("MainWindow", "Current Values"))
        self.curr_val1.setText(_translate("MainWindow", "Value 1: 100"))
        self.curr_val2.setText(_translate("MainWindow", "Value 2: 123.213"))
        self.curr_val4.setText(_translate("MainWindow", "Value 3: 100"))
        self.curr_val3.setText(_translate("MainWindow", "Value 4: 120"))
        self.graph_label.setText(_translate("MainWindow", "Graphs"))
        self.menuBruh.setTitle(_translate("MainWindow", "Bruh"))



# Creates A graph for the layout 
def createGraph(name):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    p = pg.PlotWidget()
    p.setSizePolicy(sizePolicy)
    sizePolicy.setHeightForWidth(p.sizePolicy().hasHeightForWidth())
    p.setMinimumSize(QtCore.QSize(100, 100))
    p.setMaximumSize(QtCore.QSize(1000, 1000))
    p.setObjectName(name)
    return p

# Rotates an array to the left
# and adds new value at the end
# of array
def rotateLeft(arr, newVal):
    if (np.size(arr) < 2):
        raise NameError("Size of Array Less than 2")
    for i in range(np.size(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = newVal


# NEED ARRAY AS I
i = [0,0,0]

# Updates the array, depending
# if the array is filled it will
# either rotate the array or 
# just put the new variable at
# index i.
def updateArr(arr, newVar, j):
    global i,timeArr
    np.size(arr)
    if i[j] > np.size(timeArr)-1:
        return rotateLeft(arr, newVar,)
    else:
        arr[i[j]] = newVar
        # THIS NEEDS TO BE CHANGED
        i[j] += 1

timeArr = np.arange(0, 50, 1)
infoArr = np.zeros((3,50))


def update(ui):
    global ptr, timeArr, infoArr, i
    f = open("testFile", "r")
    plots = []
    for graphs in range(NUMBER_GRAPHS):
        p = ui.graph_section.itemAt(graphs).widget()
        plots.append(p.plot(timeArr, infoArr[graphs]))

    for x in f:
        time.sleep(.2)
        txt = x.split()
        ui.textBrowser.append(x)

        for j in range(NUMBER_GRAPHS):
            plots[j].setData(timeArr, infoArr[j])
            # ui.current_val_layout.itemAt(0).widget().setText("Value 1: " + txt[0])
            ui.current_val_layout.itemAt(0).widget().children()
            arr = infoArr[j]
            updateArr(arr, int(txt[j]), j)

        rotateLeft(timeArr, timeArr[-1] + 1)

        QtGui.QGuiApplication.processEvents()
        

    
def secondStart(ui):

    for i in range(NUMBER_GRAPHS):
        p1 = createGraph("graph_" + str(i))
        p1.setLabel('left', 'Data')
        p1.setLabel('bottom', 'Time')
        ui.graph_section.addWidget(p1)
    
    # p2 = createGraph("graph_2")
    # p3 = createGraph("graph_3")


    # ui.graph_section.addWidget(p2)
    # ui.graph_section.addWidget(p3)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    secondStart(ui)
    MainWindow.show()
    update(ui)
    sys.exit(app.exec_())

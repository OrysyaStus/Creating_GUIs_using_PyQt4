# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_6.28.2016.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setIconSize(QtCore.QSize(26, 26))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tutorial = QtGui.QPushButton(self.centralwidget)
        self.tutorial.setGeometry(QtCore.QRect(40, 300, 331, 211))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tutorial.setFont(font)
        self.tutorial.setObjectName(_fromUtf8("tutorial"))
        self.get_started = QtGui.QPushButton(self.centralwidget)
        self.get_started.setGeometry(QtCore.QRect(420, 300, 331, 211))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.get_started.setFont(font)
        self.get_started.setObjectName(_fromUtf8("get_started"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 70, 611, 101))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.welcome_label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName(_fromUtf8("welcome_label"))
        self.verticalLayout_4.addWidget(self.welcome_label)
        self.welcome_label1 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.welcome_label1.setFont(font)
        self.welcome_label1.setObjectName(_fromUtf8("welcome_label1"))
        self.verticalLayout_4.addWidget(self.welcome_label1)
        self.icon = QtGui.QPushButton(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(40, 80, 121, 91))
        self.icon.setObjectName(_fromUtf8("icon"))
        self.icon.raise_()
        self.tutorial.raise_()
        self.get_started.raise_()
        self.verticalLayoutWidget.raise_()
        self.icon.raise_()
        self.welcome_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionHome = QtGui.QAction(MainWindow)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionSaved_Data = QtGui.QAction(MainWindow)
        self.actionSaved_Data.setObjectName(_fromUtf8("actionSaved_Data"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionProQinase_Cell_Lines = QtGui.QAction(MainWindow)
        self.actionProQinase_Cell_Lines.setObjectName(_fromUtf8("actionProQinase_Cell_Lines"))
        self.actionReference_Cell_Lines = QtGui.QAction(MainWindow)
        self.actionReference_Cell_Lines.setObjectName(_fromUtf8("actionReference_Cell_Lines"))
        self.actionPharmacogenomic_Data = QtGui.QAction(MainWindow)
        self.actionPharmacogenomic_Data.setObjectName(_fromUtf8("actionPharmacogenomic_Data"))
        self.actionPathway_Analysis = QtGui.QAction(MainWindow)
        self.actionPathway_Analysis.setObjectName(_fromUtf8("actionPathway_Analysis"))
        self.actionBs = QtGui.QAction(MainWindow)
        self.actionBs.setObjectName(_fromUtf8("actionBs"))
        self.actionProQinase = QtGui.QAction(MainWindow)
        self.actionProQinase.setObjectName(_fromUtf8("actionProQinase"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tutorial.setText(_translate("MainWindow", "Tutorial", None))
        self.get_started.setText(_translate("MainWindow", "Let\'s Get Started", None))
        self.welcome_label.setText(_translate("MainWindow", "Welcome to the ProQinase Cell Line Explorer.", None))
        self.welcome_label1.setText(_translate("MainWindow", "Use this tool to discover novel information for targeting cancer.", None))
        self.icon.setText(_translate("MainWindow", "PushButton", None))
        self.actionHome.setText(_translate("MainWindow", "Home", None))
        self.actionSaved_Data.setText(_translate("MainWindow", "Saved Data", None))
        self.actionExport.setText(_translate("MainWindow", "Export", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionProQinase_Cell_Lines.setText(_translate("MainWindow", "ProQinase Cell Lines", None))
        self.actionReference_Cell_Lines.setText(_translate("MainWindow", "Reference Cell Lines", None))
        self.actionPharmacogenomic_Data.setText(_translate("MainWindow", "Pharmacogenomic Data", None))
        self.actionPathway_Analysis.setText(_translate("MainWindow", "Pathway Analysis", None))
        self.actionBs.setText(_translate("MainWindow", "bs", None))
        self.actionProQinase.setText(_translate("MainWindow", "ProQinase", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


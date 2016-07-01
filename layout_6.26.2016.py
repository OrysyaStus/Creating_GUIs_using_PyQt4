# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_6.26.2016.ui'
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
        MainWindow.resize(799, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 220, 281, 181))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 220, 281, 181))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 531, 78))
        self.label.setObjectName(_fromUtf8("label"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 811, 591))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHome = QtGui.QMenu(self.menubar)
        self.menuHome.setObjectName(_fromUtf8("menuHome"))
        self.menuProQinase_Cell_Lines = QtGui.QMenu(self.menubar)
        self.menuProQinase_Cell_Lines.setObjectName(_fromUtf8("menuProQinase_Cell_Lines"))
        self.menuReference_Cell_Lines = QtGui.QMenu(self.menubar)
        self.menuReference_Cell_Lines.setObjectName(_fromUtf8("menuReference_Cell_Lines"))
        self.menuContact = QtGui.QMenu(self.menubar)
        self.menuContact.setObjectName(_fromUtf8("menuContact"))
        self.menuExport = QtGui.QMenu(self.menubar)
        self.menuExport.setObjectName(_fromUtf8("menuExport"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionA = QtGui.QAction(MainWindow)
        self.actionA.setObjectName(_fromUtf8("actionA"))
        self.actionExplorer = QtGui.QAction(MainWindow)
        self.actionExplorer.setObjectName(_fromUtf8("actionExplorer"))
        self.actionSaved = QtGui.QAction(MainWindow)
        self.actionSaved.setObjectName(_fromUtf8("actionSaved"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionExplorer_2 = QtGui.QAction(MainWindow)
        self.actionExplorer_2.setObjectName(_fromUtf8("actionExplorer_2"))
        self.actionSaved_2 = QtGui.QAction(MainWindow)
        self.actionSaved_2.setObjectName(_fromUtf8("actionSaved_2"))
        self.actionExport_2 = QtGui.QAction(MainWindow)
        self.actionExport_2.setObjectName(_fromUtf8("actionExport_2"))
        self.actionExplorer_3 = QtGui.QAction(MainWindow)
        self.actionExplorer_3.setObjectName(_fromUtf8("actionExplorer_3"))
        self.actionSaved_3 = QtGui.QAction(MainWindow)
        self.actionSaved_3.setObjectName(_fromUtf8("actionSaved_3"))
        self.actionExport_3 = QtGui.QAction(MainWindow)
        self.actionExport_3.setObjectName(_fromUtf8("actionExport_3"))
        self.actionExplorer_4 = QtGui.QAction(MainWindow)
        self.actionExplorer_4.setObjectName(_fromUtf8("actionExplorer_4"))
        self.actionSaved_4 = QtGui.QAction(MainWindow)
        self.actionSaved_4.setObjectName(_fromUtf8("actionSaved_4"))
        self.actionExport_4 = QtGui.QAction(MainWindow)
        self.actionExport_4.setObjectName(_fromUtf8("actionExport_4"))
        self.actionPathway_Analysis = QtGui.QAction(MainWindow)
        self.actionPathway_Analysis.setObjectName(_fromUtf8("actionPathway_Analysis"))
        self.menuProQinase_Cell_Lines.addAction(self.actionExplorer)
        self.menuProQinase_Cell_Lines.addAction(self.actionSaved)
        self.menuProQinase_Cell_Lines.addAction(self.actionExport)
        self.menuProQinase_Cell_Lines.addAction(self.actionPathway_Analysis)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuProQinase_Cell_Lines.menuAction())
        self.menubar.addAction(self.menuReference_Cell_Lines.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuContact.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Tutorial", None))
        self.pushButton_2.setText(_translate("MainWindow", "Let\'s Begin", None))
        self.label.setText(_translate("MainWindow", "Welcome to the ProQinase Cell Line Explorer. Use this tool to discover novel information for targeting cancer.  ", None))
        self.menuHome.setTitle(_translate("MainWindow", "Home", None))
        self.menuProQinase_Cell_Lines.setTitle(_translate("MainWindow", "Explorer", None))
        self.menuReference_Cell_Lines.setTitle(_translate("MainWindow", "Saved", None))
        self.menuContact.setTitle(_translate("MainWindow", "Contact", None))
        self.menuExport.setTitle(_translate("MainWindow", "Export", None))
        self.actionA.setText(_translate("MainWindow", "A", None))
        self.actionExplorer.setText(_translate("MainWindow", "ProQinase Cell Lines", None))
        self.actionSaved.setText(_translate("MainWindow", "Reference Cell Lines", None))
        self.actionExport.setText(_translate("MainWindow", "Pharmacological Data", None))
        self.actionExplorer_2.setText(_translate("MainWindow", "Explorer", None))
        self.actionSaved_2.setText(_translate("MainWindow", "Saved", None))
        self.actionExport_2.setText(_translate("MainWindow", "Export", None))
        self.actionExplorer_3.setText(_translate("MainWindow", "Explorer", None))
        self.actionSaved_3.setText(_translate("MainWindow", "Saved", None))
        self.actionExport_3.setText(_translate("MainWindow", "Export", None))
        self.actionExplorer_4.setText(_translate("MainWindow", "Explorer", None))
        self.actionSaved_4.setText(_translate("MainWindow", "Saved", None))
        self.actionExport_4.setText(_translate("MainWindow", "Export", None))
        self.actionPathway_Analysis.setText(_translate("MainWindow", "Pathway Analysis", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


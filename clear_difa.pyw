<<<<<<< HEAD
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clear_difa.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(-20, 560, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.clear_command = QtWidgets.QPushButton(Dialog)
        self.clear_command.setGeometry(QtCore.QRect(110, 290, 111, 23))
        self.clear_command.setObjectName("clear_command")
        self.keep_command = QtWidgets.QPushButton(Dialog)
        self.keep_command.setGeometry(QtCore.QRect(246, 290, 111, 23))
        self.keep_command.setObjectName("keep_command")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 451, 261))
        self.groupBox.setObjectName("groupBox")
        self.base_view = QtWidgets.QTableWidget(self.groupBox)
        self.base_view.setGeometry(QtCore.QRect(10, 91, 421, 161))
        self.base_view.setColumnCount(2)
        self.base_view.setObjectName("base_view")
        self.base_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.base_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.base_view.setHorizontalHeaderItem(1, item)
        self.sn_filter = QtWidgets.QLineEdit(self.groupBox)
        self.sn_filter.setGeometry(QtCore.QRect(80, 50, 113, 20))
        self.sn_filter.setObjectName("sn_filter")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.search = QtWidgets.QPushButton(self.groupBox)
        self.search.setGeometry(QtCore.QRect(200, 50, 75, 23))
        self.search.setObjectName("search")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 310, 451, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cleared_view = QtWidgets.QTableWidget(self.groupBox_2)
        self.cleared_view.setGeometry(QtCore.QRect(10, 30, 421, 192))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cleared_view.setFont(font)
        self.cleared_view.setColumnCount(2)
        self.cleared_view.setObjectName("cleared_view")
        self.cleared_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cleared_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cleared_view.setHorizontalHeaderItem(1, item)
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.buttonBox.raise_()
        self.clear_command.raise_()
        self.keep_command.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Clear DIFA"))
        self.clear_command.setText(_translate("Dialog", "Clear from DIFA"))
        self.keep_command.setText(_translate("Dialog", "Keep for DIFA"))
        self.groupBox.setTitle(_translate("Dialog", "Equipment pending DIFA"))
        item = self.base_view.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Description"))
        item = self.base_view.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Serial No"))
        self.label.setText(_translate("Dialog", "Filter by sn"))
        self.search.setText(_translate("Dialog", "Search"))
        self.groupBox_2.setTitle(_translate("Dialog", "Cleared Equipment"))
        item = self.cleared_view.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Description"))
        item = self.cleared_view.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Serial No"))


import icons_rc
=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clear_difa.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(-20, 560, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.clear_command = QtWidgets.QPushButton(Dialog)
        self.clear_command.setGeometry(QtCore.QRect(110, 290, 111, 23))
        self.clear_command.setObjectName("clear_command")
        self.keep_command = QtWidgets.QPushButton(Dialog)
        self.keep_command.setGeometry(QtCore.QRect(246, 290, 111, 23))
        self.keep_command.setObjectName("keep_command")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 451, 261))
        self.groupBox.setObjectName("groupBox")
        self.base_view = QtWidgets.QTableWidget(self.groupBox)
        self.base_view.setGeometry(QtCore.QRect(10, 91, 421, 161))
        self.base_view.setColumnCount(2)
        self.base_view.setObjectName("base_view")
        self.base_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.base_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.base_view.setHorizontalHeaderItem(1, item)
        self.sn_filter = QtWidgets.QLineEdit(self.groupBox)
        self.sn_filter.setGeometry(QtCore.QRect(80, 50, 113, 20))
        self.sn_filter.setObjectName("sn_filter")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.search = QtWidgets.QPushButton(self.groupBox)
        self.search.setGeometry(QtCore.QRect(200, 50, 75, 23))
        self.search.setObjectName("search")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 310, 451, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cleared_view = QtWidgets.QTableWidget(self.groupBox_2)
        self.cleared_view.setGeometry(QtCore.QRect(10, 30, 421, 192))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cleared_view.setFont(font)
        self.cleared_view.setColumnCount(2)
        self.cleared_view.setObjectName("cleared_view")
        self.cleared_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cleared_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cleared_view.setHorizontalHeaderItem(1, item)
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.buttonBox.raise_()
        self.clear_command.raise_()
        self.keep_command.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Clear DIFA"))
        self.clear_command.setText(_translate("Dialog", "Clear from DIFA"))
        self.keep_command.setText(_translate("Dialog", "Keep for DIFA"))
        self.groupBox.setTitle(_translate("Dialog", "Equipment pending DIFA"))
        item = self.base_view.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Description"))
        item = self.base_view.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Serial No"))
        self.label.setText(_translate("Dialog", "Filter by sn"))
        self.search.setText(_translate("Dialog", "Search"))
        self.groupBox_2.setTitle(_translate("Dialog", "Cleared Equipment"))
        item = self.cleared_view.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Description"))
        item = self.cleared_view.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Serial No"))


import icons_rc
>>>>>>> Branch

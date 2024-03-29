# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Return_wo.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(627, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/newIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.return_command = QtWidgets.QPushButton(Dialog)
        self.return_command.setGeometry(QtCore.QRect(220, 290, 75, 23))
        self.return_command.setObjectName("return_command")
        self.remove_command = QtWidgets.QPushButton(Dialog)
        self.remove_command.setGeometry(QtCore.QRect(320, 290, 75, 23))
        self.remove_command.setObjectName("remove_command")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 591, 261))
        self.groupBox.setObjectName("groupBox")
        self.base_select = QtWidgets.QComboBox(self.groupBox)
        self.base_select.setGeometry(QtCore.QRect(10, 30, 251, 22))
        self.base_select.setObjectName("base_select")
        self.base_select.addItem("")
        self.base_select.addItem("")
        self.base_view = QtWidgets.QTableWidget(self.groupBox)
        self.base_view.setGeometry(QtCore.QRect(10, 91, 571, 161))
        self.base_view.setColumnCount(2)
        self.base_view.setObjectName("base_view")
        self.base_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.base_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.base_view.setHorizontalHeaderItem(1, item)
        self.sn_filter = QtWidgets.QLineEdit(self.groupBox)
        self.sn_filter.setGeometry(QtCore.QRect(360, 30, 113, 20))
        self.sn_filter.setObjectName("sn_filter")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(290, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(480, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.return_date = QtWidgets.QDateEdit(self.groupBox)
        self.return_date.setGeometry(QtCore.QRect(360, 60, 110, 22))
        self.return_date.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.return_date.setCalendarPopup(True)
        self.return_date.setDate(QtCore.QDate.currentDate())
        self.return_date.setObjectName("return_date")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(290, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 310, 591, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.return_view = QtWidgets.QTableWidget(self.groupBox_2)
        self.return_view.setGeometry(QtCore.QRect(10, 30, 571, 192))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.return_view.setFont(font)
        self.return_view.setColumnCount(5)
        self.return_view.setObjectName("return_view")
        self.return_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.return_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.return_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.return_view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.return_view.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.return_view.setHorizontalHeaderItem(4, item)
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.buttonBox.raise_()
        self.return_command.raise_()
        self.remove_command.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Return Equipment"))
        self.return_command.setText(_translate("Dialog", "Return"))
        self.remove_command.setText(_translate("Dialog", "Remove"))
        self.groupBox.setTitle(_translate("Dialog", "Move from"))
        self.base_select.setItemText(0, _translate("Dialog", "Lekhwair"))
        self.base_select.setItemText(1, _translate("Dialog", "Nimr"))
        item = self.base_view.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Description"))
        item = self.base_view.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Serial No"))
        self.label.setText(_translate("Dialog", "Filter by sn"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.return_date.setDisplayFormat(_translate("Dialog", "dd-MMM-yyyy"))
        self.label_2.setText(_translate("Dialog", "Return Date"))
        self.groupBox_2.setTitle(_translate("Dialog", "Return to Sohar"))
        item = self.return_view.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Description"))
        item = self.return_view.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Serial No"))
        item = self.return_view.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Quantity"))
        item = self.return_view.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Condition"))
        item = self.return_view.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Well name"))


import icons_rc

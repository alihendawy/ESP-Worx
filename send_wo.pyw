# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_wo.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(326, 96)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.send_date = QtWidgets.QDateEdit(Dialog)
        self.send_date.setGeometry(QtCore.QRect(50, 30, 131, 22))
        self.send_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.send_date.setCalendarPopup(True)
        self.send_date.setObjectName("send_date")
        self.send_date.setDate(QtCore.QDate.currentDate())
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(12, 32, 23, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Enter sending date"))
        self.send_date.setDisplayFormat(_translate("Dialog", "dd-MMM-yyyy"))
        self.label.setText(_translate("Dialog", "Date"))


import icons_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cable_scrap.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(293, 273)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-120, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 30, 211, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 50, 47, 21))
        self.label.setObjectName("label")
        self.reelno = QtWidgets.QLineEdit(self.frame)
        self.reelno.setGeometry(QtCore.QRect(60, 50, 113, 20))
        self.reelno.setObjectName("reelno")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 47, 21))
        self.label_2.setObjectName("label_2")
        self.qty = QtWidgets.QLineEdit(self.frame)
        self.qty.setGeometry(QtCore.QRect(60, 90, 113, 20))
        self.qty.setObjectName("qty")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 47, 21))
        self.label_3.setObjectName("label_3")
        self.date = QtWidgets.QDateEdit(self.frame)
        self.date.setGeometry(QtCore.QRect(60, 10, 110, 22))
        self.date.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.date.setCalendarPopup(True)
        self.date.setObjectName("date")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 47, 21))
        self.label_4.setObjectName("label_4")
        self.armor = QtWidgets.QComboBox(self.frame)
        self.armor.setGeometry(QtCore.QRect(60, 130, 111, 22))
        self.armor.setObjectName("armor")
        self.armor.addItem("")
        self.armor.addItem("")
        self.armor.addItem("")
        self.armor.addItem("")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Scrap Cable"))
        self.label.setText(_translate("Dialog", "Reel no"))
        self.label_2.setText(_translate("Dialog", "Length"))
        self.label_3.setText(_translate("Dialog", "Date"))
        self.label_4.setText(_translate("Dialog", "arm/cond"))
        self.armor.setItemText(0, _translate("Dialog", "Galv New"))
        self.armor.setItemText(1, _translate("Dialog", "Galv Used"))
        self.armor.setItemText(2, _translate("Dialog", "SS New"))
        self.armor.setItemText(3, _translate("Dialog", "SS Used"))



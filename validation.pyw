# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'validation.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(265, 156)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-120, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label.setObjectName("label")
        self.pn_input = QtWidgets.QLineEdit(Dialog)
        self.pn_input.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.pn_input.setObjectName("pn_input")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Validate Item"))
        self.label.setText(_translate("Dialog", "Part Number"))
        self.pn_input.setToolTip(_translate("Dialog", "Input PN for item to validate store count"))
        self.label_2.setText(_translate("Dialog", "Validate DH equipment count"))



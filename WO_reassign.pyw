# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WO_reassign.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(303, 195)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/newIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-120, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 261, 121))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 47, 16))
        self.label_3.setObjectName("label_3")
        self.base = QtWidgets.QComboBox(self.groupBox)
        self.base.setGeometry(QtCore.QRect(80, 80, 111, 22))
        self.base.setObjectName("base")
        self.base.addItem("")
        self.base.addItem("")
        self.fromWell = QtWidgets.QLabel(self.groupBox)
        self.fromWell.setGeometry(QtCore.QRect(80, 20, 111, 21))
        self.fromWell.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.fromWell.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fromWell.setLineWidth(2)
        self.fromWell.setText("")
        self.fromWell.setObjectName("fromWell")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 47, 16))
        self.label_2.setObjectName("label_2")
        self.toWell = QtWidgets.QLineEdit(self.groupBox)
        self.toWell.setGeometry(QtCore.QRect(80, 50, 113, 20))
        self.toWell.setObjectName("toWell")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Reassign Workorder"))
        self.groupBox.setToolTip(_translate("Dialog", "Reassign workorder to another well"))
        self.groupBox.setTitle(_translate("Dialog", "Reassign Workorder"))
        self.label_3.setText(_translate("Dialog", "Base"))
        self.base.setItemText(0, _translate("Dialog", "Lekhwair"))
        self.base.setItemText(1, _translate("Dialog", "Nimr"))
        self.label_2.setText(_translate("Dialog", "To"))
        self.label.setText(_translate("Dialog", "From"))


import icons_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minStore_dlg2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(231, 213)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-150, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 181, 111))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(40, 70, 121, 17))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 113, 20))
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Check Min store"))
        self.groupBox.setTitle(_translate("Dialog", "Check single item/entire store"))
        self.checkBox.setText(_translate("Dialog", "Check entire Store"))
        self.label.setText(_translate("Dialog", "PN:"))
        self.lineEdit.setToolTip(_translate("Dialog", "If checkbox is selected, no PN is required."))


import icons_rc

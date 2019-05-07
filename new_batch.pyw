# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_batch.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 157)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(280, 60, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(22, 72, 45, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(22, 100, 34, 16))
        self.label_2.setObjectName("label_2")
        self.batchDate = QtWidgets.QDateEdit(Dialog)
        self.batchDate.setGeometry(QtCore.QRect(90, 100, 121, 20))
        self.batchDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.batchDate.setCalendarPopup(True)
        self.batchDate.setObjectName("batchDate")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setObjectName("label_3")
        self.batchFile = QtWidgets.QLabel(Dialog)
        self.batchFile.setGeometry(QtCore.QRect(90, 70, 121, 21))
        self.batchFile.setFrameShape(QtWidgets.QFrame.Panel)
        self.batchFile.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.batchFile.setLineWidth(2)
        self.batchFile.setText("")
        self.batchFile.setObjectName("batchFile")
        self.loadFile = QtWidgets.QToolButton(Dialog)
        self.loadFile.setGeometry(QtCore.QRect(220, 70, 25, 19))
        self.loadFile.setObjectName("loadFile")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Load new Equipment Batch"))
        self.label.setText(_translate("Dialog", "File name"))
        self.label_2.setText(_translate("Dialog", "Date in"))
        self.batchDate.setDisplayFormat(_translate("Dialog", "dd-MMM-yyyy"))
        self.label_3.setText(_translate("Dialog", "New Equipment Batch"))
        self.loadFile.setText(_translate("Dialog", "..."))


import icons_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reel_update.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(244, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-140, 360, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 60, 201, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.SN1 = QtWidgets.QLineEdit(self.frame)
        self.SN1.setGeometry(QtCore.QRect(70, 110, 113, 20))
        self.SN1.setObjectName("SN1")
        self.SN2 = QtWidgets.QLineEdit(self.frame)
        self.SN2.setGeometry(QtCore.QRect(70, 150, 113, 20))
        self.SN2.setObjectName("SN2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 47, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 47, 16))
        self.label_3.setObjectName("label_3")
        self.length = QtWidgets.QSpinBox(self.frame)
        self.length.setGeometry(QtCore.QRect(70, 70, 111, 22))
        self.length.setMaximum(5000)
        self.length.setSingleStep(300)
        self.length.setObjectName("length")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 47, 16))
        self.label_4.setObjectName("label_4")
        self.arm_cond = QtWidgets.QComboBox(self.frame)
        self.arm_cond.setGeometry(QtCore.QRect(70, 230, 111, 22))
        self.arm_cond.setObjectName("arm_cond")
        self.arm_cond.addItem("")
        self.arm_cond.addItem("")
        self.arm_cond.addItem("")
        self.arm_cond.addItem("")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 51, 16))
        self.label_5.setObjectName("label_5")
        self.well = QtWidgets.QLineEdit(self.frame)
        self.well.setGeometry(QtCore.QRect(70, 190, 113, 20))
        self.well.setObjectName("well")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 47, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.label_7.setObjectName("label_7")
        self.date = QtWidgets.QDateEdit(self.frame)
        self.date.setGeometry(QtCore.QRect(70, 30, 110, 22))
        self.date.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.date.setCalendarPopup(True)
        self.date.setTimeSpec(QtCore.Qt.TimeZone)
        self.date.setObjectName("date")
        self.date.setDate(QtCore.QDate.currentDate())

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update Cable Reel"))
        self.label.setText(_translate("Dialog", "Update cable Reel"))
        self.label_2.setText(_translate("Dialog", "To Reel"))
        self.label_3.setText(_translate("Dialog", "From Reel"))
        self.label_4.setText(_translate("Dialog", "Length"))
        self.arm_cond.setItemText(0, _translate("Dialog", "Galv New"))
        self.arm_cond.setItemText(1, _translate("Dialog", "Galv Used"))
        self.arm_cond.setItemText(2, _translate("Dialog", "SS New"))
        self.arm_cond.setItemText(3, _translate("Dialog", "SS Used"))
        self.label_5.setText(_translate("Dialog", "Arm/cond"))
        self.label_6.setText(_translate("Dialog", "Well"))
        self.label_7.setText(_translate("Dialog", "Date"))


import icons_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WO_edit.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(467, 182)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(31, 41, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 51, 16))
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(320, 20, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 91, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sn_option = QtWidgets.QRadioButton(self.layoutWidget)
        self.sn_option.setCheckable(True)
        self.sn_option.setChecked(False)
        self.sn_option.setObjectName("sn_option")
        self.verticalLayout.addWidget(self.sn_option)
        self.pn_option = QtWidgets.QRadioButton(self.layoutWidget)
        self.pn_option.setCheckable(True)
        self.pn_option.setObjectName("pn_option")
        self.verticalLayout.addWidget(self.pn_option)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 281, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.id_input = QtWidgets.QLineEdit(self.frame_2)
        self.id_input.setGeometry(QtCore.QRect(70, 20, 111, 20))
        self.id_input.setObjectName("id_input")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(210, 10, 47, 13))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(210, 30, 51, 22))
        self.spinBox.setMaximum(5000)
        self.spinBox.setObjectName("spinBox")
        self.date_input = QtWidgets.QDateEdit(self.frame_2)
        self.date_input.setGeometry(QtCore.QRect(70, 60, 110, 22))
        self.date_input.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_input.setCalendarPopup(True)
        self.date_input.setObjectName("date_input")
        self.date_input.setDate(QtCore.QDate.currentDate())
        self.frame_2.raise_()
        self.frame.raise_()
        self.buttonBox.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit Workorder"))
        self.label.setText(_translate("Dialog", "ID (SN/PN)"))
        self.label_2.setText(_translate("Dialog", "Date"))
        self.sn_option.setText(_translate("Dialog", "Serial Number"))
        self.pn_option.setText(_translate("Dialog", "Part Number"))
        self.label_3.setText(_translate("Dialog", "ID type"))
        self.label_4.setText(_translate("Dialog", "Qty"))
        self.date_input.setDisplayFormat(_translate("Dialog", "dd-MMM-yyyy"))


import icons_rc

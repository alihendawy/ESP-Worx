# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minStore_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(451, 296)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 421, 261))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.add_pn = QtWidgets.QPushButton(self.groupBox)
        self.add_pn.setGeometry(QtCore.QRect(200, 100, 75, 23))
        self.add_pn.setObjectName("add_pn")
        self.pn_input = QtWidgets.QLineEdit(self.groupBox)
        self.pn_input.setGeometry(QtCore.QRect(200, 70, 113, 20))
        self.pn_input.setObjectName("pn_input")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(200, 50, 71, 16))
        self.label_6.setObjectName("label_6")
        self.min_qty = QtWidgets.QSpinBox(self.groupBox)
        self.min_qty.setGeometry(QtCore.QRect(330, 70, 61, 22))
        self.min_qty.setMaximum(10000)
        self.min_qty.setProperty("value", 1)
        self.min_qty.setObjectName("min_qty")
        self.sub_pn = QtWidgets.QPushButton(self.groupBox)
        self.sub_pn.setGeometry(QtCore.QRect(200, 130, 75, 23))
        self.sub_pn.setToolTipDuration(-1)
        self.sub_pn.setObjectName("sub_pn")
        self.pn_table = QtWidgets.QTableWidget(self.groupBox)
        self.pn_table.setGeometry(QtCore.QRect(10, 40, 171, 192))
        self.pn_table.setColumnCount(4)
        self.pn_table.setObjectName("pn_table")
        self.pn_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.pn_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pn_table.setHorizontalHeaderItem(1, item)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(330, 50, 47, 13))
        self.label_7.setObjectName("label_7")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create Min Store"))
        self.groupBox.setTitle(_translate("Dialog", "Create Minimum Store"))
        self.add_pn.setToolTip(_translate("Dialog", "Add Item"))
        self.add_pn.setText(_translate("Dialog", "<-----"))
        self.label_6.setText(_translate("Dialog", "Part Number"))
        self.sub_pn.setToolTip(_translate("Dialog", "Remove Item"))
        self.sub_pn.setText(_translate("Dialog", "----->"))
        item = self.pn_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Part Number"))
        item = self.pn_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "QTY"))
        self.label_7.setText(_translate("Dialog", "Min qty"))


import icons_rc

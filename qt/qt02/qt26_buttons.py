# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt26_buttons.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(765, 666)
        Form.setBaseSize(QtCore.QSize(777, 777))
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(470, 10, 131, 631))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Abort|QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ignore|QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.NoToAll|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Open|QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.RestoreDefaults|QtWidgets.QDialogButtonBox.Retry|QtWidgets.QDialogButtonBox.Save|QtWidgets.QDialogButtonBox.SaveAll|QtWidgets.QDialogButtonBox.Yes|QtWidgets.QDialogButtonBox.YesToAll)
        self.buttonBox.setObjectName("buttonBox")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(20, 210, 141, 41))
        self.toolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton.setAutoRaise(False)
        self.toolButton.setObjectName("toolButton")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(210, 200, 222, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 270, 181, 28))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 141, 171))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(True)
        self.groupBox.setObjectName("groupBox")
        self.cb4 = QtWidgets.QCheckBox(self.groupBox)
        self.cb4.setGeometry(QtCore.QRect(50, 130, 91, 19))
        self.cb4.setCheckable(True)
        self.cb4.setChecked(False)
        self.cb4.setTristate(False)
        self.cb4.setObjectName("cb4")
        self.cb3 = QtWidgets.QCheckBox(self.groupBox)
        self.cb3.setGeometry(QtCore.QRect(50, 100, 91, 19))
        self.cb3.setCheckable(True)
        self.cb3.setChecked(False)
        self.cb3.setTristate(False)
        self.cb3.setObjectName("cb3")
        self.cb2 = QtWidgets.QCheckBox(self.groupBox)
        self.cb2.setGeometry(QtCore.QRect(50, 70, 91, 19))
        self.cb2.setCheckable(True)
        self.cb2.setChecked(False)
        self.cb2.setTristate(False)
        self.cb2.setObjectName("cb2")
        self.cb1 = QtWidgets.QCheckBox(self.groupBox)
        self.cb1.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.cb1.setCheckable(True)
        self.cb1.setChecked(False)
        self.cb1.setTristate(False)
        self.cb1.setObjectName("cb1")
        self.rb_hc1 = QtWidgets.QRadioButton(Form)
        self.rb_hc1.setGeometry(QtCore.QRect(350, 20, 115, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Warning.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rb_hc1.setIcon(icon)
        self.rb_hc1.setObjectName("rb_hc1")
        self.rb_hc2 = QtWidgets.QRadioButton(Form)
        self.rb_hc2.setGeometry(QtCore.QRect(350, 50, 115, 31))
        self.rb_hc2.setObjectName("rb_hc2")
        self.rb_hc3 = QtWidgets.QRadioButton(Form)
        self.rb_hc3.setGeometry(QtCore.QRect(350, 80, 115, 31))
        self.rb_hc3.setObjectName("rb_hc3")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 20, 141, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rb3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb3.setGeometry(QtCore.QRect(30, 80, 115, 31))
        self.rb3.setAutoExclusive(False)
        self.rb3.setObjectName("rb3")
        self.rb2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb2.setGeometry(QtCore.QRect(30, 50, 115, 31))
        self.rb2.setAutoExclusive(False)
        self.rb2.setObjectName("rb2")
        self.rb1 = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb1.setGeometry(QtCore.QRect(30, 20, 115, 31))
        self.rb1.setAutoExclusive(False)
        self.rb1.setObjectName("rb1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "..."))
        self.commandLinkButton.setText(_translate("Form", "打开百度"))
        self.commandLinkButton.setDescription(_translate("Form", "www.baidu.com"))
        self.pushButton.setText(_translate("Form", "PushButton", "123"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.cb4.setText(_translate("Form", "分支三"))
        self.cb3.setText(_translate("Form", "分支二"))
        self.cb2.setText(_translate("Form", "分支一"))
        self.cb1.setText(_translate("Form", "总控"))
        self.rb_hc1.setText(_translate("Form", "互斥一"))
        self.rb_hc2.setText(_translate("Form", "互斥二"))
        self.rb_hc3.setText(_translate("Form", "互斥三"))
        self.groupBox_2.setTitle(_translate("Form", "GroupBox"))
        self.rb3.setText(_translate("Form", "选择3"))
        self.rb2.setText(_translate("Form", "选择2"))
        self.rb1.setText(_translate("Form", "选择1(&A)"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qlist.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 376)
        self.list1 = QtWidgets.QListWidget(Form)
        self.list1.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.list1.setObjectName("list1")
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        self.list2 = QtWidgets.QListWidget(Form)
        self.list2.setGeometry(QtCore.QRect(280, 10, 256, 192))
        self.list2.setObjectName("list2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 220, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(370, 230, 111, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.list1.isSortingEnabled()
        self.list1.setSortingEnabled(False)
        item = self.list1.item(0)
        item.setText(_translate("Form", "Virat Kohli"))
        item = self.list1.item(1)
        item.setText(_translate("Form", "Shikhar Dhawan"))
        item = self.list1.item(2)
        item.setText(_translate("Form", "M.Shami"))
        item = self.list1.item(3)
        item.setText(_translate("Form", "D Bravo"))
        item = self.list1.item(4)
        item.setText(_translate("Form", "Gayle"))
        item = self.list1.item(5)
        item.setText(_translate("Form", "Bhubhneshwar Kumar"))
        item = self.list1.item(6)
        item.setText(_translate("Form", "Sachin tendulkar"))
        item = self.list1.item(7)
        item.setText(_translate("Form", "MS Dhoni"))
        self.list1.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "Player\'s Name"))
        self.label_2.setText(_translate("Form", "Selected Players"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

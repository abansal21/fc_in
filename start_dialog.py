# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from aux import *
import sys
class Ui_Form():
    def setupUi(self, Form):
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.pushButton.clicked.connect(self.show_new_dialog) 
        self.pushButton_2.clicked.connect(self.show_open_dialog) 
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        move_to_center(self.form)
        
        set_shortcut(self.form, 'Ctrl+N', self.show_new_dialog)
        set_shortcut(self.form, 'Ctrl+O', self.show_open_dialog)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "New Team"))
        self.pushButton_2.setText(_translate("Form", "Open Team"))
    
    def show_new_dialog(self):
        import get_team_name
        
        self.window = QtWidgets.QWidget()
        self.ui = get_team_name.Ui_get_team_name(self.form)
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        
        
    def show_open_dialog(self):
        import open_team
        self.window = QtWidgets.QWidget()
        self.ui = open_team.Ui_Form(self.form)
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_team_name.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from aux import *
class Ui_get_team_name(object):
    def __init__(self, parent):
        self.parent = parent
        
    def setupUi(self, Form):
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(Form)
        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(self.rejected)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        move_to_center(self.form)
        self.lineEdit.returnPressed.connect(self.accepted)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Team Name: "))
        
        
    def rejected(self):
        self.form.close()
        self.parent.show()
    def accepted(self):
        # do team
        self.parent.close()
        self.team = self.lineEdit.text()
        if self.team != '':
            self.show_main()
        else:
            show_alert('Please Enter a Team Name.')
    
    def show_main(self):
        import final
        self.window = QtWidgets.QMainWindow()
        self.ui = final.Ui_MainWindow(self.form)
        self.ui.setupUi(self.window)
        self.ui.initialize(self.team)
        self.form.close()
        self.window.show()
        

def main(name = sys.argv):
    app = QtWidgets.QApplication(name)
    print(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_get_team_name()
    ui.setupUi(Form)
    return Form
    Form.show()
    #sys.exit(app.exec_())
if __name__ == "__main__":
    main()
    



from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from aux import *
import sqlite3

class Ui_Form(object):
    def __init__(self, parent = None):
        self.parent = parent
    def setupUi(self, Form):
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(400, 242)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(Form)
        
        add_teams_to_combo(self.comboBox)
        
        self.buttonBox.rejected.connect(self.rejected)
        self.buttonBox.accepted.connect(self.accepted)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        move_to_center(self.form)

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
        self.team = self.comboBox.currentText()
        
        self.form.close()
        self.show_main()
        
    
    def show_main(self):
        import final
        self.window = QtWidgets.QMainWindow()
        self.ui = final.Ui_MainWindow(self.form)
        self.ui.setupUi(self.window)
        self.ui.open_team(self.team)
        self.form.close()
        self.window.show()
    
def main(name = sys.argv):
    app = QtWidgets.QApplication(name)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    


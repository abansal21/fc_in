# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from qcheckcombobox import CheckComboBox
class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 564)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cb_team = QtWidgets.QComboBox(Form)
        self.cb_team.setObjectName("cb_team")
        self.horizontalLayout_2.addWidget(self.cb_team)
        
        self.cb_match = CheckComboBox(Form, placeholderText = 'Select')
        self.model = self.cb_match.model()
        self.cb_match.setObjectName("cb_match")
        self.cb_match.addItem("Match1")
        self.model.item(0).setCheckable(True)
        self.cb_match.addItem("Match2")
        self.model.item(1).setCheckable(True)
        self.cb_match.addItem("Match3")
        self.model.item(2).setCheckable(False)
        
        self.horizontalLayout_2.addWidget(self.cb_match)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lb_pts = QtWidgets.QLabel(Form)
        self.lb_pts.setStyleSheet("color:rgb(85, 85, 255)")
        self.lb_pts.setObjectName("lb_pts")
        self.horizontalLayout_5.addWidget(self.lb_pts)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lw_players = QtWidgets.QListWidget(Form)
        self.lw_players.setObjectName("lw_players")
        self.horizontalLayout.addWidget(self.lw_players)
        self.lw_poins = QtWidgets.QListWidget(Form)
        self.lw_poins.setStyleSheet("color:rgb(85, 85, 255);")
        #self.lw_poins.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lw_poins.setObjectName("lw_poins")
        self.horizontalLayout.addWidget(self.lw_poins)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pb1 = QtWidgets.QPushButton(Form)
        self.pb1.setObjectName("pb1")
        self.horizontalLayout_3.addWidget(self.pb1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Evaluate the Performance of your Fantasy Team"))

        self.label_2.setText(_translate("Form", "Players"))
        self.label_3.setText(_translate("Form", "Points"))
        self.lb_pts.setText(_translate("Form", "####"))
        self.pb1.setText(_translate("Form", "Calculate Score"))
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


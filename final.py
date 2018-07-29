# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from aux import *
import sqlite3
import message_box
dbname = 'cricket.db'

class Ui_MainWindow(object):
    def __init__(self, parent=None):
        self.parent = parent
        self.selected_players = {}
        self.details = {}
        self.wk = False
        self.team_name = None
        self.total_value = 0
        
        
    def setupUi(self, MainWindow):
        self.form = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 600)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.verticalFrame)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lb_bat = QtWidgets.QLabel(self.verticalFrame)
        self.lb_bat.setStyleSheet("color:rgb(85, 85, 255)")
        self.lb_bat.setObjectName("lb_bat")
        self.horizontalLayout_4.addWidget(self.lb_bat)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_8 = QtWidgets.QLabel(self.verticalFrame)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lb_bwl = QtWidgets.QLabel(self.verticalFrame)
        self.lb_bwl.setStyleSheet("color:rgb(85, 85, 255)")
        self.lb_bwl.setObjectName("lb_bwl")
        self.horizontalLayout_4.addWidget(self.lb_bwl)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_7 = QtWidgets.QLabel(self.verticalFrame)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.lb_ar = QtWidgets.QLabel(self.verticalFrame)
        self.lb_ar.setStyleSheet("color:rgb(85, 85, 255)")
        self.lb_ar.setObjectName("lb_ar")
        self.horizontalLayout_4.addWidget(self.lb_ar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.label_5 = QtWidgets.QLabel(self.verticalFrame)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lb_wk = QtWidgets.QLabel(self.verticalFrame)
        self.lb_wk.setStyleSheet("color:rgb(85, 85, 255)")
        self.lb_wk.setObjectName("lb_wk")
        self.horizontalLayout_4.addWidget(self.lb_wk)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addWidget(self.verticalFrame, 0, 1, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.lb_availpts = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lb_availpts.setFont(font)
        self.lb_availpts.setStyleSheet("color:rgb(85, 85, 255)")
        self.lb_availpts.setObjectName("lb_availpts")
        self.horizontalLayout.addWidget(self.lb_availpts)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rb_bat = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_bat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rb_bat.setObjectName("rb_bat")
        self.horizontalLayout_3.addWidget(self.rb_bat)
        self.rb_bwl = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_bwl.setObjectName("rb_bwl")
        self.horizontalLayout_3.addWidget(self.rb_bwl)
        self.rb_ar = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_ar.setObjectName("rb_ar")
        self.horizontalLayout_3.addWidget(self.rb_ar)
        self.rb_wk = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_wk.setObjectName("rb_wk")
        
        self.rb_bat.toggled.connect(self.checkstate)
        self.rb_bwl.toggled.connect(self.checkstate)
        self.rb_ar.toggled.connect(self.checkstate)
        self.rb_wk.toggled.connect(self.checkstate)

        self.horizontalLayout_3.addWidget(self.rb_wk)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.lw_avail = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setKerning(False)
        self.lw_avail.setFont(font)
        self.lw_avail.setStyleSheet("")
        self.lw_avail.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lw_avail.setLineWidth(0)
        self.lw_avail.setObjectName("lw_avail")
        
        self.lw_avail.itemDoubleClicked.connect(self.move_to_selected)

        
        item = QtWidgets.QListWidgetItem()
        self.lw_avail.addItem(item)
        self.verticalLayout_4.addWidget(self.lw_avail)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(100, 0))
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.lb_usedpts = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lb_usedpts.setFont(font)
        self.lb_usedpts.setStyleSheet("color:rgb(85, 85, 255)")
        self.lb_usedpts.setObjectName("lb_usedpts")
        self.horizontalLayout_2.addWidget(self.lb_usedpts)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalFrame_4 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame_4.setObjectName("horizontalFrame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.horizontalFrame_4)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.lb_teamname = QtWidgets.QLabel(self.horizontalFrame_4)
        self.lb_teamname.setStyleSheet("color:rgb(85, 85, 255)")
        self.lb_teamname.setObjectName("lb_teamname")
        self.horizontalLayout_5.addWidget(self.lb_teamname)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_5.addWidget(self.horizontalFrame_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lw_selected = QtWidgets.QListWidget(self.centralwidget)
        self.lw_selected.setObjectName("lw_selected")
        
        self.lw_selected.itemDoubleClicked.connect(self.move_to_avail)

        
        self.verticalLayout_5.addWidget(self.lw_selected)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 2, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 39))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.menubar.triggered[QtWidgets.QAction].connect(self.menufunction)
        
        move_to_center(self.form)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_2.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.lb_bat.setText(_translate("MainWindow", "##"))
        self.label_8.setText(_translate("MainWindow", "Bowleres (BOW)"))
        self.lb_bwl.setText(_translate("MainWindow", "##"))
        self.label_7.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.lb_ar.setText(_translate("MainWindow", "##"))
        self.label_5.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.lb_wk.setText(_translate("MainWindow", "##"))
        self.label_13.setText(_translate("MainWindow", "Points Available  "))
        self.lb_availpts.setText(_translate("MainWindow", "####"))
        self.rb_bat.setText(_translate("MainWindow", "BAT"))
        self.rb_bwl.setText(_translate("MainWindow", "BOW"))
        self.rb_ar.setText(_translate("MainWindow", "AR"))
        self.rb_wk.setText(_translate("MainWindow", "W&K"))
        __sortingEnabled = self.lw_avail.isSortingEnabled()
        self.lw_avail.setSortingEnabled(False)
        item = self.lw_avail.item(0)
        item.setText(_translate("MainWindow", "Select a category form above."))
        self.lw_avail.setSortingEnabled(__sortingEnabled)
        self.label_14.setText(_translate("MainWindow", ">"))
        self.label_10.setText(_translate("MainWindow", "Points Used   "))
        self.lb_usedpts.setText(_translate("MainWindow", "####"))
        self.label_15.setText(_translate("MainWindow", "Team Name"))
        self.lb_teamname.setText(_translate("MainWindow", "Displayed Here"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "&NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "&OPEN Team"))
        self.actionOPEN_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "&SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "&EVALUATE Team"))
        self.actionEVALUATE_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))

    def checkstate(self):
        role = self.get_checkstate()
        
        self.fill_avail_list("where ctg = '{}'".format(role))
    def get_checkstate(self):
        if self.rb_bat.isChecked():
            return 'BAT'
        elif self.rb_bwl.isChecked():
            return 'BWL'
        elif self.rb_ar.isChecked():
            return 'AR'
        else:#self.rb_wk.isChecked()
            return 'WK'
    
    def fill_avail_list(self, condition = '', tbname = 'stats'):
        conn = sqlite3.connect(dbname)
        qry = 'select player from {} {};'.format(tbname, condition)
        cur = transaction(conn, qry)
        l = list(map(lambda x:x[0], cur.fetchall()))
        self.lw_avail.clear()
        for name in l:
            if name not in self.selected_players.keys():
                self.lw_avail.addItem(name)
        
    def initialize(self, team_name):
        self.team_name = team_name
        self.lb_bat.setText('0')
        self.lb_bwl.setText('0')
        self.lb_ar.setText('0')
        self.lb_wk.setText('0')
        self.lb_usedpts.setText('0')
        self.lb_availpts.setText('1000')
        self.lb_teamname.setText(team_name)
        self.fetch_player_values()
    
    
    
    def fetch_player_values(self):
        qry = 'select player, value, ctg  from stats'
        cr = execute_qry(qry)
    
        if cr is not None:
            for name, value, role in cr.fetchall():
                self.details.setdefault(name, {})['value'] = int(value)
                self.details.setdefault(name, {})['role'] = role
                    
                
        print(self.details)
    def open_team(self, team_name):
        self.initialize(team_name)
        qry = 'select players, value from teams where name = ?'
        cr = execute_qry(qry, [team_name])
        self.lb_teamname.setText(team_name)
        if cr is not None:
            players, value = cr.fetchone()
            bats = 0
            bwls = 0
            wks = 0
            ars = 0
            print(type(eval(players)))
            for k, v in eval(players).items():
                self.lw_selected.addItem('{} ({})'.format(k, v['role']))
                self.selected_players[k] = v
                if v['role'] == 'BAT':
                    bats += 1
                elif v['role'] == 'BWL':
                    bwls += 1
                elif v['role'] == 'AR':
                    ars += 1
                elif v['role'] == 'WK':
                    wks += 1
                    self.wk = True
            print(self.selected_players)
            self.lb_usedpts.setText(str(value))
            self.lb_ar.setText(str(ars))
            self.lb_bat.setText(str(bats))
            self.lb_bwl.setText(str(bwls))
            self.lb_wk.setText(str(wks))
            self.lb_availpts.setText(str(1000- value))
            
        else:
            pass
            # the team is not found
    
    def move_to_selected(self, item):
        try:
            value = self.details[item.text()]['value']
        except KeyError:
            return
        try:
            if int(self.lb_availpts.text()) < value:
                raise Exception('Not Enough Points Available!')
            
            if self.get_checkstate() == 'WK':
                if self.wk == True:
                    raise Exception("You can't select more than one wicket-keeper.")
                self.wk = True
        
            self.lw_avail.takeItem(self.lw_avail.row(item))
            self.lw_selected.addItem('{} ({})'.format(item.text(), self.get_checkstate()))
            self.selected_players[item.text()] = self.details[item.text()]
            
            eval("self.lb_{0}.setText(str(int(self.lb_{0}.text()) + 1))".format(self.get_checkstate().lower()))

            self.lb_availpts.setText(str(int(self.lb_availpts.text()) - value))
            self.lb_usedpts.setText(str(int(self.lb_usedpts.text()) + value))
            self.total_value += value
        except Exception as e:
            print(e)
            #show dialog that not enough points available
            show_alert(str(e))
            return
        
        print(self.selected_players)
        
    
    def move_to_avail(self, item):
        self.lw_selected.takeItem(self.lw_selected.row(item))
        if self.get_checkstate() == 'WK':
            self.wk = False
        name, brac_role = item.text().split()
        role = brac_role[1:-1]
        if self.get_checkstate() == role:
            self.lw_avail.addItem(name)
        
        self.selected_players.pop(name)
        print(self.selected_players)
        
        value = self.details[name]['value']
        
        eval("self.lb_{0}.setText(str(int(self.lb_{0}.text()) - 1))".format(role.lower()))

        self.lb_availpts.setText(str(int(self.lb_availpts.text()) + value))
        self.lb_usedpts.setText(str(int(self.lb_usedpts.text()) - value))
        self.total_value -= value
        
    def menufunction(self, action):
        import start_dialog
        txt = (action.text())
        print(txt)
        if txt == '&NEW Team':
            self.show_new_dialog()
        
        elif txt == '&OPEN Team':
            self.show_open_dialog()
        elif txt == '&SAVE Team':
            self.save_team()
        elif txt == '&EVALUATE Team':
            self.show_eval()
        
    def show_new_dialog(self):
        import get_team_name
        self.window = QtWidgets.QWidget()
        self.ui = get_team_name.Ui_get_team_name(self.form)
        self.ui.setupUi(self.window)
        self.window.show()
        
        
    def show_open_dialog(self):
        import open_team
        self.window = QtWidgets.QWidget()
        self.ui = open_team.Ui_Form(self.form)
        self.ui.setupUi(self.window)
        self.window.show()
        
    def show_eval(self):
        import evaluate_wrapper
        self.ui = evaluate_wrapper.EvaluateWrapper(self.form)
        self.ui.show()
        
    def save_team(self):
        if len(self.selected_players.keys()) != 11:
            show_alert('A team must have exactly 11 players.')
            return
        if not self.wk:
            show_alert('A team must have one Wicket-Keeper.')
            return
        qry = 'insert into teams(name, players, value) values(?, ?, ?);'
        cr = execute_qry(qry, [self.team_name, str(self.selected_players), self.total_value])
        if cr == INTEGRITY_FAILED:
        
            box = message_box.MessageBox('Team Already Exists.\n Replace !?.')
            result = box.show()
            if result:
                # replace
                qry = 'delete from teams where name = ?'
                execute_qry(qry, [self.team_name])
                return self.save_team()
            else:
                return
            
        if cr is not None:
            show_alert('Saved.')
        else:
            show_alert('Invalid Values Supplied!')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


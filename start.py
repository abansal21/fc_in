import start_dialog, open_team, get_team_name, final
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Start_Ui(start_dialog.Ui_Form):
    def __init__(self, parent = None):
        self.parent = parent
    def setupUi(self, Form):
        self.form = Form
        super.setupUi(self.form)
        self.pushButton.clicked.connect(self.show_new_dialog) 
        self.pushButton_2.clicked.connect(self.show_open_dialog) 

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

class Start:
    def show_widget(self, ui):
        self.window = QtWidgets.QWidget()
        self.ui = ui
        self.ui.setupUi(self.window)
        self.window.show()
        return self.window

    def show_main_win(self, ui):
        self.window = QtWidgets.QMainWindow()
        self.ui = ui
        self.ui.setupUi(self.window)
       # self.ui.open_team(self.team)
        self.window.show()
        return self.window

    def show_start_dialog(self):
        app = QtWidgets.QApplication(sys.argv)
        self.cur_form = start_dialog(Start_Ui())
        sys.exit(app.exec_())

    def show_final(self):
        self.cur_form.close()
        self.cur_form = show_main_win(final.Ui_MainWindow(self.cur_form))

def main():
    s = Start()
    s.show_start_dialog()
if __name__ == "__main__":
    main()
    

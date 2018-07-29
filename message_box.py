import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from aux import move_to_center
 
class MessageBox(QWidget):
 
    def __init__(self, st):
        super().__init__()
        self.title = 'messagebox'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.st =st
 
    def show(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        move_to_center(self)
        buttonReply = QMessageBox.question(self, 'message', self.st, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            return True
        else:
            return False
 
        self.close()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MessageBox('hi')
    res = ex.show()
    print(res)
    sys.exit()

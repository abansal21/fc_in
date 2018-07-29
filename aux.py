from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3
dbname = 'cricket.db'
INTEGRITY_FAILED = 'INTEGRITY FAILED'
def transaction(connection, query, datatup = None):
    cur = connection.cursor()
    try:
        if datatup is None:
            cur.execute(query)
        else:
            cur.execute(query, datatup)
        connection.commit()
    except sqlite3.IntegrityError:
        return INTEGRITY_FAILED
    except Exception as e:
        connection.rollback()
        print(e)
        #print('Unable to complete Transaction.')
        return None
    # end of Transaction
    return cur

def get_confirmation(s = "?"):
    flg = input("{} (y/n): ".format(s)).lower()
    if flg == 'y' or flg == '':
        return True
    return False

def get_int(s):
    while(True):
        try:
            value = int(input(s))
        except ValueError:
            print('Try Again..\n')
        else:
            break
    return value

def show_alert(msg):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setText(msg)
    msgBox.exec_()
    
def move_to_center(form):
    qtRectangle = form.frameGeometry()
    centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    form.move(qtRectangle.topLeft())
    
def execute_qry(qry, datatup = None):
    conn = sqlite3.connect(dbname)
    return transaction(conn, qry, datatup)
    
def add_teams_to_combo(combo):
    qry = 'select name from teams;'
    cr = execute_qry(qry)
    names = list(map(lambda x:x[0], cr.fetchall()))
    for name in names:
        combo.addItem(name)

def set_shortcut(widget, shortcut_str, func):
    widget.shortcut = QShortcut(QKeySequence(shortcut_str), widget)
    widget.shortcut.activated.connect(func)

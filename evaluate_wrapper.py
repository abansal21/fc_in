import evaluate
from aux import *
from ev_funcs import *
from collections import namedtuple

class EvaluateWrapper(evaluate.Ui_Form):
    def __init__(self, parent = None):
        self.parent = parent
        self.players = None
        self.details = {}
        
        
    def setupUi(self, Form):
        super(EvaluateWrapper, self).setupUi(Form)
        self.form = Form
        
        self.populate()
        self.pb1.clicked.connect(self.evalu)
        self.cb_team.currentIndexChanged.connect(self.add_players)
        move_to_center(self.form)
        
    def populate(self):
        self.cb_team.addItem('<Select One>')
        add_teams_to_combo(self.cb_team)
    
    def add_players(self, index):
        self.lw_players.clear()
        self.lw_poins.clear()
        self.lb_pts.setText('####')
        if index == 0:
            return
        txt = self.cb_team.itemText(index)
        qry = 'select players from teams where name = ?'
        cr = execute_qry(qry, [txt])
        if cr is not None:
            self.players = eval(cr.fetchone()[0])
            for player in self.players.keys():
                self.lw_players.addItem(player)
            
    def iterAllItems(self, lw):
        for i in range(lw.count()):
            yield lw.item(i).text()
        
    def evalu(self):
        self.lw_poins.clear()
        pts = 0
        team = self.cb_team.currentText()
        checks = self.cb_match.checkedIndices()

        match = list(map(lambda x:self.cb_match.itemText(x), checks))
        print(match)
        lw_pts_lis = []
        Player = namedtuple('Player', "name runs balls fours sixes ballsGiven runsGiven wkts catches stumps ro".split())
        for i in range(len(match)):
            lw_pts_lis.append([])
            qry = "select player, scored, faced, fours, sixes, balls, given, wkts, catches, stumping, ro from {};".format(match[i])
            cr = execute_qry(qry)
            if cr is not None:
                for playerdet in cr.fetchall():
                    
                    pl = Player(*playerdet)
                    s = "{{'runs':{}, '4':{}, '6':{}, 'balls':{}, 'overs':{}, 'field':{}, 'wkts':{}, 'runsGiven':{}}}".format(pl.runs, pl.fours, pl.sixes, pl.balls, pl.ballsGiven/6, pl.catches + pl.stumps + pl.ro, pl.wkts, pl.runsGiven)
                    self.details[pl.name] = eval(s)
                print(self.details)
            else:
                show_alert('Invalid.')
                return
        
            for name in self.iterAllItems(self.lw_players):
                p = self.details[name]
                res = total_points(p)
                pts += res
                lw_pts_lis[i].append(res)
       
        lw_pts_lis = [sum(x) for x in zip(*lw_pts_lis)]
        try:
            for pt in lw_pts_lis:
                self.lw_poins.addItem(str(pt//len(match)))
            self.lb_pts.setText(str(pts//len(match)))
        except ZeroDivisionError:
            self.lb_pts.setText('####')
            self.lw_poins.clear()
            show_alert('No Players')
        
        
    def show(self):
        self.window = QtWidgets.QWidget()
        self.setupUi(self.window)
        self.window.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = EvaluateWrapper()
    ui.show()
    sys.exit(app.exec_())
        

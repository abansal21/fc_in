# p's format p = {'name':None, 'runs':0, '4':0, '6':0, 'balls':0, 'overs':0, 'field':0, 'wkts':0, 'runsGiven':0}
def batting_points(p):
    runs = p['runs']
    points = 0
    if runs > 0:
        strike_rate = runs/p['balls']
    
        # 1 point for 2 runs scored
        points = runs//2
        
        # additional 5 points for half century
        if runs >= 50:
            points += 5
        
        # additional 10 points for century
        if runs >= 100:
            points += 10
        
        if strike_rate >= 80 and strike_rate <= 100:
            points += 2
        elif strike_rate > 100:
            points += 4
        
    points += (p['4'] + 2*p['6'])
    
    return points

def bowling_points(p):
    # 10 points for each wicket
    points = 10 * p['wkts']
    
    # additional 5 points for 3 wickets per innings
    if p['wkts'] >= 3:
        points += 5
    
    # Additional 10 points for 5 wickets or more
    if p['wkts'] >= 5:
        points += 10
    try:
        ec_rate = p['runsGiven']/p['overs']
        if ec_rate >= 3.5 and ec_rate <= 4.5:
            points += 4
        elif ec_rate >= 2 and ec_rate < 3.5:
            points += 7
        elif ec_rate < 2 and ec_rate > 0:
            points += 10
    except ZeroDivisionError:
        pass
    
    return points

def fielding_points(p):
    # fielding points
    return 10* p['field']

def total_points(p):
    return batting_points(p) + bowling_points(p) + fielding_points(p)

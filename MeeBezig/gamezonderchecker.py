import random
from chqngesforfulllooper import ispossible
allestukken = [101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,110,110,111,112,112,113,113,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,413,413,0,0,0,0,0,0,0,0]
stukkenoverinpot = allestukken.copy()
stukkeninspelershand = []
stukkenopveld = []
def gameplaycalculator(lijstinput,spelernummer):
    global stukkenoverinpot
    global stukkeninspelershand
    global stukkenopveld
    stukkenindezespelerzijnhand = stukkeninspelershand[spelernummer].copy()
    oldhand = stukkenindezespelerzijnhand.copy()
    if not lijstinput:
        o = random.choice(stukkenoverinpot)
        stukkenoverinpot.remove(o)
        stukkeninspelershand[spelernummer] = stukkenindezespelerzijnhand.append(o)
        return True
    else:
        for i in lijstinput:
            if i in stukkenindezespelerzijnhand:
                stukkenindezespelerzijnhand.remove(i)
            else:
                stukkeninspelershand[spelernummer] =oldhand
                return False
        gelegdestukken = stukkenopveld + lijstinput
        mogelijk, pad = ispossible(gelegdestukken)
        if mogelijk:
            stukkeninspelershand[spelernummer] = sorted(stukkenindezespelerzijnhand)
            stukkenopveld = gelegdestukken.copy()
            return True
        else:
            stukkeninspelershand[spelernummer] = oldhand
            return False
def setupgame(aantalspelers):
    global stukkeninspelershand
    for i in range(aantalspelers):
        tempspeler = []
        for w in range(14):
            stukinjouwhand = random.choice(stukkenoverinpot)
            stukkenoverinpot.remove(stukinjouwhand)
            tempspeler.append(stukinjouwhand)
        stukkeninspelershand.append(sorted(tempspeler))



def gameplayloop():
    z = input("aantal spelers")
    z = int(z)
    setupgame(z)
    completed = False
    while not completed:
        spelers = 0
        while spelers < z:
            print(stukkeninspelershand[spelers])
            x =  input("stukken leggen deze beurt")
            x = x.translate({ord(c): None for c in '[]'}).split(',')
            print(x)
            xints = [int(i) for i in x if i.isnumeric()]
            print(xints)
            doorgaan = gameplaycalculator(xints,spelers)
            if not doorgaan: spelers-=1
            spelers +=1


gameplayloop()
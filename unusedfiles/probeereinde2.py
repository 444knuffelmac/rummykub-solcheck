from finished import listallrowsfunctry, funcnodigprobeinde

def mogelijkepaden(pad,rows,beginrows):
    maybepos = [] #beginindex is juist, rest niet gechecked
    confirmedpos = [] # alles is gechecked en is correct, dus deze kunnen
    if pad[0] in beginrows:
        i=0
        while i < len(beginrows):
            if beginrows[i] == pad[0]:
                maybepos.append(rows[i])
            i+=1
        for i in maybepos:
            k=0
            stopped = False
            while k < len(i):
                if i[k] in pad:
                    k+=1
                    continue
                stopped = True
                break
            if not stopped:
                confirmedpos.append(i)
    return confirmedpos
def getmogelijkepaden(currentpad,threetileros,fourtileros,fivetileros,beginthreeti,beginfourti,beginfiveti):
    #currentpad = de lijst van overgebleven nummers in dit pad
    allpossiblerows = [] #alle mogelijke rijen, niet op basis van hoeveelheid
    rows3mog = mogelijkepaden(currentpad,threetileros,beginthreeti)
    rows4mog = mogelijkepaden(currentpad,fourtileros,beginfourti)
    rows5mog = mogelijkepaden(currentpad,fivetileros,beginfiveti)
    for i in rows5mog:
        allpossiblerows.append(i)
    for i in rows4mog:
        allpossiblerows.append(i)
    for i in rows3mog:
        allpossiblerows.append(i)
    return rows3mog,rows4mog,rows5mog,allpossiblerows

#oplossing --> de volgorde van hoe diep ze gaan, van diepst naar dichts, dit ook returnen
def finalcalculatorrecursive(piececolnumb):
    if not piececolnumb:
        return True,[]

    jokers = listallrowsfunctry.jokercount(piececolnumb)
    uniquenumbers = listallrowsfunctry.onlyuniquenumbers(piececolnumb)
    n, o = listallrowsfunctry.whatvalueshaveneighboursbothtypes(uniquenumbers)
    neighbourlessnumbers = listallrowsfunctry.neighbourless(uniquenumbers, n, o)
    stillpos = listallrowsfunctry.firstfilter(neighbourlessnumbers, uniquenumbers)
    if not stillpos:
        return False,[]
    farneighbours = listallrowsfunctry.extendedneighbours(uniquenumbers, jokers, neighbourlessnumbers)
    stillpos =listallrowsfunctry.secondfilter(neighbourlessnumbers,farneighbours,jokers)
    if not stillpos:
        return False,[]
    threetilerow = listallrowsfunctry.makeallthreetilerows(uniquenumbers, jokers)
    stillpos = listallrowsfunctry.thirthfilter(uniquenumbers, threetilerow)
    if not stillpos:
        return False,[]
    fourtilerow = listallrowsfunctry.makeallfourtilerows(uniquenumbers, jokers)
    fivetilerow = listallrowsfunctry.makeallfivetilerows(uniquenumbers, jokers)
    threetilerowbegin = funcnodigprobeinde.beginswith(threetilerow)
    fourtilerowbegin = funcnodigprobeinde.beginswith(fourtilerow)
    fivetilerowbegin = funcnodigprobeinde.beginswith(fivetilerow)
    oplossing =[]
    if not piececolnumb:
        return True,[]
    a,b,c,mogelijkpaden = getmogelijkepaden(piececolnumb,threetilerow,fourtilerow,fivetilerow,threetilerowbegin,fourtilerowbegin,fivetilerowbegin)
    possible = False
    print(mogelijkpaden)
    print(len(mogelijkpaden))
    for i in mogelijkpaden:
        smallersize = piececolnumb.copy()
        for l in i:
            smallersize.remove(l)
        print(smallersize)
        possible,oplossing = finalcalculatorrecursive(smallersize)
        if possible:
            oplossing.append(i)
            break
    return possible,oplossing


#piecescolornumber = [101,102,103,104,105,105,106,107,108]
#piecescolornumber = [0,101,102,103,104,105,105,106,108]
#piecescolornumber = [109,110,110,111,112,112,113,113,104,310]
stresstest = [101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,109,110,110,111,112,112,113,113,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,413,413,0,0,0,0,0,0,0,0]
piecescolornumber = stresstest
#piecescolornumber = [101,201,301]
print(finalcalculatorrecursive(piecescolornumber))
'''posrow3,posrow4,posrow5,allposrows = getmogelijkepaden(piecescolornumber,threetilerow,fourtilerow,fivetilerow,threetilerowbegin,fourtilerowbegin,fivetilerowbegin)
print("three tile rows")
print(posrow3)
print(threetilerow)
print("four tile rows")
print(posrow4)
print(fourtilerow)
print("five tile rows")
print(posrow5)
print(fivetilerow)
print("allrows")
print(allposrows)'''
import time
import shelve
from otherfunctionsdeont import *
from itertools import combinations,chain
#from memory_profiler import profile


def allpossiblecombinations2(numbers):
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(numbers)
    return list(chain.from_iterable(set(combinations(s, r+2)) for r in range(len(s)-2)))
#@profile

def finalcalculatorrecursive(piececolnumb, memory):
    if not piececolnumb: del piececolnumb; return True, []
    if str(piececolnumb) in memory:
        m = memory[str(piececolnumb)]
        del piececolnumb
        return m[0], m[1]
    jokers = piececolnumb.count(0)

    if jokers == len(piececolnumb):
        returnvalue = [0]*jokers
        del jokers
        memory[str(piececolnumb)] = [True, returnvalue]
        del piececolnumb
        return True, returnvalue

    uniquenumbers = sorted(list(set(piececolnumb)))
    neighbourlessnumbers = whatvalueshaveneighboursbothtypes(uniquenumbers)
    if  not jokers and (len(neighbourlessnumbers) > 0):
        del neighbourlessnumbers, jokers, uniquenumbers
        memory[str(piececolnumb)] = [False, []]
        del piececolnumb
        return False, []

    if not secondfilter(neighbourlessnumbers, jokers, uniquenumbers):
        del neighbourlessnumbers,jokers,uniquenumbers
        memory[str(piececolnumb)] = [False, []]
        del piececolnumb
        return False, []
    del neighbourlessnumbers
    alltilerows,threetilerows = makeallrowsnofunc(uniquenumbers, jokers)
    del jokers

    if not filterzoveel(uniquenumbers, threetilerows):
        del uniquenumbers,alltilerows
        memory[str(piececolnumb)] = [False, []]
        del piececolnumb
        return False, []
    mogelijkpaden = mogelijkepaden(uniquenumbers, alltilerows)
    del alltilerows, uniquenumbers
    possible,oplossing = False,[]

    for i in mogelijkpaden:
        smallersize = piececolnumb.copy()

        for l in i: smallersize.remove(l)
        possible, oplossing = finalcalculatorrecursive(smallersize, memory)
        del smallersize

        if possible:
            oplossing.append(i)
            memory[str(piececolnumb)] = [possible, oplossing.copy()]
            del piececolnumb
            break
    return possible, oplossing




with shelve.open('e') as memoryd:
    memoryd.clear()
    piecescolornumber = [101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,110,110,111,112,112,113,113,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,413,413,0,0,0,0,0,0,0,0]
    #piecescolornumber = [101,101,201,301,301,401,401]
    #piecescolornumber = [0,0,0]
    start = time.time()
    x = finalcalculatorrecursive(piecescolornumber,memoryd)
    end = time.time()
    print(end-start)
    """start = time.time()
    for _ in range(100):
        finalcalculatorrecursive(piecescolornumber,memoryd)
        finalcalculatorrecursive(piecescolornumber,memoryd)
        y = finalcalculatorrecursive(piecescolornumber,memoryd)
    end = time.time()
    print(end-start)"""
    #for key, value in memoryd.items() :
    #    print (key, value)
    print(x)
    #print(y)
    #print(finalcalculatorrecursive([0,0,0],memoryd))
    """piecescolornumber = [101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,109,110,110,111,111,112,112,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,413,0]
    start = time.time()
    x = finalcalculatorrecursive(piecescolornumber,memoryd)
    end = time.time()
    print(end-start)
    print(x)"""
    #print(finalcalculatorrecursive([101,102,104],memoryd))


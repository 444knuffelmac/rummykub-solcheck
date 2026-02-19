import time
import shelve
from otherfunctionsdeont import *
from itertools import combinations,chain
#from memory_profiler import profile
import cProfile

def allpossiblecombinations2(numbers):
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    return list(chain.from_iterable(set(combinations(numbers, r+2)) for r in range(len(numbers)-2)))
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
        memory[str(piececolnumb)] = [True, returnvalue]
        return True, returnvalue

    uniquenumbers = sorted(list(set(piececolnumb)))
    neighbourlessnumbers = whatvalueshaveneighboursbothtypes(uniquenumbers)
    if  not jokers and (len(neighbourlessnumbers) > 0):
        memory[str(piececolnumb)] = [False, []]
        return False, []

    if not secondfilter(neighbourlessnumbers, jokers, uniquenumbers):
        del neighbourlessnumbers,jokers,uniquenumbers
        memory[str(piececolnumb)] = [False, []]
        return False, []
    possiblerows = possiblewithrows(uniquenumbers, jokers)
    if not possiblerows:
        memory[str(piececolnumb)] = [False, []]
        return False, []

    possible,oplossing = False,[]

    for i in possiblerows:
        smallersize = piececolnumb.copy()

        for l in i: smallersize.remove(l)
        possible, oplossing = finalcalculatorrecursive(smallersize, memory)
        del smallersize

        if possible:
            oplossing.append(i)
            memory[str(piececolnumb)] = [possible, oplossing.copy()]
            break
    return possible, oplossing


def ispossible(piececolnumb):
    with shelve.open('e') as memoryd:
        return finalcalculatorrecursive(piececolnumb, memoryd)
piecescolornumber = [101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,110,110,111,112,112,113,113,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,413,413]

with shelve.open('e') as memoryd:
    memoryd.clear()
    start = time.time()
    cProfile.run('finalcalculatorrecursive(piecescolornumber, memoryd)')
    end = time.time()
    print(end - start)
    print(ispossible(piecescolornumber))
    start = time.time()
    cProfile.run('finalcalculatorrecursive(piecescolornumber, memoryd)')
    end = time.time()
    print(end - start)
#cProfile.run('ispossible(piecescolornumber)')



#piecescolornumber = [101,101,201,301,301,401,401]
#piecescolornumber = [0,0,0]
"""
x = finalcalculatorrecursive(piecescolornumber,memoryd)
"""
"""start = time.time()
for _ in range(100):
    finalcalculatorrecursive(piecescolornumber,memoryd)
    finalcalculatorrecursive(piecescolornumber,memoryd)
    y = finalcalculatorrecursive(piecescolornumber,memoryd)
end = time.time()
print(end-start)"""
#for key, value in memoryd.items() :
#    print (key, value)
#print(x)
#print(y)
#print(finalcalculatorrecursive([0,0,0],memoryd))
"""piecescolornumber = [101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,109,110,110,111,111,112,112,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,413,0]
start = time.time()
x = finalcalculatorrecursive(piecescolornumber,memoryd)
end = time.time()
print(end-start)
print(x)"""
#print(finalcalculatorrecursive([101,102,104],memoryd))
import time
#from finished import listallrowsfunctry
from itertools import combinations,chain
"""def allpossiblecombinations(numbers):
    uniquenumbers, freqlist = listallrowsfunctry.frequentielist(numbers)
    combinations = []
    i=0
    while i < len(uniquenumbers):
        subcombinations = []
        inumber = uniquenumbers[i]
        amount = freqlist[i][1]
        subcombinations.append([inumber])
        if amount >1:
            subcombinations.append([inumber,inumber])
        k=i+1
        while k< len(uniquenumbers):
            amountofk = freqlist[k][1]
            shorttermcombinations = subcombinations.copy()
            for l in shorttermcombinations:
                temporvalue = []
                for m in l:
                    temporvalue.append(m)
                temporvalue.append(uniquenumbers[k])
                if not(len(temporvalue) == len(numbers)):
                    temporvalue.sort()
                    subcombinations.append(temporvalue)
            if amountofk == 2:
                shorttermcombinations = subcombinations.copy()
                for l in shorttermcombinations:
                    temporvalue = []
                    for m in l:
                        temporvalue.append(m)
                    temporvalue.append(uniquenumbers[k])
                    if not (len(temporvalue) == len(numbers)):
                        temporvalue.sort()
                        if not(temporvalue in subcombinations):
                            subcombinations.append(temporvalue)
            k+=1
        for m in subcombinations:
            combinations.append(m)
        i+=1
    return combinations"""
def allpossiblecombinations3(numbers):
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(numbers)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
def allpossiblecombinations2(numbers):
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    return list(chain.from_iterable(set(combinations(numbers, r+2)) for r in range(len(numbers)-2)))
def traildfsd(numbers):
    s = list(numbers)

#print(allpossiblecombinations([1,2,3]))
#print(allpossiblecombinations([1,2,2,3]))
"""start = time.time()
print(allpossiblecombinations([1,2,2,3,4,5]))
end = time.time()
print(end - start)#4.076957702636719e-05
start = time.time()
#print(allpossiblecombinations([101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,109,110,110,111,111,112,112,113,113,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,413,413,0,0,0,0,0,0,0,0]))
#print(allpossiblecombinations([101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,109,110,110,111,111,112,112,113,113,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,413,413]))
#print(allpossiblecombinations([101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,109,110,110,111,111,112,112,113,113]))
print(allpossiblecombinations([101,102,103,104,105,107,108,109,110,111,112,113]))
end = time.time()
print(end - start)#0.004841804504394531"""
start = time.time()
#d = [101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,109,110,110,111,111,112,112,113,113]
d= [101,101,102,102,103,103,104,104,105,105,106,106]
m = allpossiblecombinations2(d)
print(len(m))
#m = list(set(m))
print(len(m))
#print(m)
print(m)

#print(m)
end = time.time()
print(end - start) #0.6871631145477295 vs 0,16
start = time.time()
#print(allpossiblecombinations([101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,109,110,110,111,111,112,112,113,113]))
end = time.time()
print(end - start) # not ending vs 73.83786606788635
'''
        wat wil ik dat deze code doet:
        maxlength van output = len(input)-1
        minlen = 1 (dus geen lege, behalve als input leeg is)
        geeft alle waarden terug
        input = [1,2,3]
        output = [[1],[1,2],[1,3],[2],[2,3],[3]
        
        input = [1,2,2,3]
        output = [[1],[1,2],[1,3],[1,2,2],[1,2,3],[2],[2,2],[2,3],[2,2,3],[3]
                '''
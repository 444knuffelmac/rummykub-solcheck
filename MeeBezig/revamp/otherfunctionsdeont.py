from itertools import combinations, chain
def reversenumber(number:int):
    stringnumber = str(number)
    flippednumber = int(stringnumber[::-1])
    return (flippednumber * 10) if len(stringnumber) == 2 else flippednumber


def whatvalueshaveneighboursbothtypes(pscolornumber):
    pscolornumberalt =  [int(s) for s in sorted([str(s)[::-1] for s in pscolornumber])]  # presort for the other one
    noneighbours = pscolornumber.copy()
    for i in range(len(pscolornumber)):
        number = pscolornumber[i]
        if number == 0: noneighbours.remove(number); continue
        if 0 < i and number - 1 == pscolornumber[i - 1]:
            noneighbours.remove(number);continue

        if i + 2 < len(pscolornumber) and number + 1 == pscolornumber[i + 1]:
            noneighbours.remove(number);continue
    for i in range(len(pscolornumberalt)):
        number = pscolornumberalt[i]
        if not (reversenumber(number) in noneighbours): continue
        if i + 1 < len(pscolornumberalt) and number %10 <= 3:
            if number + 1 == pscolornumberalt[i + 1]:
                noneighbours.remove(reversenumber(number)); continue
            if number %10 <= 2:
                if number + 2 == pscolornumberalt[i + 1]:
                    noneighbours.remove(reversenumber(number));continue
                if number % 10 == 1:
                    if number + 3 == pscolornumberalt[i + 1]:
                        noneighbours.remove(reversenumber(number)); continue
        if 0 < i and number %10 >= 2:
            if number - 1 == pscolornumberalt[i - 1]:
                noneighbours.remove(reversenumber(number)); continue
            if number % 10 >= 3:
                if number - 2 == pscolornumberalt[i - 1]:
                    noneighbours.remove(reversenumber(number));continue
                if number % 10 == 4:
                    if number - 3 == pscolornumberalt[i - 1]:
                        noneighbours.remove(reversenumber(number));continue
    return noneighbours

def secondfilter(noneighbours, jokercounted,uniquenumbers):
    extendedneighbour = [i for i in noneighbours if i - 2 in uniquenumbers or i + 2 in uniquenumbers]
    return False if len(extendedneighbour) > (jokercounted * 2) + 1 or (jokercounted == 1 and any(i and not (i in extendedneighbour) for i in noneighbours)) else True

def mogelijkepaden(pad,rows):
    confirmedpos = [] # alles is gechecked en is correct, dus deze kunnen
    beginrows = [i[0] for i in rows]
    w = 1 if pad[0] == 0 else 0
    if not (pad[w] in beginrows): return []
    maybepos = [rows[i] for i in range(len(beginrows)) if beginrows[i] == pad[w]]

    for i in maybepos:
        stopped = False
        for k in range(len(i)):
            if not (i[k] in pad):
                stopped = True
                break
        if not stopped:
            confirmedpos.append(i)
    return confirmedpos
def mogelijkepaden2(pad,rows,beginrows):
    # pad = de lijst van overgebleven nummers in dit pad
    # confirmedpos alle mogelijke rijen in dit pad
    maybepos = [] #beginindex is juist, rest niet gechecked
    confirmedpos = [] # alles is gechecked en is correct, dus deze kunnen
    w=0
    while pad[w] == 0:
        w+=1
    if pad[w] in beginrows:
        i=0
        while i < len(beginrows):
            if beginrows[i] == pad[w]:
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
def makeallrowsnofunc(uniquenumbers, jokercounted):
    allrows = []
    threetilerows = []
    for i in uniquenumbers:
        if i + 1 in uniquenumbers:
            if i + 2 in uniquenumbers:
                if i + 3 in uniquenumbers:
                    if i + 4 in uniquenumbers:
                        allrows.append([i, i + 1, i + 2, i + 3, i + 4])
                    allrows.append([i, i + 1, i + 2, i + 3])
        if i + 100 in uniquenumbers:
            if i + 200 in uniquenumbers:
                if i + 300 in uniquenumbers:
                    allrows.append([i, i + 100, i + 200, i + 300])
        if i + 1 in uniquenumbers:
            if i + 2 in uniquenumbers:
                allrows.append([i, i + 1, i + 2])
                threetilerows.append([i, i + 1, i + 2])
        if i + 100 in uniquenumbers:
            if i + 200 in uniquenumbers:
                allrows.append([i, i + 100, i + 200])
                threetilerows.append([i, i + 100, i + 200])
            if i + 300 in uniquenumbers:
                allrows.append([i, i + 100, i + 300])
                threetilerows.append([i, i + 100, i + 300])
        if i + 200 in uniquenumbers:
            if i + 300 in uniquenumbers:
                allrows.append([i, i + 200, i + 300])
                threetilerows.append([i, i + 200, i + 300])
    if jokercounted > 0:
        for i in uniquenumbers:
            if i + 1 in uniquenumbers:
                if i + 2 in uniquenumbers:
                    if i + 3 in uniquenumbers:
                        allrows.append([i, i + 1, i + 2, i + 3, 0])
                    if i + 4 in uniquenumbers:
                        allrows.append([i, i + 1, i + 2, 0, i + 4])
                if i + 3 in uniquenumbers:
                    if i + 4 in uniquenumbers:
                        allrows.append([i, i + 1, 0, i + 3, i + 4])
            if i + 2 in uniquenumbers:
                if i + 3 in uniquenumbers:
                    if i + 4 in uniquenumbers:
                        allrows.append([i, 0, i + 2, i + 3, i + 4])
            if i + 1 in uniquenumbers:
                if i + 2 in uniquenumbers:
                    allrows.append([i, i + 1, i + 2, 0])
                if i + 3 in uniquenumbers:
                    allrows.append([i, i + 1, 0, i + 3])
            if i + 2 in uniquenumbers:
                if i + 3 in uniquenumbers:
                    allrows.append([i, 0, i + 2, i + 3])
            if i + 100 in uniquenumbers:
                if i + 200 in uniquenumbers:
                    allrows.append([i, i + 100, i + 200, 0])
                if i + 300 in uniquenumbers:
                    allrows.append([i, i + 100, 0, i + 300])
            if i + 200 in uniquenumbers:
                if i + 300 in uniquenumbers:
                    allrows.append([i, 0, i + 200, i + 300])
            if i + 1 in uniquenumbers:
                allrows.append([i, i + 1, 0])
                threetilerows.append([i, i + 1, 0])
            if i + 2 in uniquenumbers:
                allrows.append([i, 0, i + 2])
                threetilerows.append([i, 0, i + 2])
            if i + 100 in uniquenumbers:
                allrows.append([i, i + 100, 0])
                threetilerows.append([i, i + 100, 0])
            if i + 200 in uniquenumbers:
                allrows.append([i, 0, i + 200])
                threetilerows.append([i, 0, i + 200])

            if i + 300 in uniquenumbers:
                allrows.append([i, 0, i + 300])
                threetilerows.append([i, 0, i + 300])
        if jokercounted > 1:
            for i in uniquenumbers:
                if i + 1 in uniquenumbers:
                    if i + 2 in uniquenumbers:
                        allrows.append([i, i + 1, i + 2, 0, 0])
                    if i + 3 in uniquenumbers:
                        allrows.append([i, i + 1, 0, i + 3, 0])
                    if i + 4 in uniquenumbers:
                        allrows.append([i, i + 1, 0, 0, i + 4])
                if i + 2 in uniquenumbers:
                    if i + 3 in uniquenumbers:
                        allrows.append([i, 0, i + 2, i + 3, 0])
                    if i + 4 in uniquenumbers:
                        allrows.append([i, 0, i + 2, 0, i + 4])
                if i + 3 in uniquenumbers:
                    if i + 4 in uniquenumbers:
                        allrows.append([i, 0, 0, i + 3, i + 4])
                if i + 1 in uniquenumbers:
                    allrows.append([i, i + 1, 0, 0])
                if i + 2 in uniquenumbers:
                    allrows.append([i, 0, i + 2, 0])
                if i + 3 in uniquenumbers:
                    allrows.append([i, 0, 0, i + 3])
                if i + 100 in uniquenumbers:
                    allrows.append([i, i + 100, 0, 0])
                if i + 200 in uniquenumbers:
                    allrows.append([i, 0, i + 200, 0])
                if i + 300 in uniquenumbers:
                    allrows.append([i, 0, 0, i + 300])
                allrows.append([i, 0, 0])
            if jokercounted > 2:
                for i in uniquenumbers:
                    if i + 1 in uniquenumbers:
                        allrows.append([i, i + 1, 0, 0, 0])
                    if i + 2 in uniquenumbers:
                        allrows.append([i, 0, i + 2, 0, 0])
                    if i + 3 in uniquenumbers:
                        allrows.append([i, 0, 0, i + 3, 0])
                    if i + 4 in uniquenumbers:
                        allrows.append([i, 0, 0, 0, i + 4])
                    allrows.append([i, 0, 0, 0])
                if jokercounted > 3:
                    for i in uniquenumbers:
                        allrows.append([i, 0, 0, 0, 0])

    return allrows,threetilerows

def makeallrowsnofunc2(uniquenumbers, jokercounted):
    lsittemp = list(set(combinations(uniquenumbers, 3)))
    liste = []
    for i in lsittemp:
        liste.append(sorted(list(i)))
    filter(lambda i: not any(i[x] == 0 for x in range(3)), lsittemp)
    filter(lambda i: i[1]-i[0] < 1 or any(i[1]-i[0] == l for l in [100,200,300]) or any(i[1]-i[0] == l for l in [1,2,3]) , lsittemp)

def filterzoveel(uniquenumbers,threetilerows):
    stillpossible = False
    uniquenumbersnojoker = uniquenumbers.copy()
    if 0 in uniquenumbersnojoker:
        uniquenumbersnojoker.remove(0)
    for i in uniquenumbersnojoker:
        stillpossible = False
        if i == 0:
            continue
        for k in threetilerows:
            if not (i in k):
                continue
            stillpossible = True
            break
        if not stillpossible:
            break
    return stillpossible


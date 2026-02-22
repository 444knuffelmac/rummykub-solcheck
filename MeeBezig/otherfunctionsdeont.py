def whatvalueshaveneighboursbothtypes(pscolornumber):
    noneighbours = []
    x = len(pscolornumber)
    for i in range(x):
        number = pscolornumber[i]
        if number == 0: continue
        if 0 < i and number - 1 == pscolornumber[i - 1]:
            continue
        if i + 2 < x and number + 1 == pscolornumber[i + 1]:
            continue
        if number //100 <= 3:
            if number + 100 in pscolornumber:
                continue
            if number //100 <= 2:
                if number + 200 in pscolornumber:
                    continue
                if number //100 == 1:
                    if number + 300 in pscolornumber:
                         continue
        if number //100 >= 2:
            if number - 100 in pscolornumber:
                 continue
            if number //100 >= 3:
                if number - 200 in pscolornumber:
                    continue
                if number //100 == 4 and number - 300 in pscolornumber: continue
        noneighbours.append(number)
    return noneighbours



def secondfilter(noneighbours, jokercounted,uniquenumbers):
    extendedneighbour = [i for i in noneighbours if i - 2 in uniquenumbers or i + 2 in uniquenumbers]
    return False if len(extendedneighbour) > (jokercounted * 2) + 1 or (jokercounted == 1 and any(i and not (i in extendedneighbour) for i in noneighbours)) else True

def possiblewithrows(uniquenumbers, jokercounted):

    uniquenumbersnojoker = uniquenumbers.copy()
    if 0 in uniquenumbersnojoker: uniquenumbersnojoker.remove(0)
    if jokercounted > 0:

        for i in uniquenumbersnojoker:#710 keer utigevoerd dus TE VEEL

            if not (any(i+x in uniquenumbersnojoker for x in [1,2,100,200,300,-1,-2,-100,-200,-300])):
                return []
    else:
        for i in uniquenumbersnojoker:
            if not (any(all(i + x in uniquenumbersnojoker for x in y) for y in
                   [[1, 2], [100, 200], [100, 300], [200, 300], [-1, 1], [-2, -1], [-100, 100], [-100, 200],[-200, 100], [-300, -200], [-300, -100]])):
                return []


    allrows = []
    i = uniquenumbersnojoker[0]
    if all(i + x in uniquenumbersnojoker for x in  [1,2,3]):
        if i + 4 in uniquenumbersnojoker:
            allrows.append([(i+x) for x in [0,1,2,3,4]])
        allrows.append([(i+x) for x in [0,1,2,3]])

    if all(i + x in uniquenumbersnojoker for x in  [100,200,300]):
        allrows.append([(i+x) for x in [0,100,200,300]])
    if all(i + x in uniquenumbersnojoker for x in  [1,2]):
        allrows.append([i, i + 1, i + 2])
    if i + 100 in uniquenumbersnojoker:
        if i + 200 in uniquenumbersnojoker:
            allrows.append([i, i + 100, i + 200])
        if i + 300 in uniquenumbersnojoker:
            allrows.append([i, i + 100, i + 300])
    if i + 200 in uniquenumbersnojoker:
        if i + 300 in uniquenumbersnojoker:
            allrows.append([i, i + 200, i + 300])

    if jokercounted > 0:
        if all(i + x in uniquenumbersnojoker for x in  [1,2]):
            if i + 3 in uniquenumbersnojoker:
                allrows.append([i, i + 1, i + 2, i + 3, 0])
            if i + 4 in uniquenumbersnojoker:
                allrows.append([i, i + 1, i + 2, 0, i + 4])
            if all(i + x in uniquenumbersnojoker for x in [3,4]):
                    allrows.append([i, i + 1, 0, i + 3, i + 4])
        if all(i + x in uniquenumbersnojoker for x in  [2,3,4]):
            allrows.append([i, 0, i + 2, i + 3, i + 4])
        if i + 1 in uniquenumbersnojoker:
            if i + 2 in uniquenumbersnojoker:
                allrows.append([i, i + 1, i + 2, 0])
            if i + 3 in uniquenumbersnojoker:
                allrows.append([i, i + 1, 0, i + 3])
        if all(i + x in uniquenumbersnojoker for x in [2,3]):
                allrows.append([i, 0, i + 2, i + 3])
        if i + 100 in uniquenumbersnojoker:
            if i + 200 in uniquenumbersnojoker:
                allrows.append([i, i + 100, i + 200, 0])
            if i + 300 in uniquenumbersnojoker:
                allrows.append([i, i + 100, 0, i + 300])
        if all(i + x in uniquenumbersnojoker for x in [200,300]):
                allrows.append([i, 0, i + 200, i + 300])
        if i + 1 in uniquenumbersnojoker:
            allrows.append([i, i + 1, 0])
        if i + 2 in uniquenumbersnojoker:
            allrows.append([i, 0, i + 2])
        if i + 100 in uniquenumbersnojoker:
            allrows.append([i, i + 100, 0])
        if i + 200 in uniquenumbersnojoker:
            allrows.append([i, 0, i + 200])
        if i + 300 in uniquenumbersnojoker:
            allrows.append([i, 0, i + 300])
        if jokercounted > 1:
            if i + 1 in uniquenumbersnojoker:
                if i + 2 in uniquenumbersnojoker:
                    allrows.append([i, i + 1, i + 2, 0, 0])
                if i + 3 in uniquenumbersnojoker:
                    allrows.append([i, i + 1, 0, i + 3, 0])
                if i + 4 in uniquenumbersnojoker:
                    allrows.append([i, i + 1, 0, 0, i + 4])
            if i + 2 in uniquenumbersnojoker:
                if i + 3 in uniquenumbersnojoker:
                    allrows.append([i, 0, i + 2, i + 3, 0])
                if i + 4 in uniquenumbersnojoker:
                    allrows.append([i, 0, i + 2, 0, i + 4])
            if all(i + x in uniquenumbersnojoker for x in [3,4]):
                    allrows.append([i, 0, 0, i + 3, i + 4])
            if i + 1 in uniquenumbersnojoker:
                allrows.append([i, i + 1, 0, 0])
            if i + 2 in uniquenumbersnojoker:
                allrows.append([i, 0, i + 2, 0])
            if i + 3 in uniquenumbersnojoker:
                allrows.append([i, 0, 0, i + 3])
            if i + 100 in uniquenumbersnojoker:
                allrows.append([i, i + 100, 0, 0])
            if i + 200 in uniquenumbersnojoker:
                allrows.append([i, 0, i + 200, 0])
            if i + 300 in uniquenumbersnojoker:
                allrows.append([i, 0, 0, i + 300])
            allrows.append([i, 0, 0])
            if jokercounted > 2:
                if i + 1 in uniquenumbersnojoker:
                    allrows.append([i, i + 1, 0, 0, 0])
                if i + 2 in uniquenumbersnojoker:
                    allrows.append([i, 0, i + 2, 0, 0])
                if i + 3 in uniquenumbersnojoker:
                    allrows.append([i, 0, 0, i + 3, 0])
                if i + 4 in uniquenumbersnojoker:
                    allrows.append([i, 0, 0, 0, i + 4])
                allrows.append([i, 0, 0, 0])
                if jokercounted > 3:
                    allrows.append([i, 0, 0, 0, 0])

    return allrows
def nojokerrows(allrows,uniquenumbers,threetilerows):
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
        if i +1 in uniquenumbers:
            if i+2 in uniquenumbers:
                allrows.append([i, i + 1, i + 2])
                threetilerows.append([i, i + 1, i + 2])
        if i+100 in uniquenumbers:
           if i+200 in uniquenumbers:
               allrows.append([i, i + 100, i + 200])
               threetilerows.append([i, i + 100, i + 200])
           if i + 300 in uniquenumbers:
                allrows.append([i, i + 100, i + 300])
                threetilerows.append([i, i + 100, i + 300])
        if i + 200 in uniquenumbers:
            if i + 300 in uniquenumbers:
                allrows.append([i, i + 200, i + 300])
                threetilerows.append([i, i + 200, i + 300])
    return allrows,threetilerows
def onejokerrows(allrows,uniquenumbers,threetilerows):
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
    return allrows,threetilerows
def twojokerrows(allrows,uniquenumbers):
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
        if i+3 in uniquenumbers:
            if i + 4 in uniquenumbers:
                allrows.append([i, 0,0, i + 3, i + 4])
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
    return allrows
def threejokerrows(allrows,uniquenumbers):
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
    return allrows
def fourjokerrows(allrows,uniquenumbers):
    for i in uniquenumbers:
        allrows.append([i, 0, 0, 0, 0])
    return allrows
def makeallrows(uniquenumbers, jokercounted):
    allrows = []
    threetilerows = []
    allrows,threetilerows =nojokerrows(allrows,uniquenumbers,threetilerows)
    if jokercounted > 0:
        allrows,threetilerows = onejokerrows(allrows,uniquenumbers,threetilerows)
        if jokercounted > 1:
            allrows = twojokerrows(allrows,uniquenumbers)
            if jokercounted > 2:
                allrows = threejokerrows(allrows,uniquenumbers)
                if jokercounted > 3:
                    allrows = fourjokerrows(allrows,uniquenumbers)
            return True,allrows
    stillpossible = workingthirthfilter(uniquenumbers,threetilerows)
    return stillpossible,allrows
def workingthirthfilter(uniquenumbers,threetilerows):
    init = False
    for i in uniquenumbers:
        init = False
        if i == 0:
            continue
        for k in threetilerows:
            if not (i in k):
                continue
            init = True
            break
        if not init:
            break
    return init


def makeallrowsnofunc(uniquenumbers,jokercounted):
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
            
            
            return True, allrows
    stillpossible = False
    for i in uniquenumbers:
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
    return stillpossible, allrows

print(makeallrows([101,102,103,104],0))
print(makeallrowsnofunc([101,102,103,104],0))
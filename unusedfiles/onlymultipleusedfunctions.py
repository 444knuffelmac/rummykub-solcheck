def reversenumber(number):
    stringnumber = str(number)
    flippednumber = int(stringnumber[::-1])
    if len(stringnumber) ==2:
        return flippednumber*10
    return flippednumber
def finalcalculatorrecursive(piececolnumb):
    if not piececolnumb:
        return True,[]
    jokers = piececolnumb.count(0)
    if jokers == len(piececolnumb):
        returnvalue = []
        i = jokers
        while 0 < i:
            returnvalue.append(0)
            i-=1
        return True, returnvalue
    uniquenumbers = []
    tempvalue = []
    for i in range(len(piececolnumb)):
        number = piececolnumb[i]
        if not number in uniquenumbers:
            uniquenumbers.append(number)
    for i in range(len(uniquenumbers)):
        number = uniquenumbers[i]
        tempvalue.append(number)
        tempvalue.append(piececolnumb.count(number))
        tempvalue = []
    # presort for the other one
    pscolorstring = []
    pscolornumberalt = []
    for x in piececolnumb:
        pscolorstring.append(str(x)[::-1])
    pscolorstring = sorted(pscolorstring)
    for x in pscolorstring:
        pscolornumberalt.append(int(x))
    withneighbourstype1 = []
    withneighbourstype2 = []
    for p in range(len(piececolnumb)):
        number = piececolnumb[p]
        if number == 0:
            continue
        if 1 < p:
            if number - 1 == piececolnumb[p - 1]:
                withneighbourstype1.append(number)
                continue
            if number == piececolnumb[p - 1] and number - 1 == piececolnumb[p - 2]:
                withneighbourstype1.append(number)
                continue
        elif 0 < p:
            if number - 1 == piececolnumb[p - 1]:
                withneighbourstype1.append(number)
                continue
        if p + 2 < len(piececolnumb):
            if number + 1 == piececolnumb[p + 1]:
                withneighbourstype1.append(number)
                continue
            if number == piececolnumb[p + 1] and number + 1 == piececolnumb[p + 2]:
                withneighbourstype1.append(number)
                continue
        elif p + 1 < len(piececolnumb):
            if number + 1 == piececolnumb[p + 1]:
                withneighbourstype1.append(number)
                continue

    for p in range(len(pscolornumberalt)):
        number = pscolornumberalt[p]
        if number == 0:
            continue
        if number % 10 == 1:
            if p + 2 < len(pscolornumberalt):
                if p + 1 < len(pscolornumberalt):
                    if number + 1 == pscolornumberalt[p + 1] or number + 1 == pscolornumberalt[p + 2]:
                        withneighbourstype2.append(reversenumber(number))
                        continue
                    if number + 2 == pscolornumberalt[p + 1] or number + 2 == pscolornumberalt[p + 2]:
                        withneighbourstype2.append(reversenumber(number))
                        continue
                    if number + 3 == pscolornumberalt[p + 1] or number + 3 == pscolornumberalt[p + 2]:
                        withneighbourstype2.append(reversenumber(number))
                        continue
            elif p + 1 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[p + 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number + 2 == pscolornumberalt[p + 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number + 3 == pscolornumberalt[p + 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
        elif number % 10 == 2:
            if p + 2 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[p + 1] or number + 1 == pscolornumberalt[p + 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number + 2 == pscolornumberalt[p + 1] or number + 2 == pscolornumberalt[p + 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            elif p + 1 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[p + 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number + 2 == pscolornumberalt[p + 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            if 1 < p:
                if number - 1 == pscolornumberalt[p - 1] or number - 1 == pscolornumberalt[p - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            elif 0 < p:
                if number - 1 == pscolornumberalt[p - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
        elif number % 10 == 3:
            if p + 2 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[p + 1] or number + 1 == pscolornumberalt[p + 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            elif p + 1 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[p + 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            if 1 < p:
                if number - 1 == pscolornumberalt[p - 1] or number - 1 == pscolornumberalt[p - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 2 == pscolornumberalt[p - 1] or number - 2 == pscolornumberalt[p - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            elif 0 < p:
                if number - 1 == pscolornumberalt[p - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 2 == pscolornumberalt[p - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
        else:
            if 1 < p:
                if number - 1 == pscolornumberalt[p - 1] or number - 1 == pscolornumberalt[p - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 2 == pscolornumberalt[p - 1] or number - 2 == pscolornumberalt[p - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 3 == pscolornumberalt[p - 1] or number - 3 == pscolornumberalt[p - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            elif 0 < p:
                if number - 1 == pscolornumberalt[p - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 2 == pscolornumberalt[p - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 3 == pscolornumberalt[p - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
    noneighbours = []
    for i in uniquenumbers:
        if i == 0:
            continue
        if not ((i in withneighbourstype1) or (i in withneighbourstype2)):
            noneighbours.append(i)
    if jokers == 0:
        if len(noneighbours) > 0:
            return False, []
    extendedneighbour = []
    if jokers > 0:
        for i in noneighbours:
            if i - 2 in uniquenumbers or i + 2 in uniquenumbers:
                extendedneighbour.append(i)
    if len(extendedneighbour) > (jokers * 2) + 1:
        return False,[]
    elif jokers == 1:
        for i in noneighbours:
            if i == 0:
                continue
            if i in extendedneighbour:
                continue
            else:
                return False,[]
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
    if jokers > 0:
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
        if jokers > 1:
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
            if jokers > 2:
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
                if jokers > 3:
                    for i in uniquenumbers:
                        allrows.append([i, 0, 0, 0, 0])
    if jokers < 2:
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
                return False,[]
    alltilerowsbegins = []
    for i in range(len(allrows)):
        alltilerowsbegins.append(allrows[i][0])
    oplossing =[]
    maybepos = []  # beginindex is juist, rest niet gechecked
    confirmedpos = []  # alles is gechecked en is correct, dus deze kunnen
    w = 0
    while piececolnumb[w] == 0:
        w += 1
    if piececolnumb[w] in alltilerowsbegins:
        i = 0
        while i < len(alltilerowsbegins):
            if alltilerowsbegins[i] == piececolnumb[w]:
                maybepos.append(allrows[i])
            i += 1
        for i in maybepos:
            k = 0
            stopped = False
            while k < len(i):
                if i[k] in piececolnumb:
                    k += 1
                    continue
                stopped = True
                break
            if not stopped:
                confirmedpos.append(i)
    possible = False
    print(confirmedpos)
    print(len(confirmedpos))
    for i in confirmedpos:
        smallersize = piececolnumb.copy()
        for l in i:
            smallersize.remove(l)
        possible,oplossing = finalcalculatorrecursive(smallersize)
        if possible:
            oplossing.append(i)
            break
    return possible,oplossing

#piecescolornumber = [101,102,103,104,105,105,106,107,108]

#[101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,109,110,110,111,112,112,113,113,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,413,413,0,0,0,0,0,0,0,0]
#print(finalcalculatorrecursive(piecescolornumber))
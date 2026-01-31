def jokercount(pscolornumber):
    return pscolornumber.count(0)
def onlyuniquenumbers(pscolornumber):
    uniquenumbers = []
    tempvalue = []
    for i in range(len(pscolornumber)):
        number = pscolornumber[i]
        if not number in uniquenumbers:
            uniquenumbers.append(number)
    for i in range(len(uniquenumbers)):
        number = uniquenumbers[i]
        tempvalue.append(number)
        tempvalue.append(pscolornumber.count(number))
        tempvalue = []

    return uniquenumbers
def sortstringly(pscolornumber):
    pscolorstring = []
    pscolornumber2 =[]
    for x in range(len(pscolornumber)):
        pscolorstring.append(str(pscolornumber[x])[::-1])
    pscolorstring =sorted(pscolorstring)
    for x in range(len(pscolorstring)):
        pscolornumber2.append(int(pscolorstring[x]))
    return pscolornumber2
def reversenumber(number):
    stringnumber = str(number)
    flippednumber = int(stringnumber[::-1])
    if len(stringnumber) ==2:
        return flippednumber*10
    return flippednumber
def whatvalueshaveneighboursbothtypes(pscolornumber):
    pscolornumberalt = sortstringly(pscolornumber)  # presort for the other one
    withneighbourstype1 =[]
    withneighbourstype2 =[]
    for i in range(len(pscolornumber)):
        number = pscolornumber[i]
        if number==0:
            continue
        if 1<i:
            if number - 1 == pscolornumber[i - 1]:
                withneighbourstype1.append(number)
                continue
            if number == pscolornumber[i - 1] and number - 1 == pscolornumber[i - 2]:
                withneighbourstype1.append(number)
                continue
        elif 0<i:
            if number - 1 == pscolornumber[i - 1]:
                withneighbourstype1.append(number)
                continue
        if i+2 < len(pscolornumber):
            if number + 1 == pscolornumber[i + 1]:
                withneighbourstype1.append(number)
                continue
            if number == pscolornumber[i + 1] and number + 1 == pscolornumber[i + 2]:
                withneighbourstype1.append(number)
                continue
        elif i+1 < len(pscolornumber):
            if number + 1 == pscolornumber[i + 1]:
                withneighbourstype1.append(number)
                continue

    for i in range(len(pscolornumberalt)):
        number = pscolornumberalt[i]
        if number == 0:
            continue
        if number % 10 == 1:
            if i+2 < len(pscolornumberalt):
                if i + 1 < len(pscolornumberalt):
                    if number + 1 == pscolornumberalt[i + 1] or number+1 == pscolornumberalt[i+2]:
                        withneighbourstype2.append(reversenumber(number))
                        continue
                    if number + 2 == pscolornumberalt[i + 1] or number+2 == pscolornumberalt[i+2]:
                        withneighbourstype2.append(reversenumber(number))
                        continue
                    if number + 3 == pscolornumberalt[i + 1] or number+3 == pscolornumberalt[i+2]:
                        withneighbourstype2.append(reversenumber(number))
                        continue
            elif i+1 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number+2 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number+3 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
        elif number%10 == 2:
            if i+2 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[i + 1] or number + 1 == pscolornumberalt[i + 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number + 2 == pscolornumberalt[i + 1] or number + 2 == pscolornumberalt[i + 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            elif i+1 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number+2 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            if 1<i:
                if number - 1 == pscolornumberalt[i - 1] or number - 1 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            elif 0<i:
                if number - 1 == pscolornumberalt[i-1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
        elif number%10 == 3:
            if i+2 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[i + 1] or number + 1 == pscolornumberalt[i + 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            elif i+1 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            if 1 < i:
                if number - 1 == pscolornumberalt[i - 1] or number - 1 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 2 == pscolornumberalt[i - 1] or number - 2 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            elif 0 < i:
                if number - 1 == pscolornumberalt[i - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 2 == pscolornumberalt[i - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
        else:
            if 1 < i:
                if number - 1 == pscolornumberalt[i - 1] or number - 1 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 2 == pscolornumberalt[i - 1] or number - 2 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 3 == pscolornumberalt[i - 1] or number - 3 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
            elif 0 < i:
                if number - 1 == pscolornumberalt[i - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 2 == pscolornumberalt[i - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue
                if number - 3 == pscolornumberalt[i - 1]:
                    withneighbourstype2.append(reversenumber(number))
                    continue

    return withneighbourstype1, withneighbourstype2
def neighbourless(uniquenumbers,withneighbourstype1,withneighbourstype2):
    noneighbours = []
    for i in uniquenumbers:
        if i == 0:
            continue
        if not((i in withneighbourstype1) or (i in withneighbourstype2)):
            noneighbours.append(i)
    return noneighbours
def firstfilter(noneighbours,uniquenumbers):
    stillpossible = True
    if not 0 in uniquenumbers:
        if len(noneighbours) > 0:
            stillpossible = False
    return stillpossible
def extendedneighbours(uniquenumbers,jokercounted,noneighbours):
    extendedneighbour = []
    if jokercounted > 0:
        for i in noneighbours:
            if i - 2 in uniquenumbers or i+2 in uniquenumbers:
                extendedneighbour.append(i)
    return extendedneighbour
def secondfilter(noneighbours,extendedneighbour,jokercounted):
    possible = True
    if len(extendedneighbour) > (jokercounted*2)+1:
        possible = False
    elif jokercounted == 1:
        for i in noneighbours:
            if i == 0:
                continue
            if i in extendedneighbour:
                continue
            else:
                possible = False
                break
    return possible
def makeallthreetilerows(uniquenumbers, jokercounted):
    threetilerows = []
    if jokercounted == 0:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if i > len(uniquenumbers) - 3:
                continue
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    threetilerows.append([number, number + 1, number + 2])
            if number + 100 in uniquenumbers:
                if number + 200 in uniquenumbers:
                    threetilerows.append([number, number + 100, number + 200])
                if number + 300 in uniquenumbers:
                    threetilerows.append([number, number + 100, number + 300])
            if number + 200 in uniquenumbers:
                if number + 300 in uniquenumbers:
                    threetilerows.append([number, number + 200, number + 300])
    elif jokercounted == 1:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if i == len(uniquenumbers) - 1:
                continue
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    threetilerows.append([number, number + 1, number + 2])
            if number + 100 in uniquenumbers:
                if number + 200 in uniquenumbers:
                    threetilerows.append([number, number + 100, number + 200])
                if number + 300 in uniquenumbers:
                    threetilerows.append([number, number + 100, number + 300])
            if number + 200 in uniquenumbers:
                if number + 300 in uniquenumbers:
                    threetilerows.append([number, number + 200, number + 300])
            if number+1 in uniquenumbers:
                threetilerows.append([number, number + 1, 0])
            if number + 2 in uniquenumbers:
                threetilerows.append([number, 0, number + 2])
            if number + 100 in uniquenumbers:
                threetilerows.append([number, number + 100, 0])
            if number+200 in uniquenumbers:
                threetilerows.append([number, 0, number + 200])
            if number + 300 in uniquenumbers:
                threetilerows.append([number, 0, number + 300])
    else:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    threetilerows.append([number, number + 1, number + 2])
            if number + 100 in uniquenumbers:
                if number + 200 in uniquenumbers:
                    threetilerows.append([number, number + 100, number + 200])
                if number + 300 in uniquenumbers:
                    threetilerows.append([number, number + 100, number + 300])
            if number + 200 in uniquenumbers:
                if number + 300 in uniquenumbers:
                    threetilerows.append([number, number + 200, number + 300])
            if number + 1 in uniquenumbers:
                threetilerows.append([number, number + 1, 0])
            if number+2 in uniquenumbers:
                threetilerows.append([number, 0, number + 2])
            if number+100 in uniquenumbers:
                threetilerows.append([number, number + 100, 0])
            if number+200 in uniquenumbers:
                threetilerows.append([number, 0, number + 200])
            if number + 300 in uniquenumbers:
                threetilerows.append([number, 0, number + 300])
            threetilerows.append([number, 0, 0])
    return threetilerows
def thirthfilter(uniquenumbers,threetilerows):
    notinit = False
    for i in uniquenumbers:
        if i == 0:
            continue
        if not (i in threetilerows):
            notinit = True
            break
    return notinit
def makeallfourtilerows(uniquenumbers,jokercounted):
    fourtilerows = []
    if jokercounted == 0:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if i > len(uniquenumbers) - 4:
                continue

            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    if number+3 in uniquenumbers:
                        fourtilerows.append([number, number + 1, number + 2,number+3])
            if number + 100 in uniquenumbers:
                if number + 200 in uniquenumbers:
                    if number+300 in uniquenumbers:
                        fourtilerows.append([number, number + 100, number + 200,number+300])
    elif jokercounted == 1:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if i > len(uniquenumbers)-3:
                continue
            if number+1 in uniquenumbers:
                if number+2 in uniquenumbers:
                    if number+3 in uniquenumbers:
                        fourtilerows.append([number, number+1, number + 2,number+3])
            if number+100 in uniquenumbers:
                if number+200 in uniquenumbers:
                    if number+300 in uniquenumbers:
                        fourtilerows.append([number,number+100, number + 200, number + 300])
            if number+1 in uniquenumbers:
                if number+2 in uniquenumbers:
                    fourtilerows.append([number, number + 1, number+2, 0])
                if number+3 in uniquenumbers:
                    fourtilerows.append([number, number+1,0, number+3])
            if number+2 in uniquenumbers:
                if number+3 in uniquenumbers:
                    fourtilerows.append([number,0, number+2, number+3])
            if number+100 in uniquenumbers:
                if number+200 in uniquenumbers:
                    fourtilerows.append([number, number + 100, number + 200,0])
                if number+300 in uniquenumbers:
                    fourtilerows.append([number, number + 100, 0,number + 300])
            if number+200 in uniquenumbers:
                if number+300 in uniquenumbers:
                    fourtilerows.append([number, 0,number + 200, number + 300])
    elif jokercounted == 2:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if i == len(uniquenumbers)-1:
                continue
            if number+1 in uniquenumbers:
                if number+2 in uniquenumbers:
                    if number+3 in uniquenumbers:
                        fourtilerows.append([number, number+1, number + 2,number+3])
            if number+100 in uniquenumbers:
                if number+200 in uniquenumbers:
                    if number+300 in uniquenumbers:
                        fourtilerows.append([number,number+100, number + 200, number + 300])
            if number+1 in uniquenumbers:
                if number+2 in uniquenumbers:
                    fourtilerows.append([number, number + 1, number+2, 0])
                if number+3 in uniquenumbers:
                    fourtilerows.append([number, number+1,0, number+3])
            if number+2 in uniquenumbers:
                if number+3 in uniquenumbers:
                    fourtilerows.append([number,0, number+2, number+3])
            if number+100 in uniquenumbers:
                if number+200 in uniquenumbers:
                    fourtilerows.append([number, number + 100, number + 200,0])
                if number+300 in uniquenumbers:
                    fourtilerows.append([number, number + 100, 0,number + 300])
            if number+200 in uniquenumbers:
                if number+300 in uniquenumbers:
                    fourtilerows.append([number, 0,number + 200, number + 300])
            if number+1 in uniquenumbers:
                fourtilerows.append([number, number+1, 0,0])
            if number+2 in uniquenumbers:
                fourtilerows.append([number, 0,number+2,0])
            if number+3 in uniquenumbers:
                fourtilerows.append([number, 0, 0,number+3])
            if number+100 in uniquenumbers:
                fourtilerows.append([number, number+100, 0,0])
            if number+200 in uniquenumbers:
                fourtilerows.append([number,0, number+200, 0])
            if number+300 in uniquenumbers:
                fourtilerows.append([number, 0,0, number+300])

    else:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    if number + 3 in uniquenumbers:
                        fourtilerows.append([number, number + 1, number + 2, number + 3])
            if number + 100 in uniquenumbers:
                if number + 200 in uniquenumbers:
                    if number + 300 in uniquenumbers:
                        fourtilerows.append([number, number + 100, number + 200, number + 300])
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    fourtilerows.append([number, number + 1, number + 2, 0])
                if number + 3 in uniquenumbers:
                    fourtilerows.append([number, number + 1, 0, number + 3])
            if number + 2 in uniquenumbers:
                if number + 3 in uniquenumbers:
                    fourtilerows.append([number, 0, number + 2, number + 3])
            if number + 100 in uniquenumbers:
                if number + 200 in uniquenumbers:
                    fourtilerows.append([number, number + 100, number + 200, 0])
                if number + 300 in uniquenumbers:
                    fourtilerows.append([number, number + 100, 0, number + 300])
            if number + 200 in uniquenumbers:
                if number + 300 in uniquenumbers:
                    fourtilerows.append([number, 0, number + 200, number + 300])
            if number + 1 in uniquenumbers:
                fourtilerows.append([number, number + 1, 0, 0])
            if number + 2 in uniquenumbers:
                fourtilerows.append([number, 0, number + 2, 0])
            if number + 3 in uniquenumbers:
                fourtilerows.append([number, 0, 0, number + 3])
            if number + 100 in uniquenumbers:
                fourtilerows.append([number, number + 100, 0, 0])
            if number + 200 in uniquenumbers:
                fourtilerows.append([number, 0, number + 200, 0])
            if number + 300 in uniquenumbers:
                fourtilerows.append([number, 0, 0, number + 300])
            fourtilerows.append([number, 0, 0,0])
    return fourtilerows
def makeallfivetilerows(uniquenumbers, jokercounted): #longest row with use (otherwise it can be saved as 3+3) --> 1xxx5 is the last
    #time jokers are usefull in that way, as it reduces it from 4 jokers to 3 jokers needed.
    fivetilerows = []
    if jokercounted == 0:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if i> len(uniquenumbers)-5:
                continue

            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    if number + 3 in uniquenumbers:
                        if number+4 in uniquenumbers:
                            fivetilerows.append([number, number + 1, number + 2, number + 3,number+4])
    elif jokercounted == 1:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if i > len(uniquenumbers) - 4:
                continue
            if number+1 in uniquenumbers:
                if number+2 in uniquenumbers:
                    if number+3 in uniquenumbers:
                        if number+4 in uniquenumbers:
                            fivetilerows.append([number, number + 1, number + 2, number + 3,number+4])
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    if number + 3 in uniquenumbers:
                        fivetilerows.append([number, number + 1, number + 2, number + 3, 0])
                    if number+4 in uniquenumbers:
                        fivetilerows.append([number, number + 1, number + 2,0, number + 4])
                if number+3 in uniquenumbers:
                    if number+4 in uniquenumbers:
                        fivetilerows.append([number, number + 1, 0, number + 3, number + 4])
            if number+2 in uniquenumbers:
                if number+3 in uniquenumbers:
                    if number+4 in uniquenumbers:
                        fivetilerows.append([number, 0, number + 2, number + 3, number + 4])
    elif jokercounted == 2:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if i > len(uniquenumbers) - 3:
                continue
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    if number + 3 in uniquenumbers:
                        if number + 4 in uniquenumbers:
                            fivetilerows.append([number, number + 1, number + 2, number + 3, number + 4])
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    if number + 3 in uniquenumbers:
                        fivetilerows.append([number, number + 1, number + 2, number + 3, 0])
                    if number + 4 in uniquenumbers:
                        fivetilerows.append([number, number + 1, number + 2, 0, number + 4])
                if number + 3 in uniquenumbers:
                    if number + 4 in uniquenumbers:
                        fivetilerows.append([number, number + 1, 0, number + 3, number + 4])
            if number + 2 in uniquenumbers:
                if number + 3 in uniquenumbers:
                    if number + 4 in uniquenumbers:
                        fivetilerows.append([number, 0, number + 2, number + 3, number + 4])
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    fivetilerows.append([number, number + 1, number + 2, 0, 0])
                if number + 3 in uniquenumbers:
                    fivetilerows.append([number, number + 1, 0, number + 3, 0])
                if number + 4 in uniquenumbers:
                        fivetilerows.append([number, number + 1, 0, 0, number + 4])
            if number + 2 in uniquenumbers:
                if number + 3 in uniquenumbers:
                    fivetilerows.append([number, 0, number + 2, number + 3, 0])
                if number + 4 in uniquenumbers:
                    fivetilerows.append([number, 0, number + 2, 0, number + 4])

    elif jokercounted == 3:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if i == len(uniquenumbers) - 1:
                continue
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    if number + 3 in uniquenumbers:
                        if number + 4 in uniquenumbers:
                            fivetilerows.append([number, number + 1, number + 2, number + 3, number + 4])
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    if number + 3 in uniquenumbers:
                        fivetilerows.append([number, number + 1, number + 2, number + 3, 0])
                    if number + 4 in uniquenumbers:
                        fivetilerows.append([number, number + 1, number + 2, 0, number + 4])
                if number + 3 in uniquenumbers:
                    if number + 4 in uniquenumbers:
                        fivetilerows.append([number, number + 1, 0, number + 3, number + 4])
            if number + 2 in uniquenumbers:
                if number + 3 in uniquenumbers:
                    if number + 4 in uniquenumbers:
                        fivetilerows.append([number, 0, number + 2, number + 3, number + 4])
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    fivetilerows.append([number, number + 1, number + 2, 0, 0])
                if number + 3 in uniquenumbers:
                    fivetilerows.append([number, number + 1, 0, number + 3, 0])
                if number + 4 in uniquenumbers:
                    fivetilerows.append([number, number + 1, 0, 0, number + 4])
            if number + 2 in uniquenumbers:
                if number + 3 in uniquenumbers:
                    fivetilerows.append([number, 0, number + 2, number + 3, 0])
                if number + 4 in uniquenumbers:
                    fivetilerows.append([number, 0, number + 2, 0, number + 4])
            if number+1 in uniquenumbers:
                fivetilerows.append([number, number + 1, 0, 0, 0])
            if number+2 in uniquenumbers:
                fivetilerows.append([number, 0, number + 2, 0, 0])
            if number+3 in uniquenumbers:
                fivetilerows.append([number, 0, 0, number + 3, 0])
            if number+4 in uniquenumbers:
                fivetilerows.append([number, 0, 0, 0, number + 4])
    else:
        for i in range(len(uniquenumbers)):
            number = uniquenumbers[i]
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    if number + 3 in uniquenumbers:
                        if number + 4 in uniquenumbers:
                            fivetilerows.append([number, number + 1, number + 2, number + 3, number + 4])
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    if number + 3 in uniquenumbers:
                        fivetilerows.append([number, number + 1, number + 2, number + 3, 0])
                    if number + 4 in uniquenumbers:
                        fivetilerows.append([number, number + 1, number + 2, 0, number + 4])
                if number + 3 in uniquenumbers:
                    if number + 4 in uniquenumbers:
                        fivetilerows.append([number, number + 1, 0, number + 3, number + 4])
            if number + 2 in uniquenumbers:
                if number + 3 in uniquenumbers:
                    if number + 4 in uniquenumbers:
                        fivetilerows.append([number, 0, number + 2, number + 3, number + 4])
            if number + 1 in uniquenumbers:
                if number + 2 in uniquenumbers:
                    fivetilerows.append([number, number + 1, number + 2, 0, 0])
                if number + 3 in uniquenumbers:
                    fivetilerows.append([number, number + 1, 0, number + 3, 0])
                if number + 4 in uniquenumbers:
                    fivetilerows.append([number, number + 1, 0, 0, number + 4])
            if number + 2 in uniquenumbers:
                if number + 3 in uniquenumbers:
                    fivetilerows.append([number, 0, number + 2, number + 3, 0])
                if number + 4 in uniquenumbers:
                    fivetilerows.append([number, 0, number + 2, 0, number + 4])
            if number + 1 in uniquenumbers:
                fivetilerows.append([number, number + 1, 0, 0, 0])
            if number + 2 in uniquenumbers:
                fivetilerows.append([number, 0, number + 2, 0, 0])
            if number + 3 in uniquenumbers:
                fivetilerows.append([number, 0, 0, number + 3, 0])
            if number + 4 in uniquenumbers:
                fivetilerows.append([number, 0, 0, 0, number + 4])
            fivetilerows.append([number, 0, 0,0, 0])
    return fivetilerows
def beginswith(matrixarray):
    beginwaarden=[]
    for i in range(len(matrixarray)):
        beginwaarden.append(matrixarray[i][0])
    return beginwaarden
def mogelijkepaden(pad,rows,beginrows):
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
def finalcalculatorrecursive(piececolnumb):
    if not piececolnumb:
        return True,[]
    jokers = jokercount(piececolnumb)
    if jokers == len(piececolnumb):
        returnvalue = []
        i = jokers
        while 0 < i:
            returnvalue.append(0)
            i-=1
        return True, returnvalue

    uniquenumbers = onlyuniquenumbers(piececolnumb)
    n, o = whatvalueshaveneighboursbothtypes(uniquenumbers)
    neighbourlessnumbers = neighbourless(uniquenumbers, n, o)
    stillpos = firstfilter(neighbourlessnumbers, uniquenumbers)
    if not stillpos:
        return False,[]
    farneighbours = extendedneighbours(uniquenumbers, jokers, neighbourlessnumbers)
    stillpos =secondfilter(neighbourlessnumbers,farneighbours,jokers)
    if not stillpos:
        return False,[]
    threetilerow = makeallthreetilerows(uniquenumbers, jokers)
    stillpos = thirthfilter(uniquenumbers, threetilerow)
    if not stillpos:
        return False,[]
    fourtilerow = makeallfourtilerows(uniquenumbers, jokers)
    fivetilerow = makeallfivetilerows(uniquenumbers, jokers)
    threetilerowbegin = beginswith(threetilerow)
    fourtilerowbegin = beginswith(fourtilerow)
    fivetilerowbegin = beginswith(fivetilerow)
    oplossing =[]
    if not piececolnumb:
        return True,[]
    a,b,c,mogelijkpaden = getmogelijkepaden(piececolnumb,threetilerow,fourtilerow,fivetilerow,threetilerowbegin,fourtilerowbegin,fivetilerowbegin)
    possible = False
    for i in mogelijkpaden:
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
#print(generalfunctionsimportthis.finalcalculatorrecursive(piecescolornumber))
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
    print(pscolornumber)
    print(pscolornumberalt)
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
'''def makeeverypossiblerow(pscolornumber):

    # if it is to small
    if len(pscolornumber) < 3:
        return pscolornumber,[]
    pscolornumberalt = sortstringly(pscolornumber)  # presort for the other one
    rows = []

    #checks for jokers
    jokeramount = pscolornumber.count(0)
    if jokeramount == 0:'''
def frequentielist(pscolornumber):
    uniquenumbers = []
    frequencienumbers = []
    tempvalue = []
    for i in range(len(pscolornumber)):
        number = pscolornumber[i]
        if not number in uniquenumbers:
            uniquenumbers.append(number)
    for i in range(len(uniquenumbers)):
        number = uniquenumbers[i]
        tempvalue.append(number)
        tempvalue.append(pscolornumber.count(number))
        frequencienumbers.append(tempvalue)
        tempvalue = []

    return uniquenumbers, frequencienumbers

def firstfilter(noneighbours,uniquenumbers):
    stillpossible = True
    if not 0 in uniquenumbers:
        if len(noneighbours) > 0:
            stillpossible = False
    return stillpossible
def jokercount(pscolornumber):
    return pscolornumber.count(0)
def neighbourless(uniquenumbers,withneighbourstype1,withneighbourstype2):
    noneighbours = []
    for i in range(len(uniquenumbers)):
        if not((uniquenumbers[i] in withneighbourstype1) or (uniquenumbers[i] in withneighbourstype2)):
            print(uniquenumbers[i])
            noneighbours.append(uniquenumbers[i])
    return noneighbours
def extendedneighbours(uniquenumbers,jokercounted,noneighbours):
    extendedneighbour = []
    if jokercounted > 0:
        for i in range(len(noneighbours)):
            number = noneighbours[i]
            if i < 2:
                if i > len(noneighbours) - 3:
                    continue
                if number + 2 in uniquenumbers:
                    extendedneighbour.append(number)
                    continue
            if i > len(noneighbours) - 3:
                if number - 2 in uniquenumbers:
                    extendedneighbour.append(number)
                    continue
            if number - 2 in uniquenumbers or number+2 in uniquenumbers:
                extendedneighbour.append(number)
    return extendedneighbour
def secondfilter(noneighbours,extendedneighbour,jokercounted):
    possible = True
    if len(extendedneighbour) > (jokercounted*2)+1:
        possible = False
    if jokercounted == 1:
        for i in range(len(noneighbours)):
            number = noneighbours[i]
            if number in extendedneighbour:
                continue
            else:
                possible = False
    return possible
def makeallthreetilerows(uniquenumbers,jokercounted):
    threetilerows = []
    for i in range(len(uniquenumbers)):
        number = uniquenumbers[i]
        '''blauwe 3 kan --> 1,2,3 blauw
                            2,3,4 blauw
                            3,4,5 blauw
                            103,203,303
                            203,303,403
                            103,303,403
                            x3 voor jokers die die plaatsen kunnen innemen
                            (alleen 3 blauw is geforceerd om erin te zitten)
                            maximaal variaties zijn 18
                            MAAR alle normale posities waar b3 niet voraan staat mogen weg
                            
                            3,4,5 blauw -> enige zonder joker (rest waarde lager dan deze dus dan zitten ze er al in)
                            j,3,4 blauw
                            3,4,j blauw
                            3, j, 5 blauw
                            j,303,403 
                            j,j,3
                            j,3,j
                            3,j,j               
                            '''
        if jokercounted == 0:
            if i > uniquenumbers.len()-3:
                continue
            if number+1 in uniquenumbers:
                if number+2 in uniquenumbers:
                    threetilerows.append([number,number+1,number+2])
            if number+100 in uniquenumbers:
                if number+200 in uniquenumbers:
                    threetilerows.append([number, number + 100, number + 200])
                if number+300 in uniquenumbers:
                    threetilerows.append([number, number + 100, number + 300])
            if number+200 in uniquenumbers:
                if number+300 in uniquenumber:
                    threetilerows.append([number, number + 200, number + 300])
        elif jokercounted == 1:
            if i > uniquenumbers.len()-2:
                continue
            if number+1 in uniquenumbers:
                threetilerows.append([number,number+1,0])
                if number+2 in uniquenumbers:
                    threetilerows.append([number, 0, number + 2])
                    threetilerows.append([number,number+1,number+2])
            if number+100 in uniquenumbers:
                threetilerows.append([number, number + 100, 0])
                if number+200 in uniquenumbers:
                    threetilerows.append([number, number + 100, number + 200])
                if number+300 in uniquenumbers:
                    threetilerows.append([number, 0, number+300])
                    threetilerows.append([number, number + 100, number + 300])
            if number+200 in uniquenumbers:
                threetilerows.append([number, 0,number + 200])
                if number+300 in uniquenumber:
                    threetilerows.append([number, number + 200, number + 300])

        else:
            threetilerows.append([number, 0, 0])
            if number+1 in uniquenumbers:
                threetilerows.append([number,number+1,0])
                if number+2 in uniquenumbers:
                    threetilerows.append([number, 0, number + 2])
                    threetilerows.append([number,number+1,number+2])
            if number+100 in uniquenumbers:
                threetilerows.append([number, number + 100, 0])
                if number+200 in uniquenumbers:
                    threetilerows.append([number, number + 100, number + 200])
                if number+300 in uniquenumbers:
                    threetilerows.append([number, 0, number+300])
                    threetilerows.append([number, number + 100, number + 300])
            if number+200 in uniquenumbers:
                threetilerows.append([number, 0,number + 200])
                if number+300 in uniquenumber:
                    threetilerows.append([number, number + 200, number + 300])
    return threetilerows




piecescolornumber = [110,110,111,112,112,113,113,104,310]
amountofjokers = jokercount(piecescolornumber)
uniquenumber,frequencienumber = frequentielist(piecescolornumber)
n,o = whatvalueshaveneighboursbothtypes(uniquenumber)
neighbourlessnumbers = neighbourless(uniquenumber,n,o)
stillpos = firstfilter(neighbourlessnumbers,uniquenumber)
farneighbours = extendedneighbours(uniquenumber,amountofjokers,neighbourlessnumbers)
threetilerows = makeallthreetilerows(uniquenumber,jokercount)
print(uniquenumber)
print(n)
print(o)
print(stillpos)
print(threetilerows)
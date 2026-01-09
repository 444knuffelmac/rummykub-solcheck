def sortstringly(pscolornumber):
    pscolorstring = []
    pscolornumber2 =[]
    for x in range(len(pscolornumber)):
        pscolorstring.append(str(pscolornumber[x])[::-1])
    pscolorstring =sorted(pscolorstring)
    for x in range(len(pscolorstring)):
        pscolornumber2.append(int(pscolorstring[x]))
    return pscolornumber2

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
        if number % 100 == 1:
            if i+2 < len(pscolornumberalt):
                if i + 1 < len(pscolornumberalt):
                    if number + 1 == pscolornumberalt[i + 1] or number+1 == pscolornumberalt[i+2]:
                        withneighbourstype2.append(number)
                        continue
                    if number + 2 == pscolornumberalt[i + 1] or number+2 == pscolornumberalt[i+2]:
                        withneighbourstype2.append(number)
                        continue
                    if number + 3 == pscolornumberalt[i + 1] or number+3 == pscolornumberalt[i+2]:
                        withneighbourstype2.append(number)
                        continue
            elif i+1 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(number)
                    continue
                if number+2 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(number)
                    continue
                if number+3 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(number)
                    continue
        elif number%100 == 2:
            if i+2 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[i + 1] or number + 1 == pscolornumberalt[i + 2]:
                    withneighbourstype2.append(number)
                    continue
                if number + 2 == pscolornumberalt[i + 1] or number + 2 == pscolornumberalt[i + 2]:
                    withneighbourstype2.append(number)
                    continue
            elif i+1 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(number)
                    continue
                if number+2 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(number)
                    continue
            if 1<i:
                if number - 1 == pscolornumberalt[i - 1] or number - 1 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(number)
                    continue
            elif 0<i:
                if number - 1 == pscolornumberalt[i-1]:
                    withneighbourstype2.append(number)
                    continue
        elif number%100 == 3:
            if i+2 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[i + 1] or number + 1 == pscolornumberalt[i + 2]:
                    withneighbourstype2.append(number)
                    continue
            elif i+1 < len(pscolornumberalt):
                if number + 1 == pscolornumberalt[i+1]:
                    withneighbourstype2.append(number)
                    continue
            if 1 < i:
                if number - 1 == pscolornumberalt[i - 1] or number - 1 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(number)
                    continue
                if number - 2 == pscolornumberalt[i - 1] or number - 2 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(number)
                    continue
            elif 0 < i:
                if number - 1 == pscolornumberalt[i - 1]:
                    withneighbourstype2.append(number)
                    continue
                if number - 2 == pscolornumberalt[i - 1]:
                    withneighbourstype2.append(number)
                    continue
        else:
            if 1 < i:
                if number - 1 == pscolornumberalt[i - 1] or number - 1 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(number)
                    continue
                if number - 2 == pscolornumberalt[i - 1] or number - 2 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(number)
                    continue
                if number - 3 == pscolornumberalt[i - 1] or number - 3 == pscolornumberalt[i - 2]:
                    withneighbourstype2.append(number)
                    continue
            elif 0 < i:
                if number - 1 == pscolornumberalt[i - 1]:
                    withneighbourstype2.append(number)
                    continue
                if number - 2 == pscolornumberalt[i - 1]:
                    withneighbourstype2.append(number)
                    continue
                if number - 3 == pscolornumberalt[i - 1]:
                    withneighbourstype2.append(number)
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

n,o = whatvalueshaveneighboursbothtypes([101,102,104,301])
print(n)
print(o)
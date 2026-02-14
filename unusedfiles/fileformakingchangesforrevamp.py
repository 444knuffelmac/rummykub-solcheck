import time
def sortstringly(pscolornumber):
    pscolorstring = []
    pscolornumber2 =[]
    for x in range(len(pscolornumber)):
        pscolorstring.append(str(pscolornumber[x])[::-1])
    pscolorstring =sorted(pscolorstring)
    for x in range(len(pscolorstring)):
        pscolornumber2.append(int(pscolorstring[x]))
    return pscolornumber2

def sortstringly2(pscolornumber):
    pscolorstring = []
    for x in pscolornumber:
        pscolorstring.append(str(x)[::-1])
    pscolorstring =sorted(pscolorstring)
    for x in pscolorstring:
        pscolorstring[x]=(int(x))
    return pscolorstring

def sortstringly3(pscolornumber):
    return [int(s) for s in sorted([str(s)[::-1] for s in pscolornumber])]

def extendedneighbours(uniquenumbers, jokercounted, noneighbours):
    if jokercounted == 0: return []
    extendedneighbour = []
    for i in noneighbours:
        if i - 2 in uniquenumbers or i + 2 in uniquenumbers: extendedneighbour.extend(i)
    return extendedneighbour
def extendedneighbours2(uniquenumbers, jokercounted, noneighbours):
    if jokercounted == 0: return []
    extendedneighbour = []
    for i in noneighbours:
        if i - 2 in uniquenumbers or i + 2 in uniquenumbers:
            extendedneighbour.append(i)
    return extendedneighbour

def secondfilter(noneighbours, extendedneighbour, jokercounted):
    if len(extendedneighbour) > (jokercounted * 2) + 1:
        return False
    elif jokercounted == 1:
        for i in noneighbours:
            if i == 0 or i in extendedneighbour:
                continue
            else:
                return False
    return True

def beginswith1(matrixarray):
    beginwaarden = []
    for i in range(len(matrixarray)):
        beginwaarden.append(matrixarray[i][0])
    return beginwaarden

def beginswith(matrixarray):
    return [i[0] for i in matrixarray]

def mogelijkepaden2(pad, rows, beginrows):
    # pad = de lijst van overgebleven nummers in dit pad
    # confirmedpos alle mogelijke rijen in dit pad
    maybepos = []  # beginindex is juist, rest niet gechecked
    confirmedpos = []  # alles is gechecked en is correct, dus deze kunnen
    w = 0
    while pad[w] == 0:
        w += 1
    if pad[w] in beginrows:
        i = 0
        while i < len(beginrows):
            if beginrows[i] == pad[w]:
                maybepos.append(rows[i])
            i += 1
        for i in maybepos:
            k = 0
            stopped = False
            while k < len(i):
                if i[k] in pad:
                    k += 1
                    continue
                stopped = True
                break
            if not stopped:
                confirmedpos.append(i)
    return confirmedpos


def mogelijkepaden(pad, rows, beginrows):
    # pad = de lijst van overgebleven nummers in dit pad
    # confirmedpos alle mogelijke rijen in dit pad
    maybepos = []  # beginindex is juist, rest niet gechecked
    confirmedpos = []  # alles is gechecked en is correct, dus deze kunnen
    for w in pad:
        while w == 0:
            continue
        if w in beginrows:
            for i in rows:
                if i[0] == w:
                    maybepos.append(i)
            for i in maybepos:
                stopped = False
                for k in i:
                    if k in pad:
                        continue
                    stopped = True
                    break
                if not stopped:
                    confirmedpos.append(i)
    return confirmedpos




def mogelijkepaden3(pad, rows):
    # pad = de lijst van overgebleven nummers in dit pad
    # confirmedpos alle mogelijke rijen in dit pad
    beginrows = [i[0] for i in rows]
    deletablerows = rows.copy()
    for w in pad:
        while not w:
            continue
        if w in beginrows:
            for i in deletablerows:
                if i[0] == w:
                    for k in i:
                        if k in pad:
                            continue
                        deletablerows.remove(i)
                        break
    return deletablerows


def sortstringlyfinal(pscolornumber:list):
    ## sorted list of reverse ints
    return [int(s) for s in sorted([str(s)[::-1] for s in pscolornumber])]
xe = [101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,109,110,110,111,111,112,112,113,113,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,413,413,0,0,0,0,0,0,0,0]
start = time.time()
print(sortstringly(xe))
end = time.time()
print(end-start)
start = time.time()
print(sortstringlyfinal(xe))
end = time.time()
print(end-start)

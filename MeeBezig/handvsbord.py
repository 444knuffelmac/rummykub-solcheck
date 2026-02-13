
from finished import generalfunctionsimportthis
from MeeBezig import everypossiblecombinationfinder
def unlistinglist(listedlist):
    unlistedlist = []
    for xs in listedlist:
        for x in xs:
            unlistedlist.append(x)
    return unlistedlist
def amountofelementsinlistdepth1(listforcount):
    amountofelements = []
    for xs in listforcount:
        amountofelements.append(len(xs))
    return amountofelements
def amountofelementsinlistdepth2(listforcount):
    amountofelements = []
    for xs in listforcount:
        for x in xs:
            amountofelements.append(len(xs))
    return amountofelements
def mogelijkheden(inhand,outhand):
    inhandstring = ','.join(map(str, inhand))
    outhandstring = ','.join(map(str, outhand))
    pieceslist = inhandstring + "," + outhandstring
    solutions = []
    pieceslistact = pieceslist.split(',')
    pieceslistact[-1] = pieceslistact[-1].strip("\n")
    pieceslistactu = []
    verwijderd = []
    for i in pieceslistact:
        pieceslistactu.append(int(i))

    with open('../MeeBezig/afgelegdpadmetit.txt', 'r+') as f:
        f.truncate(0)
        f.seek(0)
        continueing, solution = generalfunctionsimportthis.finalcalculatorrecursive(pieceslistactu)
        with open("../finished/afgelegdpad.txt", "r+") as afegdpad:
            for dqf in afegdpad:
                dqf = dqf.split(',')
                dqf[-1] = dqf[-1].strip("\n")
                olo = []
                for o in dqf:
                    olo.append(o)
                # set list back to string
                print(olo, file=f)
            afegdpad.truncate(0)
        print(continueing, solution, file=f)
        if not continueing:
            allcombinationsinhand = everypossiblecombinationfinder.allpossiblecombinations(inhand)
            allcombinations = []
            for combination in allcombinationsinhand:
                temp2 = []
                for i in combination:
                    temp2.append(i)
                for i in outhand:
                    temp2.append(i)
                allcombinations.append(temp2)
            for combination in allcombinations:
                continueing, solution = generalfunctionsimportthis.finalcalculatorrecursive(combination)
                with open("../finished/afgelegdpad.txt", "r+") as afegdpad:
                    for dqf in afegdpad:
                        dqf = dqf.split(',')
                        dqf[-1] = dqf[-1].strip("\n")
                        olo = []
                        for o in dqf:
                            olo.append(o)
                        # set list back to string
                        print(olo, "handsverbord", file=f)
                    afegdpad.truncate(0)
                print(continueing, solution, file=f)
                if continueing:
                    pieceslistcactualint = []
                    for i in pieceslistact:
                        pieceslistcactualint.append(int(i))
                    for i in combination:
                        pieceslistcactualint.remove(i)
                    temp3 = []
                    verwijderd.append(pieceslistcactualint.copy())
                    print(temp3,"pre")
                    for i in solution:
                        temp3.append(i)
                    print(temp3,"temp3")
                    solutions.append(temp3)


        else:
            print(solution)
            solution = solution[0]
            print(solution)
            tempsolution = ["all"]
            verwijderd = [None]
            for i in solution:
                tempsolution.append(i)
            solutions.append(tempsolution)

    return solutions,verwijderd

inhnd = [101,102,103,0,110]
outhnd = [103,104,105,106,108]
mogelijk,verwijderdestukken = mogelijkheden(inhnd,outhnd)
print(mogelijk)
print(verwijderdestukken)
print(amountofelementsinlistdepth1(verwijderdestukken))
print(amountofelementsinlistdepth2(mogelijk))
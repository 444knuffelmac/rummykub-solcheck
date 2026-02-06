from finished import generalfunctionsimportthis
from MeeBezig import everypossiblecombinationfinder
def mogelijkheden(inhand,outhand):
    inhandstring = ','.join(map(str, inhand))
    outhandstring = ','.join(map(str, outhand))
    pieceslist = inhandstring + "," + outhandstring
    solutions = []
    pieceslistact = pieceslist.split(',')
    pieceslistact[-1] = pieceslistact[-1].strip("\n")
    pieceslistactu = []
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
                    temp3 = [pieceslistcactualint.copy()]
                    for i in solution:
                        temp3.append(i)
                    print(temp3)
                    solutions.append(temp3)


        else:
            print(solution)
            solution = solution[0]
            print(solution)
            tempsolution = ["all"]
            for i in solution:
                tempsolution.append(i)
            solutions.append(tempsolution)

    return solutions

inhnd = [101,102,103]
outhnd = [103,104]
mogelijk = mogelijkheden(inhnd,outhnd)
print(mogelijk)
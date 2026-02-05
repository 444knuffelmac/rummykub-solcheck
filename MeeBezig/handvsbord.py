from finished import tests
from MeeBezig import everypossiblecombinationfinder
def mogelijkheden(inhand,outhand):
    inhandstring = ','.join(map(str, inhand))
    outhandstring = ','.join(map(str, outhand))
    pieceslist = inhandstring + "," + outhandstring
    solutions = []
    with open("testvalues.txt", 'r+') as testing:
        testing.truncate(0)
        testing.seek(0)
        with open("../finished/gevondenoplossingen.txt", 'r+') as oplossingen:
            print(pieceslist)
            print(pieceslist, file=testing)
            tests.caller(False)
            isnotempty = oplossingen.read(1)
            print(isnotempty)
            if  isnotempty == None:
                allcombinationsinhand = everypossiblecombinationfinder.allpossiblecombinations(inhand)
                allcombinations = []
                for combination in allcombinationsinhand:
                    temp = ','.join(map(str, combination))
                    temp2 = outhandstring + ',' + temp
                    allcombinations.append(temp2)
                    print(allcombinations)
                    print("hlelo")
                for combination in allcombinations:
                    oplossingen.truncate(0)
                    oplossingen.seek(0)
                    testing.truncate(0)
                    testing.seek(0)
                    print(combination,file=testing)
                    tests.caller(False)
                    if oplossingen:
                        print("noep")
                        pieceslistactual = pieceslist.split(',')
                        print(pieceslistactual)
                        print(combination)
                        combinationlist = combination.split(',')
                        print(combinationlist)
                        for i in combinationlist:
                            pieceslistactual.remove(i)
                        print(pieceslistactual)
                        piecesstring = str(pieceslistactual)
                        solution = oplossingen.readline()
                        print(solution)
                        solutions.append(piecesstring + solution)


            else:
                solution = oplossingen.readline()
                print(solution)
                solutions.append("all" + solution)
    return solutions

inhnd = [1,2]
outhnd = [3,4]
mogelijk = mogelijkheden(inhnd,outhnd)
print(mogelijk)
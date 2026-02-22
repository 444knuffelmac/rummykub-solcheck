from finished import generalfunctionsimportthis
def caller(debugmode:bool):
    if debugmode:
        with open('../MeeBezig/afgelegdpadmetit.txt', 'r+') as f:
            f.truncate(0)
            f.seek(0)
            with open("../MeeBezig/testvalues") as testcases:
                with open("../finished/gevondenoplossingen.txt","w") as poi:
                    i = 1
                    for piecescolornumber in testcases:
                        print(i,"itterations")
                        print(i, "itterations",file=f)
                        i += 1
                        continued = True
                        pieceslist = piecescolornumber.split(',')
                        pieceslist[-1] = pieceslist[-1].strip("\n")
                        for l in pieceslist:
                            if not l.isdigit():
                                print("invalid pieces/no pieces")
                                print("invalid pieces/no pieces",file=f)
                                continued=False
                                break
                        if not continued:
                            continue
                        liststring =  list(map(int, pieceslist))
                        solution,solutionpath = generalfunctionsimportthis.finalcalculatorrecursive(liststring)
                        print(solution,solutionpath)
                        print(solutionpath,file=poi)
                        with open("../finished/afgelegdpad.txt", "r+") as afegdpad:
                            for dqf in afegdpad:
                                dqf = dqf.split(',')
                                dqf[-1] = dqf[-1].strip("\n")
                                olo=[]
                                for o in dqf:
                                    olo.append(o)
                                #set list back to string
                                print(olo,file=f)
                            afegdpad.truncate(0)
                        print(solution, solutionpath,file=f)

            f.close()
    else:
        with open('../MeeBezig/afgelegdpadmetit.txt', 'r+') as f:
            f.truncate(0)
            f.seek(0)
            with open("../MeeBezig/testvalues") as testcases:
                with open("../finished/gevondenoplossingen.txt","w") as poi:
                    i = 1
                    for piecescolornumber in testcases:
                        print(i, "itterations",file=f)
                        i += 1
                        continued = True
                        pieceslist = piecescolornumber.split(',')
                        pieceslist[-1] = pieceslist[-1].strip("\n")
                        for l in pieceslist:
                            if not l.isdigit():
                                print("invalid pieces/no pieces",file=f)
                                continued=False
                                break
                        if not continued:
                            continue
                        liststring =  list(map(int, pieceslist))
                        solution,solutionpath = generalfunctionsimportthis.finalcalculatorrecursive(liststring)
                        print(solution,solutionpath)
                        if solution:
                            print(solutionpath,file=poi)
                        print(solution, solutionpath,file=f)

            f.close()




from finished import generalfunctionsimportthis
with open('afgelegdpadmetit.txt','r+') as f:
    f.truncate(0)
    f.seek(0)
    with open("testvalues") as testcases:
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
                    continued=False
                    break
            if not continued:
                continue
            liststring =  list(map(int, pieceslist))
            solution,solutionpath = generalfunctionsimportthis.finalcalculatorrecursive(liststring)
            print(solution,solutionpath)
            with open("afgelegdpad.txt","r+") as afegdpad:
                for dqf in afegdpad:
                    dqf = dqf.split(',')
                    dqf[-1] = dqf[-1].strip("\n")
                    olo=[]
                    for o in dqf:
                        olo.append(o)
                    #set list back to string
                    print(olo,file=f)
                    print(olo)
                afegdpad.truncate(0)
            print(solution, solutionpath,file=f)

    f.close()
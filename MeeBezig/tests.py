from finished import generalfunctionsimportthis
with open("testvalues") as testcases:
  i = 1
  for piecescolornumber in testcases:
    print(i,"itterations")
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
    print(generalfunctionsimportthis.finalcalculatorrecursive(liststring))
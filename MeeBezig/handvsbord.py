from finished import tests
inhand = [1,2]
inhand = ','.join(map(str, inhand))
outhand = [3,4]
outhand = ','.join(map(str, outhand))
pieceslist = inhand + "," +outhand
with open("../MeeBezig/testvalues.txt", 'w') as testing:
    with open("../finished/gevondenoplossingen.txt", 'r') as oplossingen:
        print(pieceslist, file=testing)
        tests.caller()
        for lines in oplossingen:
            if lines == "None,None":



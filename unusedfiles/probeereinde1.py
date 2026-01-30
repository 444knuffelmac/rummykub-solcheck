#https://www.reddit.com/r/learnpython/comments/xttdeh/setting_one_list_equal_to_another_causes_both/
#WHY .COPY
def beginswith(matrixarray):
    beginwaarden=[]
    for i in range(len(matrixarray)):
        beginwaarden.append(matrixarray[i][0])
    return beginwaarden
def dooneminusother(array1,array2):
    templist = array1.copy()
    for l in range(len(array2)):
        print(array1)
        if array2[l] in templist:
            print(l)
            print(array2[l])
            templist.remove(array2[l])
        else:
            return array1
        l+=1
    return templist
def finalcalculator(piececolornumber,threetilerows,threetilerowsbeginwaarden,fourtilerows,fourtilerowsbeginwaarden,fivetilerows,fivetilesrowbeginwaarden,uniekenummers):
    geprobeerdeoplossingen = []
    afgelegdtraject = []
    tussenstap = piececolornumber.copy()
    oplossing = []
    oplossinggevonden = False
    mogelijkepaden = []
    einde = False
    i=0
    firstnumber = piececolornumber[0]
    #VANAF HIER IN LOOP
    while not oplossinggevonden and not einde:
        if not(firstnumber in threetilerowbeginwaarden):
         #als het er niet in zit, kan het niet
            return False,[]
        i = threetilerowsbeginwaarden.count(firstnumber) #hoeveel er beginnen met het getal
        m = 0
        indexesofthreetiles = []
        copyofthreetiles= threetilerowbeginwaarden.copy()
        while 0 < i: #THIS GIVES ALL THE INDEXES OF THE NUMBER OCCURING IN THREETILEROWS
            l = copyofthreetiles.index(firstnumber)
            indexesofthreetiles.append(l)
            copyofthreetiles[l] = 1
            i-=1
        actualtries = [] #actual rows that start with the number
        for l in indexesofthreetiles: #gives the actual rows
            actualtries.append(threetilerows[l])

        for l in actualtries: #alleen de mogelijke paden blijven over (als er wordt verwijderd worden paden die vroeger beschikbaar waarden, onbeschikbaar)
            possible=True
            for p in l:
                if not(p in tussenstap):
                    possible=False
                    break
            if not possible:
                actualtries.remove(l)


        while m < len(tussenstap):
            if m in
            m+=1






    if oplossinggevonden:
        oplossinggevonden = afgelegdtraject
    return oplossinggevonden,oplossing


#testwaarden:
piecescolornumber = [101,102,103,104,105,105,106,107,108]
threetilerow =[[101, 102, 103], [102, 103, 104], [103, 104, 105], [104, 105, 106], [105, 106, 107], [106, 107, 108]]
fourtilerow =[[101, 102, 103, 104], [102, 103, 104, 105], [103, 104, 105, 106], [104, 105, 106, 107], [105, 106, 107, 108]]
fivetilerow=[[101, 102, 103, 104, 105], [102, 103, 104, 105, 106], [103, 104, 105, 106, 107], [104, 105, 106, 107, 108]]
threetilerowbeginwaarden = beginswith(threetilerow)
fourtilerowbeginwaarden = beginswith(fourtilerow)
fivetilerowbeginwaarden = beginswith(fivetilerow)

testarray = [1,2,2,3,4]
testarray2 = [1,4]
print(dooneminusother(testarray,testarray2))

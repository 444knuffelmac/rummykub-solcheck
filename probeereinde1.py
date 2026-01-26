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
def finalcalculator(piececolornumber,threetilerows,threetilerowsbeginwaarden,fourtilerows,fourtilerowsbeginwaarden,fivetilerows,fivetilesrowbeginwaarden):
    geprobeerdeoplossing = []
    i=0 # --> UIT LOOP
    #VANAF HIER IN LOOP
    ref3 = 0
    ref4 = 0
    ref5 = 0
    k=0
    combinaties3 = []
    if piecescolornumber[i] in threetilerowsbeginwaarden:
       ref3 = threetilerowsbeginwaarden.count(piecescolornumber[i])
    if piecescolornumber[i] in fourtilerowsbeginwaarden:
       ref4 = fourtilerowsbeginwaarden.count(piecescolornumber[i])
    if piecescolornumber[i] in fivetilesrowbeginwaarden:
       ref5 = fivetilesrowbeginwaarden.count(piecescolornumber[i])
    while k < ref3:
        combinaties3.append(piececolornumber[i])



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

def beginswith(matrixarray):
    beginwaarden=[]
    for i in range(len(matrixarray)):
        beginwaarden.append(matrixarray[i][0])
    return beginwaarden
def dooneminusother(array1,array2):
    templist = array1.copy()
    for l in range(len(array2)):
        if array2[l] in templist:

            templist.remove(array2[l])
        else:
            return array1
        l+=1
    return templist
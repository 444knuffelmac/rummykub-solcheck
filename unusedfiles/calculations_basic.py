def sortstringly(pscolornumber):
    pscolorstring = []
    pscolornumber2 =[]
    for x in range(len(pscolornumber)):
        pscolorstring.append(str(pscolornumber[x]))
    pscolorstring =sorted(pscolorstring)
    for x in range(len(pscolorstring)):
        pscolornumber2.append(int(pscolorstring[x]))
    return pscolornumber2
def rijchanger(rijen,pscolornumbr,cijfer):
    rijen.append(cijfer)
    pscolornumbr.remove(cijfer)
    return rijen,pscolornumbr
def makeeveryrow(pscolornumber): #makes every possible row, longest variation (so 3,4,5,6 but not 3,4,5 as a bigger one is available)
    #if it is to small
    rows = []
    if len(pscolornumber) < 3:
        return pscolornumber,rows
    #checks for jokers
    jokeramount = pscolornumber.count(0)
    if jokeramount == 0:
        pscolornumberalt = sortstringly(pscolornumber) #presort for the other one
        k = pscolornumber[0]-1
        j=0 #amount in sequence
        p=[] # id of numbers in sequence
        #Rows with same color going up ascendly
        for i in range(len(pscolornumber)):
            if pscolornumber[i] == k+1:
                j+=1
                p.append(i)
            else:
                j=0
                p.clear()

            #If it comes up ascendendly it gets removed, this does limit it to 3 in a row at max
            if j ==3:
                l=1 #next number
                g=1 #values that are identical repeated, as to fix an error
                while pscolornumber[i+l] == k+l or pscolornumber[i+k]==k+l-g:
                        if pscolornumber[i+k]==k+l-g:
                            g+=1
                            j += 1
                        else:
                            j += 1
                            l+=1
                            p.append(i+k)

                if not(j<3):
                    if j==3:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        rows, pscolornumber  = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                    elif j==4:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        cijfer4 = pscolornumber[p[3]]
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer4)
                    elif j==5:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        cijfer4 = pscolornumber[p[3]]
                        cijfer5 = pscolornumber[p[4]]
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer4)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer5)
                    elif j==6:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        cijfer4 = pscolornumber[p[3]]
                        cijfer5 = pscolornumber[p[4]]
                        cijfer6 = pscolornumber[p[5]]
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer4)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer5)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer6)
                    elif j==7:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        cijfer4 = pscolornumber[p[3]]
                        cijfer5 = pscolornumber[p[4]]
                        cijfer6 = pscolornumber[p[5]]
                        cijfer7 = pscolornumber[p[6]]
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer4)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer5)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer6)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer7)
                    elif j==8:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        cijfer4 = pscolornumber[p[3]]
                        cijfer5 = pscolornumber[p[4]]
                        cijfer6 = pscolornumber[p[5]]
                        cijfer7 = pscolornumber[p[6]]
                        cijfer8 = pscolornumber[p[7]]
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer4)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer5)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer6)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer7)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer8)
                    elif j==9:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        cijfer4 = pscolornumber[p[3]]
                        cijfer5 = pscolornumber[p[4]]
                        cijfer6 = pscolornumber[p[5]]
                        cijfer7 = pscolornumber[p[6]]
                        cijfer8 = pscolornumber[p[7]]
                        cijfer9 = pscolornumber[p[8]]
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer4)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer5)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer6)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer7)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer8)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer9)
                    elif j==10:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        cijfer4 = pscolornumber[p[3]]
                        cijfer5 = pscolornumber[p[4]]
                        cijfer6 = pscolornumber[p[5]]
                        cijfer7 = pscolornumber[p[6]]
                        cijfer8 = pscolornumber[p[7]]
                        cijfer9 = pscolornumber[p[8]]
                        cijfer10 = pscolornumber[p[9]]
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer4)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer5)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer6)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer7)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer8)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer9)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer10)
                    elif j==11:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        cijfer4 = pscolornumber[p[3]]
                        cijfer5 = pscolornumber[p[4]]
                        cijfer6 = pscolornumber[p[5]]
                        cijfer7 = pscolornumber[p[6]]
                        cijfer8 = pscolornumber[p[7]]
                        cijfer9 = pscolornumber[p[8]]
                        cijfer10 = pscolornumber[p[9]]
                        cijfer11 = pscolornumber[p[10]]
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer4)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer5)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer6)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer7)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer8)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer9)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer10)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer11)
                    elif j==12:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        cijfer4 = pscolornumber[p[3]]
                        cijfer5 = pscolornumber[p[4]]
                        cijfer6 = pscolornumber[p[5]]
                        cijfer7 = pscolornumber[p[6]]
                        cijfer8 = pscolornumber[p[7]]
                        cijfer9 = pscolornumber[p[8]]
                        cijfer10 = pscolornumber[p[9]]
                        cijfer11 = pscolornumber[p[10]]
                        cijfer12 = pscolornumber[p[11]]
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer4)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer5)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer6)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer7)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer8)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer9)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer10)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer11)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer12)

                    elif j==13:
                        cijfer1 = pscolornumber[p[0]]
                        cijfer2 = pscolornumber[p[1]]
                        cijfer3 = pscolornumber[p[2]]
                        cijfer4 = pscolornumber[p[3]]
                        cijfer5 = pscolornumber[p[4]]
                        cijfer6 = pscolornumber[p[5]]
                        cijfer7 = pscolornumber[p[6]]
                        cijfer8 = pscolornumber[p[7]]
                        cijfer9 = pscolornumber[p[8]]
                        cijfer10 = pscolornumber[p[9]]
                        cijfer11 = pscolornumber[p[10]]
                        cijfer12 = pscolornumber[p[11]]
                        cijfer13 = pscolornumber[p[12]]
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer1)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer2)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer3)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer4)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer5)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer6)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer7)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer8)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer9)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer10)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer11)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer12)
                        rows, pscolornumber = rijchanger(rows, pscolornumber, cijfer13)

                    j=0

        #rows with other color but same value

        for i in range(len(pscolornumberalt)):


    return pscolornumber

pscolornumberer = [5,5]
pscolornumberothersort =sortstringly(pscolornumberer)
pscolornumberer.sort()
trymakerow(pscolornumberer)
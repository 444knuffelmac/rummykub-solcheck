from finished import listallrowsfunctry

def allpossiblecombinations(numbers):
    uniquenumbers, freqlist = listallrowsfunctry.frequentielist(numbers)
    combinations = []
    i=0
    while i < len(uniquenumbers):
        subcombinations = []
        inumber = uniquenumbers[i]
        amount = freqlist[i][1]
        subcombinations.append([inumber])
        if amount >1:
            subcombinations.append([inumber,inumber])
        k=i+1
        while k< len(uniquenumbers):
            amountofk = freqlist[k][1]
            shorttermcombinations = subcombinations.copy()
            for l in shorttermcombinations:
                temporvalue = []
                for m in l:
                    temporvalue.append(m)
                temporvalue.append(uniquenumbers[k])
                if not(len(temporvalue) == len(numbers)):
                    temporvalue.sort()
                    subcombinations.append(temporvalue)
            if amountofk == 2:
                shorttermcombinations = subcombinations.copy()
                for l in shorttermcombinations:
                    temporvalue = []
                    for m in l:
                        temporvalue.append(m)
                    temporvalue.append(uniquenumbers[k])
                    if not (len(temporvalue) == len(numbers)):
                        temporvalue.sort()
                        if not(temporvalue in subcombinations):
                            subcombinations.append(temporvalue)
            k+=1
        for m in subcombinations:
            combinations.append(m)
        i+=1
    return combinations
print(allpossiblecombinations([1,2,3]))
print(allpossiblecombinations([1,2,2,3]))

'''
        wat wil ik dat deze code doet:
        maxlength van output = len(input)-1
        minlen = 1 (dus geen lege, behalve als input leeg is)
        geeft alle waarden terug
        input = [1,2,3]
        output = [[1],[1,2],[1,3],[2],[2,3],[3]
        
        input = [1,2,2,3]
        output = [[1],[1,2],[1,3],[1,2,2],[1,2,3],[2],[2,2],[2,3],[2,2,3],[3]
                '''
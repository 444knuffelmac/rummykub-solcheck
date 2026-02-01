def thirthfilter(uniquenumbers,threetilerows):
    notinit = False
    print(uniquenumbers)
    for i in uniquenumbers:
        if i == 0:
            continue
        if not (i in threetilerows):
            notinit = True
            break
    return notinit
def workingthirthfilter(uniquenumbers,threetilerows):
    init = False
    print(uniquenumbers)
    for i in uniquenumbers:
        if i == 0:
            continue
        init = False
        for k in threetilerows:
            if not (i in k):
                continue
            init = True
            break
        if not init:
            break
    return init
array1 = [[1,2,3],[2,3,4]]
possiblenumbers = [1,2,3,4,5]
print(workingthirthfilter(possiblenumbers,array1))
possiblenumbers = [1,2,3,4]
print(workingthirthfilter(possiblenumbers,array1))
#array2 = [1,2,3,2,3,4]
#thirthfilter(possiblenumbers,array2)
'''for i in possiblenumbers:
    if i in array1:
        print(i)'''
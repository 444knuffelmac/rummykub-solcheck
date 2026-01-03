ln = int(input("nl or en?"))
jokercount=0
piecescolornumber = []
if ln=="nl":
    ln=False
else:
    ln=True
if ln:
    pobc = int( input("total amount of pieces on board")) #pobc = pieces on board count
    pih = int( input("total amount of pieces in your hand")) #pih = pieces in hand
    #totaalstukken
    for pobc in range(0,pobc):
        j=0 #jokerthisinput
        colorpiece=input("yellow/green,red,blue,black and joker")
        if colorpiece[0]=="y" or colorpiece[0]=="g":
            colorpiece="y"
        elif colorpiece[0]=="r":
            colorpiece="r"
        elif colorpiece[0]=="b" and colorpiece[1]=="l" and colorpiece[2]=="u":
            colorpiece="blu"
        elif colorpiece[0] == "j":
            jokercount+=1
            j=1
        else:
            colorpiece="bla"
        if j!=1:
            piecenumber=int(input("number 1-13"))
            if 0< piecenumber < 14:
                piece=colorpiece+str(piecenumber)
                piecescolornumber.append(piece)


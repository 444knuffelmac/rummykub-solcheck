ln = input("nl or en?")
piecescolornumber = []
def inputwithpiece():
    j = 0  # jokerthisinput
    colorpiece = input("yellow/green,red,blue,black and joker").lower()
    if colorpiece[0] == "y" or colorpiece[0] == "g":
        colorpiece = 100
    elif colorpiece[0] == "r":
        colorpiece = 200
    elif colorpiece[0] == "b" and colorpiece[1] == "l" and colorpiece[2] == "u":
        colorpiece = 300
    elif colorpiece[0] == "j":
        colorpiece = 0
        j = 1
    else:
        colorpiece = 400
    if j != 1:
        piecenumber = int(input("number 1-13"))
        if 0 < piecenumber < 14:
            piece = colorpiece + piecenumber
            piecescolornumber.append(piece)
    else:
        piecescolornumber.append(colorpiece)
if ln=="nl":
    ln=False
else:
    ln=True
if ln:
    pobc = int( input("total amount of pieces on board")) #pobc = pieces on board count
    pih = int( input("total amount of pieces in your hand")) #pih = pieces in hand
    #totaalstukken
    for i in range(pobc):
        inputwithpiece()

    for i in range(pih):
        inputwithpiece()
print(piecescolornumber)
piecescolornumber.sort()
print(piecescolornumber)
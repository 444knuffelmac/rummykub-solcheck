# rummikub sol(vability)check(er)
python project checking if the position is able to be solved in rumikub
rumikub pieces:
1-13 in 4 colors --> yellow-black-blue-red OR green,red,black,blue OR (in the older version (still has the colors but with the symbols of normal cards)
2 jokers (we for some reason have more(8) but for the beginning this is enough)
rules:

allowed rows (beginning has same rows excluding jokers)
3 or more pieces have to be set down following atleast one of these:
  1: they are the same color and go linearly up (1,2,3 in blue or 6,7,8,9.10 in black for example)
  2: same number NOT same color (2 in blue,black,red for example BUT NOT: 2 in blue, blue, red)
  3: same as 1 and 2 but joker can replace any of the pieces (for example: 1, joker, 3 in blue (joker color doesnt matter))
  3 CANNOT be used in the beginning
  moving pieces that are layed down is allowed BUT need to stay in the rules (so if 3,4,5 in blue is layed down, you can take the blue 3 and use it in 3 green and black, but 4,5 in blue needs to return to be 3 pieces in a row so you could add a blue 6 at the end)

beginning (not included atleast not until the rest is done or i want to do this)
everyone gets 14 pieces, randomly selected
to start placing down your pieces OR moving other pieces OR placing down jokers
you need to get 30 points (or more) in value down in 1 turn, otherwise you cant start
  to get to the 30 points you are allowed to set multiple lines down, but NO joker or other persons piece can be used to get the 30 in this turn

after you have layed the 30 points down, you are allowed to do the normal row rules from the next turn.
game ends when 1 person has no pieces left OR if nobody except one has no pieces left (house rules)

if a joker is layed down, it can be used as another piece, for example: 1,2,3 in blue with joker at the end, joker can be used in 10 in blue and yellow to complete the row (10 bluem, 10 yellow, joker)


this project is just a way to check if a certain position has a valid solution as it can get very complex to see if there is a valid solution with the pieces you have left.

base functions to add: (not sure as this is an extremely difficult project to visualise before starting)
1: row maker
2: joker inclusion
3: validation checker
additional functions to add:
1: add your hand (so the pieces you have left) and the program will try to minimise your pieces left
  if you have a joker, and it cant lay everything out (even with your joker in hand) it will go to the most optimal solution that minimises your pieces left but tries to save your joker
    for example: you have 8 pieces left, including a joker, the program finds no way to include your full hand and finish the game, but it has the choice of:
      1: placing 7 pieces down, but losing your joker (so leaving you with 1 piece but no joker)
      2: placing 6 pieces down, but keeping your joker (so leaving you with 1 piece and a joker)
      2 is more optimal as you can do more, so it should do that, but if we say try to minimise pieces it will choose the upper one.

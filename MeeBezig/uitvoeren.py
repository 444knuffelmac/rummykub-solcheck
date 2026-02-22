import time
import shelve
import cProfile
from chqngesforfulllooper import ispossible,finalcalculatorrecursive

piecescolornumber = [101,101,102,102,103,103,104,104,105,105,106,106,107,107,108,108,109,110,110,111,112,112,113,113,201,201,202,202,203,203,204,204,205,205,206,206,207,207,208,208,209,209,210,210,211,211,212,212,213,213,301,301,302,302,303,303,304,304,305,305,306,306,307,307,308,308,309,309,310,310,311,311,312,312,313,313,401,401,402,402,403,403,404,404,405,405,406,406,407,407,408,408,409,409,410,410,411,411,412,412,413,413]
with shelve.open('savefilefornewimport') as memoryd:
    memoryd.clear()
    start = time.time()
    cProfile.run('finalcalculatorrecursive(piecescolornumber, memoryd)')
    end = time.time()
    print(end - start)
    print(ispossible(piecescolornumber))
    start = time.time()
    cProfile.run('finalcalculatorrecursive(piecescolornumber, memoryd)')
    end = time.time()
    print(end - start)
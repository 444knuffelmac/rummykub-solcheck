from chqngesforfulllooper import ispossible
def krijginput(allemogelijkestukken,nieuwestukken,algelegdestukken):
    gelegdestukkenunverified = nieuwestukken.copy()
    for n in algelegdestukken:
        gelegdestukkenunverified.append(n)
    oplossing = ispossible(allemogelijkestukken)
    if oplossing:

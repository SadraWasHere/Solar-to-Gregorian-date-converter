from datetime import datetime , date , time
def SolToGreg(dt):
    shamsi = datetime(2005, 12, 24)
    miladi = datetime(1384, 10, 3)
    delta = shamsi - miladi

    return (dt - delta)

def GregToSol(dt):
    shamsi = datetime(2005, 12, 24)
    miladi = datetime(1384, 10, 3)
    delta = shamsi - miladi

    return (dt + delta)
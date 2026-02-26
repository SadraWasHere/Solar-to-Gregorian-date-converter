from datetime import datetime , date , time
def GregToSol(dt):
    shamsi = datetime(2005, 12, 24)
    miladi = datetime(1384, 10, 3)
    delta = shamsi - miladi

    return (dt - delta)

def SolToGreg(dt):
    shamsi = datetime(2005, 12, 24)
    miladi = datetime(1384, 10, 3)
    delta = shamsi - miladi

    return (dt + delta)

def AutoConv(dt):
    shamsi = datetime(2005, 12, 24)
    miladi = datetime(1384, 10, 3)
    delta = shamsi - miladi

    if int(dt.strftime("%Y")) < 1500:
        return (dt + delta)
    else:
        return (dt - delta)
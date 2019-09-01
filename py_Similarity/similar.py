from math import cos,sqrt,acos

def similar(a_vect,b_vect):
    Cos = 0
    dot_total = 0.0
    a_norm = 0.0
    b_norm = 0.0
    for a,b in zip(a_vect,b_vect):
        dot_total += a*b
        a_norm += a**2
        b_norm += b**2
    if a_norm == 0 or b_norm == 0:
        Cos = 0
    elif dot_total < 0:
        Cos = cos(acos(dot_total/sqrt(a_norm*b_norm))/2)
    else:
        Cos = dot_total/sqrt(a_norm*b_norm)
    return  round(Cos,6)
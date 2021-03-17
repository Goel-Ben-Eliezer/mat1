def XtimesY(x,y):
    if x<=0:
        return 0.0
    w=exponent(y*Ln(x))
    return float(w)


def exponent(x):
    i=1
    e_x=x
    calc=x
    a=1
    while i<150:
        calc=calc*x
        a=a*(i+1)
        e_x=e_x+calc/(a)
        i=i+1
    e_x=e_x+1      
    return float(e_x)


def Ln(x):
    if x<=0:
        return 0.0
    yn=0
    i=0
    while i<1000:
        yn=yn+2*(x-exponent(yn))/(x+exponent(yn))
        i=i+1
    return float(yn)

def sqrt(x, y):
    if y<=0 or x==0:
        return 0.0
    x=1/x
    res=XtimesY(y, x)
    return float(res)


def calculate(x):
   if x<=0:
        return 0.0
   calcul=exponent(x)*XtimesY(7, x)*XtimesY(x, -1)*sqrt(x, x)
   return calcul

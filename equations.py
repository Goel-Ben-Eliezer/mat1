def XtimesY(x,y):
    if x<=0:
        return 0
    w=exp(y*ln(x))
    return float(w)


def exp(x):
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


def ln(x):
    yn=0
    i=0
    while i<1000:
        yn=yn+2*(x-exp(yn))/(x+exp(yn))
        i=i+1
    return float(yn)

def sqrt(x, y):
    x=1/x
    res=XtimesY(y, x)
    return float(res)


def calculate(x):
   calcul=exp(x)*XtimesY(7, x)*XtimesY(x, -1)*sqrt(x, x)
   return calcul

print(calculate(float(input(''))))

    
    
    
    
    
    
    
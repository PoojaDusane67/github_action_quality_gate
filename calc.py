# this is the source code
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b==0:
        raise ValueError("cannot divide by zero")
    
    return a/b
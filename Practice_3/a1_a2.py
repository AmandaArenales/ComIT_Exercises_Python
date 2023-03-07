def a2 (x):
    x = x / 2
    print (x)
    return x 


def a1():
    x = 10
    print (x * 5) 
    x = a2 (x * 2) 
    x = x * 2 
    a2(x)
a1()


"""Write an algorithm and a sub-algorithm. 
Write two variables with the same name and the compiler does not show error."""

def sub_algorithm():
    x = "This is a variable from sub_algorithm"
    print (x)

def algorithm():
    x = "This is a variable from the algorithm"
    print (x)
    sub_algorithm()

algorithm()

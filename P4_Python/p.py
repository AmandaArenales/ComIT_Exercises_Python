import string

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
number = [ "{}".format(i) for i in range(0, 10)]
[upper.extend(l) for l in (lower, number)]
print(upper)
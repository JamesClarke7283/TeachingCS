import functools

l = [1, 2, 3, 4, 5]


def f(num):
    return num % 2 == 1


#s = list(map(f, l))
s = list(functools.reduce(f,l))
 # filter,map
print(s)

def plus(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    return a + b

plus(1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, hello=True, aa=True, df=True, fdf=True, helasssdlfk=True)

def calculator(*args):
    result = 0
    for number in args:
        result += number
    print(result)

calculator(1, 2, 1, 1, 3, 1, 1, 1, 7, 1, 4, 1)

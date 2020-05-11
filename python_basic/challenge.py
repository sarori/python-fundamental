def plus(x, y):
    return int(x) + int(y)

def minus(x, y):
    return int(x) - int(y)

def mul(x, y):
    return int(x) * int (y)

def negation(x):
    return int(x) * -1

def division(x, y):
    if (x > 0 and y > 0):
        return int(x) / int(y)
    else:
        print("Enter correct number")
        return ;

def res(x, y):
    if (x > 0 and y > 0):
        return int(x) % int(y)
    else:
        print("Enter correct number")
        return ;

def power(x, y):
    if y < 0:
        res = int(x) * power(int(x), int(y) * -1 - 1)
        return 1 / res
    if y == 0:
        return 1
    return int(x) * power(int(x), int(y) - 1)


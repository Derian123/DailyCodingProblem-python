# cons(a, b) constructs a pair, and car(pair) and cdr(pair)
# returns the first and last element of that pair. For example,
# car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def getx(a, b):
        return a
    x = pair(getx)
    return x


# x = pair(lambda a, b: a) lambda way


def cdr(pair):
    def gety(a, b):
        return b
    y = pair(gety)
    return y


# x = pair(lambda a, b: a) lambda way


def main():
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))

main()

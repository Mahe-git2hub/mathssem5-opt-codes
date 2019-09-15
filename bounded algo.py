import random

import matplotlib.pyplot as plt
import numpy as np


def fun(x: float) -> float:
    try:
        y = ((x ** 2) + 54 / x)
    except ZeroDivisionError:
        y = np.Inf
    return y


def func(x: list) -> list:
    arr = []
    for i in x:
        try:
            arr.append(i ** 2 + 54 / i)
        except ZeroDivisionError:
            arr.append(np.Inf)
    return arr


# noinspection PyTypeChecker
def bounded_algo(aa, bb, inc):
    should_reiterate = True
    xi = 0
    ran = []
    y = (lambda input: fun(input))
    while should_reiterate:
        ran = np.arange(aa, bb + 1, inc)
        print(ran)
        xi = random.choice(ran)
        sub = xi - abs(inc)
        add = xi + abs(inc)
        # sleep(4.0)
        # output = [y(sub),y(xi),y(add)]
        # print(output)
        # sleep(100)
        if (y(sub) >= y(xi)) and (y(xi) >= y(add)):
            inc = abs(inc)
            # print("from 1")
            should_reiterate = False
        elif (y(sub) <= y(xi)) and (y(xi) <= y(add)):
            inc = -inc
            # print("from 2")
            should_reiterate = False
        else:
            pass
    xx = boundader(xi, inc)
    x = xi
    while True:
        if y(xx) < y(x):
            x = xx
            xx = boundader(x, inc)
        else:
            print("The optimum lies in the range of ", xx + 1, " and ", x - 1)
            plt.plot(np.arange(x - 1, xx + 2), func(np.arange(x - 1, xx + 2)), 'r-')
            # plt.show()
            plt.plot(np.arange(aa - 1, bb + 1, inc), func(np.arange(aa - 1, bb + 1, inc)), 'b')
            plt.show()
            break


def boundader(x, inc):
    return x + ((2 ** x) * inc)


if __name__ == '__main__':
    print("Remember to update function")
    a = int(input("enter the base range\t"))
    b = int(input("enter the upper range\t"))
    c = float(input("Enter the increment value\t"))
    bounded_algo(a, b, c)

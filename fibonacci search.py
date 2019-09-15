import matplotlib.pyplot as plt
import numpy as np


def fib_search(lowerbound, upperbound, numberofiterations):
    left = lowerbound
    right = upperbound
    fib = [1, 1]
    yy = []
    for i in range(numberofiterations + 3):
        fib.append(fib[-1] + fib[-2])
    length = upperbound - lowerbound
    for i in range(1, numberofiterations + 1):
        lk = (fib[numberofiterations - i + 2] / fib[numberofiterations + 2]) * length
        x1 = left + lk
        x2 = right - lk
        if x1 not in yy:
            yy.append(x1)
        if x2 not in yy:
            yy.append(x2)
        if func(x1) < func(x2):
            right = x2
        elif func(x1) > func(x2):
            left = x1
        else:
            left = x1
            right = x2
    x = np.linspace(lowerbound, upperbound, len(yy))
    yy.sort()
    y = func(yy, 2)
    plt.plot(np.arange(lowerbound, upperbound, 100), func(np.arange(lowerbound, upperbound, 100), choice=2))
    plt.plot(x, y, 'b+')
    plt.show()


# noinspection PyTypeChecker
def func(x: object, choice: object = 1) -> object:
    """

    :param choice: int
    :type x: int
    """
    if choice == 1:
        return ((x ** 2) - (10 * x) + 2) * np.exp(0.1 * x)
    else:
        return [func(i, choice=1) for i in x]


if __name__ == '__main__':
    lowerr = int(input("Enter the lower bound of the search\t"))
    uperr = int(input("Enter the upper bound of the search\t"))
    n = int(input("Enter the number of iterations\t"))
    fib_search(lowerr, uperr, n)

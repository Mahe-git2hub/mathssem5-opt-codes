import matplotlib.pyplot as plt
import numpy as np


def interval_halving(lowerbound, upperbound) -> None:
    a = lowerbound
    b = upperbound
    k = True
    while k:
        l = b - a
        xm = (lowerbound + upperbound) / 2
        x1 = a + l / 4
        x2 = b - l / 4
        if function(x1) < function(xm):
            b = xm
            xm = x1
        elif function(x2) < function(xm):
            a = xm
            xm = x2
        else:
            a = x1
            b = x2
        l = b - a
        if l < 0.6:
            plt.plot(np.arange(lowerbound, upperbound + 1, 0.5),
                     function(np.arange(lowerbound, upperbound + 1, 0.5), 2))
            plt.show()
            k = False
            break


def function(var, choice=1):
    if choice == 1:
        try:
            y = ((var ** 2) + 54 / var)
        except ZeroDivisionError:
            y = np.Inf
        return y
    elif choice == 2:
        arr = []
        for i in var:
            try:
                arr.append(i ** 2 + 54 / i)
            except ZeroDivisionError:
                arr.append(np.Inf)
        return arr
    else:
        raise Exception("Invalid choice")
        return None


if __name__ == '__main__':
    # try:
    lowerr = int(input("Enter the lower bound of the interval"))
    # except Exception as e:
    #     traceback.print_exc()
    #     e.with_traceback()
    upperr = int(input("Enter the upper bound of the interval"))
    interval_halving(lowerr, upperr)

import matplotlib.pyplot as plt
import numpy as np


def exhaustive_search(a, b, inc):
    ran = np.arange(a, b, inc)
    # print(ran)
    y = func(ran.__array__())
    # print(y)
    plt.plot(ran, y)
    i: int
    for i in range(1, len(y) - 1):
        if (y[i - 1] > y[i] and y[i + 1] > y[i]) or (y[i] > y[i - 1] and y[i] > y[i + 1]):
            print("Approximate local optima is ", ran[i])
            plt.plot(ran[0:i], y[0:i], 'r+')
            break
        elif y[-1] > y[-2] and i == len(y) - 2:
            # print("local optima is ", y[-1])
            print("local minimum is ", a)
            print("local maximum is ", b)
            plt.plot(ran[0:i], y[0:i])
            break
        elif y[-1] < y[-2] and i == len(y) - 2:
            # print("local optima is ",y[0])
            print("local minimum is ", b)
            print("local maximum is ", a)
            plt.plot(ran[0:i], y[0:i])
            break
    plt.show()


def func(x: list) -> list:
    arr = []
    for i in x:
        try:
            arr.append(i ** 2 + 54 / i)
        except ZeroDivisionError:
            arr.append(np.Inf)
    return arr


def fun(x: float) -> float:
    try:
        y = ((x ** 2) + 54 / x)
    except ZeroDivisionError:
        y = np.Inf
    return y


if __name__ == "__main__":
    print("Remember to update function")
    a = int(input("enter the base range\t"))
    b = int(input("enter the upper range\t"))
    c = float(input("Enter the increment value\t"))
    exhaustive_search(a, b, c)

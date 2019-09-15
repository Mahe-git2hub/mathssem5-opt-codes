import scipy.optimize as op


def gss():
    res = op.golden(func, full_output=True, maxiter=numberofiter)
    return res


def nr(x0: float, num):
    res = op.newton(func=func, x0=x0, fprime=lambda x: 2 * x - 5, full_output=True, maxiter=num)
    return res


def secant(x0, num):
    # for secant method
    res = op.newton(func, x0=x0, maxiter=num)
    return res


def bisectionsearch(lower, upper):
    try:
        res = op.bisect(func, lower, upper)
        return res
    except ValueError:
        print("Invalid func args")


if __name__ == '__main__':
    func = lambda x: x ** 2 - 5 * x + 6
    low = int(input("Enter the lower bound"))
    upp = int(input("Enter the upper bound"))
    choice = int(input("Enter 1 for Golden Section Search\nEnter 2 for newton-raphson method\nEnter 3 for bisection "
                       "search\nDefault secant method "))
    numberofiter = int(input("Enter the number of iterations\t"))
    if choice == 1:
        result = gss()
        print(result)
    elif choice == 2:
        result = nr(float(low), numberofiter)
        print(result)
    elif choice == 3:
        resi = bisectionsearch(low, upp)
        print(resi)
    else:
        resi = secant(float(low), numberofiter)
        print(resi)

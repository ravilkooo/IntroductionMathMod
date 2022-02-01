import math


def deriv(func, eps):
    def f1(x):
        return (func(x + eps) - func(x)) / eps

    return f1


def dihotMethod(func, a, b, eps):
    f1 = func(a)
    f2 = func(b)
    if f1 * f2 > 0:
        return a - 1
    while abs(b - a) > eps:
        t = (a + b) / 2
        f2 = func(t)
        if f1 * f2 > 0:
            a = t
        else:
            b = t
    return (a + b) / 2


def NewtonMethod(func, a, b, eps):
    f_1deriv = deriv(func, eps)
    f_2deriv = deriv(f_1deriv, eps)
    x = a
    h = eps + 1
    if func(b) * f_2deriv(b) > 0:
        x = b
    while abs(h) > eps:
        h = func(x) / f_1deriv(x)
        x -= h
    return x


def secantMethod(func, a, b, eps):
    f1 = func(a)
    f2 = func(b)
    if f1 * f2 > 0:
        return a - 1
    f_1deriv = deriv(func, eps)
    f_2deriv = deriv(f_1deriv, eps)
    z = a
    x = b
    left = func(a) * f_2deriv(a) > 0
    h = eps + 1
    if not left:
        z = b
        x = a
    while abs(h) > eps:
        h = (z - x) * func(x) / (func(x) - func(z))
        x = x + h
    return x

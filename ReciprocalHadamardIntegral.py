import mpmath as mp
mp.mp.dps = 100


def H(x):
    Q = (mp.sin(mp.pi*x) / (2*mp.pi))*(mp.psi(0, x/2) - mp.psi(0, (x+1)/2))
    return mp.gamma(x)*(1+Q)


def RH(x):
    return 1/(H(x))


def reciprocal_gamma(x):
    return 1/mp.gamma(x)


def g(x):
    return (x/2) * (mp.psi(0, (x+1)/2) - mp.psi(0, x/2)) - 1/2


def p(x):
    return 1 - g(x) * mp.sin(mp.pi * x) / (mp.pi * x)


def L(x):
    return mp.gamma(x + 1)*p(x)


def RL(x):
    return 1/L(x)


def gg(x, a):
    return (x/2) * (mp.psi(0, (x+1)/2) - mp.psi(0, x/2)) - a/2


def pg(x, a):
    return 1 - gg(x, a) * mp.sin(mp.pi * x) / (mp.pi * x)


def Lg(x, a):
    return mp.gamma(x + 1)*pg(x, a)


def Integ(a):
    def f(x):
        return 1/Lg(x, a)

    return mp.quad(f, (0, mp.inf))

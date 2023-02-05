import mpmath as mp
mp.mp.dps = 200 # number of decimal places used during computation


def h_recip(x):  #defn of Hadamard gamma function
    q = (mp.sin(mp.pi*x) / (2*mp.pi))*(mp.psi(0, x/2) - mp.psi(0, (x+1)/2))
    return 1/(mp.gamma(x) * (1 + q))


print(mp.quad(h_recip, (0, mp.inf), error=True))

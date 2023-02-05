import mpmath as mp
mp.mp.dps = 400  # number of decimal places used during computation


def h_recip(x):  # defn of Hadamard gamma function
    q = (mp.sin(mp.pi*x) / (2*mp.pi))*(mp.psi(0, x/2) - mp.psi(0, (x+1)/2))
    return 1/(mp.gamma(x) * (1 + q))


w = mp.quad(h_recip, (0, mp.inf), error=True)
print(w[0])  # value
print(w[1])  # estimated error

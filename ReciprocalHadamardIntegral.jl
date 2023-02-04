import Pkg; Pkg.add("QuadGK"); Pkg.add("SpecialFunctions")
using SpecialFunctions, QuadGK

hadamard_gamma(x) = gamma(x) * (1 + sin(π*x) * (digamma(x / 2) - digamma((x + 1) / 2)) / (2*π))
recip_hadamard(x) = 1/hadamard_gamma(x)

function give_decimal_expansion(tol)
    return quadgk(recip_hadamard, 0, Inf)
end
print(give_decimal_expansion(1e-10))

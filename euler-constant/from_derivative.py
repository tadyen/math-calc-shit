# calculate Euler's number e via its derivative definition
# e is approx 2.71828
# The derivative definition is: d[e^x]/dx = e^x
# in other words, if F(x) = f(x) then f(x) = e^x
#
# we make a guess g, around x = 1, such that
#   g = ae
# and our psueudo-exp func,
#   pexp(x) = (ae) ** x
#
# since (ae)^x = e ^ (ln(a) * x)
# thus d/dx {pexp}(x) = ln(a) * pexp(x)
#
# in which
#   pexp(1) = ae = g
#   d = d/dx {pexp}(1) = ln(a) * g
#
# by definition, ln(a)
#   < 0 if {a is complex}
#   == 0 if {a == 1}
#   == 1 if {a == e}
#   > 1 if {a > e}
# and knowing that e^x is a monotonic increasing function,
# thus
#   ln(a) between [0, 1] for a in [1, e]
#   {ln(a) > 1} for {a > e}
# thus
#   if d > g, then ln(a) > 1, decrease g
#   if d < g, then ln(a) < 1, increase g
#   if d == g, then ln(a) == 1, and thus a == e
# strategy:
#   new_g = g * (g/d)

from typing import Any
from collections.abc import Callable, Mapping

diff = lambda a,b : abs(a-b)

def first_principle_derivative(f: Callable[[float], float] ,
                               x: float,
                               h: float) -> float | None:
  try:
    result = (f(x + h) - f(x)) / h
    return result
  except:
    return None

def euler_number_from_derivative(tolerance: float, x: float, init_e: float) -> float:
  counter: int = 0

  def __recurse(counter: int, guess: float) -> float:
    psuedo_exp = lambda x: guess ** x
    d = first_principle_derivative( psuedo_exp, x, tolerance )
    assert(d is not None and d is not complex)
    new_guess = guess * (guess / d)

    print(f"Recurse:{counter}, g:{guess}, d:{d}" )
    counter = counter + 1

    if( diff(d, guess ) > tolerance ):
      return __recurse( counter, new_guess )
    else:
      return guess

  return __recurse(counter, init_e)

if __name__ == "__main__":
  euler_number_from_derivative(1e-8, 1, 2)

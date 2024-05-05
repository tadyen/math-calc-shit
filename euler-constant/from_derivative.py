# calculate e via its derivative definition recursively

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
    pexp = lambda x: guess ** x
    d = first_principle_derivative( pexp, x, tolerance )
    assert(d is not None and d is not complex)
    new_guess = guess * (pexp(x) / d)

    print(f"Recurse:{counter}, g:{guess}, d:{d}" )
    counter = counter + 1

    if( diff(d, guess ) > tolerance ):
      return __recurse( counter, new_guess )
    else:
      return guess

  return __recurse(counter, init_e)

if __name__ == "__main__":
  euler_number_from_derivative(1e-6, 1, 200)

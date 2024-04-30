#!/usr/bin/env python
import sys
from _main import main

'''
extract binary length of integer
'''
def bin_len(n: int) -> int:
  ret = 0
  while n > 0:
    n = n >> 1
    ret += 1
  return ret

def cheap_isPrime(n):
  # an approx to sqrt is halving the digits.
  m = 1 << ( bin_len(n) >> 1)
  for i in range(2, m):
    if n % i == 0:
      return False
  return True

if __name__ == '__main__':
  main(cheap_isPrime)

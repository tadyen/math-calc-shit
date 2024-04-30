#!/usr/bin/env python
import sys
from isPrime import isPrime
from _main import main

'''
Attempting to skip integers by recursing its own definition to make it more efficient,
actually makes it worse. This is less efficient than isPrime() but it still works.
'''
def isPrime2(n):
  for i in range(2, int(n ** 0.5)+1):
    if isPrime(i) and n % i == 0:
      return False
    else:
      pass
  return True

if __name__ == '__main__':
  main(isPrime2)

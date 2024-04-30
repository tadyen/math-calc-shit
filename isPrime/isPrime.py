#!/usr/bin/env python
import sys
from main import main

def isPrime(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

if __name__ == '__main__':
  main(isPrime)

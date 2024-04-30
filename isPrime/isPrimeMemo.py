#!/usr/bin/env python
import sys
from typing import Callable

from _main import main
from cheap_isPrime import cheap_isPrime

class PrimeRecord():
  _record: dict[int, bool]
  _isPrime: Callable[[int], bool]

  def __init__(self):
    self._record = {}
    self._isPrime = cheap_isPrime
    return

  def _updateRecord(self, n: int):
    # once added cannot be modified
    if n not in self._record:
      self._record.update({n: self._isPrime(n)})
    return

  def isPrime(self, n):
    if n not in self._record:
      self._updateRecord(n)
    return self._record[n]

def isPrimeMemo(n):
  record = PrimeRecord()
  return record.isPrime(n)

if __name__ == '__main__':
  main(isPrimeMemo)

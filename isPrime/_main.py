import sys
from typing import Callable

def main(callback: Callable[[int], bool]):
  assert(callable(callback))
  if len(sys.argv) < 2:
    print("requires an argument (number)")
    return -1
  try:
    n = int(sys.argv[1])
  except:
    raise ValueError("invalid input type (should be an integer)")
  print(callback(n))
  return 0

if __name__ == "__main__":
  raise Exception(f"{__file__} should not be called directly. It is a helper module.")

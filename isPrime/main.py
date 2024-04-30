import sys

def main(callback):
  assert(callable(callable))
  if len(sys.argv) < 2:
    print("requires an argument (number)")
    return -1
  try:
    n = int(sys.argv[1])
  except:
    raise ValueError("invalid input type (should be an integer)")
  print(callback(n))
  return 0

# the isPrime algo

isPrime is well known function and is practically curriculum'd.

So why am I re-doing this? Just an exercise for myself to actually understand how it works.

## implementations

- [isPrime](#isprime)
- [isPrime2](#isprime2)
- [isPrimeMemo](#isprimememo)

## isPrime

The following is the algo implemented in python:

``` python
def isPrime(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True
```

## how it works??

note: *range(a,b) in python iterates a : b-1*

### steps

- iterate from 2 to floor(sqrt(n))
- n % i == 0 ? false : true
- the value of n does not get modified

### explanation

``` txt
(n % i == 0)
  ? (n is divisible by i thus not a prime)
  : (may be a prime?)

(i == 1) will give a trivial 0 (because anything % 1 == 0) hence we start iterating at 2

From the fundamental theorem of arithmatic (FToA), all integers can be broken into their unique prime factorisation.
  Given a non-prime N, with a factorisation of
    N = P * m   where P is a prime, m is the quotient,
    then the smallest value of P must be <= sqrt(N)
      this is because
        if smallest P > sqrt(N),
        then m must contain a Prime factor > P (by FToA)
        but if so, then P * m > P ** 2 > N (since P > sqrt(N))
        which contradicts N = P * m

  thus smallest P is an integer between 2 and sqrt(N)
  if all integers between 2 and sqrt(N) are tested, and P is not found
  then N must be a prime number itself and does not obey N = P * m

  thus the algorithm works by:
    - test every integer between 2 and sqrt(N) for possible P in N = P * m
    - if P is found, N is not prime
    - if P is not found, N is prime

tl:dr
  it's a lazy brute force algo testing all possible integers as a factor of N.
  you dont have to test past sqrt(N) due to symmetry (ie. a * b = b * a).
  as long as a factor is found, N is not prime, otherwise it's prime

QED
```

## other prime algos? or make this more efficient?

**Sieve of Aristotles** is the next contendor, but suffers space efficiency. Requires memorisation of previous primes found, but helps exclude brute forcing of non-prime integers.

why not use isPrime to help the above?
Let's make an improved isPrime...

## isPrime2

an improved version of isPrime using the original isPrime???

``` python
def isPrime(n):
  # same implementation as before
  return True

def isPrime2(n):
  for i in range(2, int(n ** 0.5)+1):
    if isPrime(i) and n % i == 0:
      return False
    else:
      pass
  return True
```

makes sense but it's probably more expensive because;

rather than performing N % 6 == value

instead it is testing 6 if 6 isPrime which in this instance is a quick False due to a factor of 2, but for larger non-primes it would get worse unless we record which integers are or aren't prime once tested .... which leads back to the whole Sieve of Aristotles thing and space complexity, but would be good if really testing bigger numbers and not for the 2nd run onwards.

## isPrimeMemo

same idea as isPrime2 but with memoisation.


def primes(nPrimes, lowerBound = 2):
  i = lowerBound
  primesYielded = 0
  while primesYielded < nPrimes:
    if not (i % 2 == 0 and i > 2):
      j = int(i ** 0.5)
      k = 2
      while k <= j:
        if i % k == 0:
          break
        k += 1
      else:
        yield i
        primesYielded += 1
    i += 1
    
def get_primes(until):
  sieve = [1] * until
  prime = 2

  primes = []

  while prime < until:
    if sieve[prime]:
      primes.append(prime)

      temp = prime + prime
      while temp < until:
        sieve[temp] = 0
        temp += prime

    prime += 1

  return primes

def longest_consecutive_prime_sum(until):
  primes = get_primes(until)

  primes_set = set(primes)
  primes_sum = [0]

  for i in range(0, len(primes)):
    primes_sum.append(primes_sum[i] + primes[i])


  total_primes = 0
  result = 0
  for i in range(0, len(primes_sum)):
    for j in range(i - (total_primes + 1), -1, -1):
      if primes_sum[i] - primes_sum[j] > until:
        break

      if primes_sum[i] - primes_sum[j] in primes_set:
        total_primes = i - j
        result = primes_sum[i] - primes_sum[j]

  return result

print (longest_consecutive_prime_sum(1000000))

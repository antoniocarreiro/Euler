import eulerlib

def sumPrimes():
	total = sum(eulerlib.primes(1999999))
	return str(total)

print(sumPrimes())
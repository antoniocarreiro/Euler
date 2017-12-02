import gmpy2

def num_divisors(n):
	end = gmpy2.isqrt(n)
	result = sum(2
		for i in range(1, end + 1)
		if n % i == 0)
	if end**2 == n:
		result -= 1
	return result

def sumUntilN(n):
    return sum(range(n + 1))

divisors = 0
n = 1
while True:
    divisors = num_divisors(sumUntilN(n))
    if(divisors > 500):
        print(sumUntilN(n))
        break
    else:
        n = n+1

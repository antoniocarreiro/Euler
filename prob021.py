from functools import reduce

def d(n):
	return sum(sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))[:-1])

print(sum(x for x in range(1, 10000) if d(x) > 0 and x != d(x) and x == d(d(x))))
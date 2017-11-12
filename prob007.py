def is_prime(a):
    return all(a % i for i in range(2, a))
    
def nth_prime(n):
    num = 1
    current = 2

    while num < n:
        current += 1
        if is_prime(current):
            num += 1
    return current
   
print(nth_prime(10001))

def sum_quare_powers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i**2
    return sum
   
def square_powers_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    pow = sum**2
    return pow

print(square_powers_sum(100) - sum_quare_powers(100))

def self_powers_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += pow(i, i)
        
    return sum
    
print(self_powers_sum(1000) % pow(10,10))

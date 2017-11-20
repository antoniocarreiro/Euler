abc_sum = 1000
for _ in range(1, abc_sum):
    for i in range(_+1, abc_sum - _):
        j = abc_sum - _ - i
        if(_**2 + i**2 == j**2):
            print(_*i*j)

def collatz(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count


index = 0;
size = 0;
for i in range(1000000):
    c = collatz(i)
    if c > size:
        size = c
        index = i

print ("size %d at index %d" , size, index)
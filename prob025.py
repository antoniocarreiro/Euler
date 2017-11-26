def fibonacci(digits):
    prev = 1
    cur = 0
    i = 0
    while(len(str(cur)) < 1000):
        prev, cur = cur, prev + cur
        i += 1

    return i

print(fibonacci(1000))
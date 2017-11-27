def fac(n):
    if 1 == n: return 1
    return n * fac(n-1)

def perm(s, n):
    if len(s) == 1:
        return str(s[0])

    p = fac(len(s)-1)

    for i in range(len(s)):
        if p*(i+1) > n:
            return str(s[i]) + perm(s[:i] + s[i+1:], n - i*p)

print(perm(range(10), 999999))
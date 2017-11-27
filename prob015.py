f = lambda n: reduce(lambda x,y:x*y, range(1,n+1), 1)
n, m = 20, 20

print "Routes through a", n, "x", m, "grid", f(n+m) // f(n) // f(m)
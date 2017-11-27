score = lambda word: sum(ord(c)-64 for c in word)
names = sorted(open('names.txt').read().rstrip().replace('"', '').split(','))

s = sum(ln*score(name) for ln, name in enumerate(names, 1))
print(s)
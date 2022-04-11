s = set()
s.add(1)
s.add(2)
print(s)
s.clear()
s = {1, 2, 3}
sc = s
s.add(4)
print(s.difference(sc))
s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
print(s2)
s.dicard(12)
print(s)
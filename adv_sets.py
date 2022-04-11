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
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}
print(s1.isdisjoint(s3))
print(s1.issubset(s2))
print(s2.issuperset(s1))

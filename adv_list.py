l = [1, 2, 3]
l.append(4)
l.count(1)
x = [1, 2, 3]
x.extend([4, 5])
print(x)
print(l.index(2))
l.insert(2, 'inserted')
print(l)
ele = l.pop()
print(l)
l.remove('inserted')
print(l)
l = [1, 2, 3, 4, 3]
l.remove(3)
print(l)
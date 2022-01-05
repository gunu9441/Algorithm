a = 3
b = 3
print(id(a), id(b))

c = [1, 1]
d = [[1, 2, 3], [4, 5, 6]]

# print(d[*c])


name = 'Michael'
first, *middle, last = name

print(name)
print(first)
print(middle)
print(last)

*names, = 'Michael', 'Jons', 'Cons'
print(names)

names = [1, 2, 3, 4]
du_names = names
names[1] = 100
print(du_names)
print(names)

du2_names = names.copy()
names[2] = 1000
print(du2_names)
print(names)

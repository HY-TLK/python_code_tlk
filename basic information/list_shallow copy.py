# shallow copy
x = [1,2,3]
y = x.copy()
print(y)
x[1] = 100
print(x)
print(y)
print()

a = [1,2,3,4]
b = a[:]
print(b)
a[1] = 1234
print(a)
print(b)
print()

# limitations of Shallow Copy
c = [[1,2,3],[4,5,6],[7,8,9]]
d = c.copy()
print(d)
c[1][1] = "n"
print(c)
print(d) # the content in d changes as c changes
print()



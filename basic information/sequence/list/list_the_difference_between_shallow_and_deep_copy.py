#shallow copy
x = [1,2,3,4,5]
y = x.copy()
print(y)
x[1] = 100
print(x)
print(y)
print()

# limitations of shallow copy
a = [[1,2,3],[4,5,6],[7,8,9]]
b = a.copy()
print(b)
a[1][1] = 1000
print(a)
print(b)
print()

#deep copy
import copy
c = [[1,2,3],[4,5,6],[7,8,9]]
d = copy.deepcopy(c)
c[1][1] = 9999
print(c)
print(d)

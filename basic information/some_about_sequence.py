# id
# for list , it won't change its unicode even if the content changes
a = [1, 2, 3]
print("the unicode of list_a is",id(a))
a *= 2
print("the unicode of liat_a after doubled is ",id(a))
# for tuple , it will change its unicode if the content changes
b = (1, 2, 3)
print("the unicode of tuple_b is",id(b))
b *= 2
print("the unicode of tuple_b after doubled is",id(b))
print()

# in , not in
c = "harry" in "harry yang"
print("determine whether 'harry' is in 'harry yang': ",c)
print()

# is , is not
d = [1, 2, 3]
e = [1, 2, 3]
print("determine whether list_d is list_e: ",d is c)

f = (1, 2, 3)
g = (1, 2, 3)
print("determine whether tuple_f is tuple_g: ",f is g)
print()

# del
x = [1, 2, 3, 4, 5, 6]
del x[1:4]
print(x)

y = [1, 2, 3, 4, 5, 6]
y[1:4] = []
print(y)

z = [1, 2, 3, 4, 5, 6]
del z[::2]
print(z)

h = [1, 2, 3, 4, 5, 6]
del h[:]
print(h)
print()

# list
print(list("harry"),type(list("harry")))
print(list((1,2,3)),type(list((1,2,3))))

# tuple
print(tuple("harry"),type(tuple("harry")))
print(tuple([1,2,3]),type(tuple([1,2,3])))

# str
print(str([1,2,3]),type(str([1,2,3])))
print(str((1,2,3)),type(str((1,2,3))))
print()

# max & min
i = [1,1,2,3,5]
print(max(i))
print(min(i))
print(max(1,1,2,3,5))
# for strings , max & min will return The letter with the largest encoding value
# When the letters are the same, the encoding value of the uppercase letter is smaller than that of the lowercase letter.
j = "HARRYharry"
print(max(j))
print(min(j))
# If it is an empty sequence, using max or min will display the contents of default
k = ""
print(min(k,default="nothing in there"))

# len & sum
l = [1,0,0,8,6]
print(len(l))
print(sum(l))

m = "Harry Yang"
print(len(m))

n = [2,3,3,3,3]
print(sum(n,start = 100))
print()

# sorted , (always return a list)
o = [4,5,2,4,4,6,7,1]
print("sort from smallest to largest: ",sorted(o))
print("reverse the sorted list: ",sorted(o, reverse = True))
print()
s = ["harry","banana","apple","bird"]
print(sorted(s))
# Sort by length
print("sort the list by length: ",sorted(s, key = len))
print()
# Sort alphabetically
print("sort alphabetically",sorted("harry"))
# Sort the tuple
print("a list will be returned even if a tuple is sorted: ",sorted((1,0,0,8,6)))
print()

# the difference between sort and sorted
p = [1,2,3,0,6,5,4]
print("original list: ",p)
print("sorted: ", sorted(p))
print("the original list doesn't change: ",p)
print()
q = [1,2,3,0,6,5,4]
print("original list: ",q)
q.sort()
print("the original list changes: ",q)
print()

# reversed
t = [1,2,5,8,0]
print("Returns a reverse iterator",reversed(t)) # Returns a reverse iterator
print("change the iterator into a list: ",list(reversed(t)))
print("change the iterator into a tuple: ",tuple(reversed(t)))
print()
print(list(reversed(range(1,5))))
print()
print(reversed("Harry")) # Returns a reverse iterator
print(list(reversed("Harry")))
print()

# all & any
# all -- whether all elements have a value of true
# any -- whether any element has a value of true
u1 = [1,1,0]
u2 = [1,1,9]
print(all(u1))
print(all(u2))
print(any(u1))
print(any(u2))
print()

# enumerate
seasons = ["Spring","Summer","Fall","Winter"]
print(list(enumerate(seasons,10)))
print()

# zip
v1 = ["a","b","c","d"]
v2 = ["e","f","g","h"]
v = list(zip(v1,v2))
print(v)
# If the lengths are different, the shortest one shall prevail.
v3 = [1,2,3]
v = list(zip(v1,v2,v3))
print(v)
# If you want the longest one(s) to appear completely
# you need to use the zip_longest function of the itertools module.
import itertools
v = list(itertools.zip_longest(v1,v2,v3))
print(v)
print()

# map
w = list(map(ord, "Harry"))
print(w)
w = list(map(pow,[2,3,4],[3,4,5]))
print(w)
w = list(map(max,[1,7,2],[3,4,5]))
print(w)
print()

# filter
x = list(filter(str.islower,"FishC"))
print(x)
print()

# Iterable objects can be reused, but iterators are disposable
y = map(str.upper,"FishC")
for each in y:
    print(each)
print(list(y))
print()

# iter
# change Iterable objects into iterators
z1 = [1,2,3]
z2 = iter(z1)
print(type(z1))
print(type(z2))
print()

# next
# Extract the elements from the iterator one by one
print(next(z2))
print(next(z2))
print(next(z2))
#After all are extracted, an exception will occur
print(next(z2))

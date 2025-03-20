#tuple
#Tuples are immutable (cannot be changed once created)
rhyme = (1,2,3,'hello')

#slice
print(rhyme[::-1 ])

#Finding Elements
print(rhyme.count(1))
print(rhyme.index(1))

#Splicing
s = (11,22,33,'world')
print(s+rhyme)
#repeating
print(s*2)

#nested tuple
w = rhyme,s
print(w)

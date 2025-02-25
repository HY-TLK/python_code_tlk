#double every single number in the list with a loop
a = [1,2,3,4,5]
for i in range (len(a)):
    a[i] = a[i]*2
print(a)


#double every single number in the list with a list comprehension expression
b = [4,5,6,7,8]
b = [i*2 for i in  b]
print(b)


#get the element on the diagonal of the group
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
dia1 = [matrix[i][i] for i in range (3)]
print(dia1)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
dia = [matrix[i][2-i] for i in range (3)]
print(dia)


#list comprehension expression and if statement
even_number = [i for i in range(10) if i%2 == 0]
print(even_number)

odd_number = [i+1 for i in range(10) if i%2 == 0]
print(odd_number)


#filter words that start with specific letter from the string list
words = ['Harry','Horray','Hello','George']
Hwords = [i for i in words if i[0] == 'H']
print(Hwords)


#
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flatten = [col for row in matrix for col in row]
print(flatten)

flatten = []
for row in matrix:
    for col in row:
        flatten.append(col)
print(flatten)


#
h = [x+y for x in "HA" for y in 'ha']
print(h)

h = []
for x in 'HA':
    for y in 'ha':
        h.append(x+y)
print(h)


#
t = [(m,n) for m in range (5) if m % 2 == 0
           for n in range (5) if n % 3 == 0]
print(t)

#1.Generate a list containing the squares of 1 to 10.
list1 = [x**2 for x in range (1,11)]
print('question1: ',list1)


#2.Generate a list of all even numbers from 1 to 20.
list2 = [x for x in range (1,21) if x % 2 == 0]
print('question2: ',list2)


#3.Convert each character in a string to uppercase and create a list.
word3 = 'harryyang'
word3n = word3.upper()
list3 = [each for each in word3n]
print('question3: ',list3)


#4.Flatten a two-dimensional list into a one-dimensional list.
matrix4 = [[1,2,3],[4,5],[6,7,8,9]]
list4 = [n for m in matrix4 for n in m]
print('question4: ',list4)


#5.Filter out all numbers greater than 10 from a list and create a new list.
samplelist5 = [5, 12, 8, 15, 3, 20]
list5 = [x for x in samplelist5 if x > 10]
print('question5: ',list5)


#6.Extract strings whose length is greater than 3 from a list of strings.
samplelist6 = ['apple','banana','dog','cat']
list6 = [each for each in samplelist6 if len(each) > 3]
print('question6: ',list6)


#7.Generate a list of the squares from 1 to 10, keeping only the even numbers.
list7 = [x**2 for x in range (1,11) if x % 2 == 0]
print('question7: ',list7)


#8.Separate the positive and negative numbers in a list into two lists.
samplelist8 = [1,-2,3,-4,5,-6]
list8_1 = [x for x in samplelist8 if x > 0]
list8_2 = [y for y in samplelist8 if y < 0]
print('question8:  positive number: ',list8_1,'\n\t\t   ','negative number: ',list8_2)


#9.Square all elements of a nested list and create a new nested list.
samplelist9 = [[1,2],[3,4],[5,6]]
list9 = [[x**2 for x in y]for y in samplelist9]
print('question9: ',list9)


#10.Extract all vowels (a, e, i, o, u) from a string and make a list.
word10 = 'hello world'
vowels = ['a','e','i','o','u']
list10 = [x for x in word10 if x in vowels]
print('question10:',list10)


#11.Generate a list of all numbers from 1 to 100 that are divisible by 3 or 5.
list11 = [x for x in range (1,21) if x % 3 == 0 or  x % 5 == 0]
print('question11:',list11)


#12.Separate strings and numbers from a list into two lists
samplelist12 = ['a',1,'b',2,'c',3]
list12_num = [x for x in samplelist12 if type(x) == int]
list12_str = [y for y in samplelist12 if type(y) == str]
print('question12:',list12_num,'\n\t\t   ',list12_str)


#13.Reverse all the strings in a list of strings and create a new list.
samplelist13 = ['hello','world','python']
list13 = [x[::-1] for x in samplelist13]
print('question13:',list13)
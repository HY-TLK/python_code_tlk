#split
a = "harry yang"
print(a.split())

#partition,rpartition
b = "Harry Yang loves Python"
print(b.partition(" "))

c = "Harry Yang loves Python"
print(c.rpartition(" "))

#join
d = ".".join(["hello","world","python"])
print(d)

#formatting strings
e = 3.1415926
print("%f"%(e))
print("%.2f"%(e))

print("{1},{0},{0}".format("hello","world"))

print("{:.7}".format("Harry Yang"))
print("{:.2f}".format(1.11111))
print("{:.2g}".format(1.11111))

print("{:b}".format(45))
print("{:o}".format(45))
print("{:x}".format(45))
# "#" represents for prefix
print("{:#b}".format(45))

print("{:e}".format(45))
print("{:f}".format(45))
print("{:.2f}".format(45))
print("{:%}".format(45))

#f-string
name = "harry"
age = "16"
print(f"my name is {name}, I am {age} years old")

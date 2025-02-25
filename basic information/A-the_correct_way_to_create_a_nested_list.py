B = [[0]*3]*3
print(B)
print(B[0] is B[1])
B[1][1] = 1
print(B)

print()

A = []
for _ in range(3):
    A.append([0]*3)
print(A)
print(A[0] is A[1])
A[1][1] = 1
print(A)

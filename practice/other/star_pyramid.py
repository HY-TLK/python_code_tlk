number_input = int(input('please enter an integer:'))
n = 1
m = number_input
while n <= number_input:
    print(' '*(m),'*'*(2*n-1),end='\n')
    m -= 1
    n += 1

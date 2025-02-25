number_input = input('please enter a number: ')
num = int(number_input)

if num < 2:
    print("it's not a prime number")  # 处理小于 2 的情况
else:
    i = 2
    while i * i <= num:  # 只需检查到 sqrt(num)
        if num % i == 0:
            print("it's not a prime number")
            break
        i += 1
    else:
        print("it's a prime number")  # 只有当 while 没有被 break 时，才会执行

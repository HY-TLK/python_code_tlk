numbers_input = input('please enter five integers:')
numbers_list = [int(num)for num in numbers_input.split()]
average = sum(numbers_list)/5
print(average)
print(numbers_list)
i = 0
while i < len(numbers_list):
    if numbers_list[i] < average:
        numbers_list.remove(numbers_list[i])
    else:
        i += 1
print(numbers_list)
    

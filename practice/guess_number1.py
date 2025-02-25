import random
y=random.randint(0,100)
attempt=0
while True:
    x = int(input('please enter a number randomly from 0 to 100:'))
    attempt += 1
    if x == y:
        print(f'Congratulations!You get the correct number after {attempt} tries')
        break
    elif x > y:
        print('try smaller number')
    else :
        print('try bigger number')
import random
y = random.randint(0,100)
attempt = 0
while True:
    guess = input ('please select a number randomly from 0 to 100:')
    guess_number = int(guess)
    attempt += 1
    if guess_number == y:
        print('success')
        print(f'{attempt} tries!')
        break
    elif guess_number < y:
        print('try bigger number')
    else:
        guess_number > y
        print('try smaller number')
        
    

import random

def test_random():
    random_number = random.randint(1, 10)
    number=int(input('enter number'))
    if number == random_number:
        print('correct')
    elif number > random_number:
        print('too much')
    elif number < random_number:
        print('too low')

    print(random_number)
    
test_random()
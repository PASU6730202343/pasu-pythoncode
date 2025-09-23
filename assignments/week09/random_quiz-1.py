"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
def test_random():
    random_number = random.randint(1, 20)
    for i in range(1,7):

        number=int(input(f'Attempt {i}/6 Enter number'))
        
        if number == random_number:
            print('correct')
            break
        elif number > random_number:
            print('too much')
        else:
            print('too low')
        
test_random()


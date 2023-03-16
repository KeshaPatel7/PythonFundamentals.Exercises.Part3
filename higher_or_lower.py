from random import randrange


def generate_a_number():
    return randrange(10)

def ask_to_enter_any_number():
    guess = input('enter a number')
    return int(guess)

def result(random_number , users_guess):
    if users_guess == random_number:
        print("You guessed it right.")
    elif users_guess > random_number:
        print("Too high.")
    else:
        print("Too low.")

random_number = generate_a_number()
users_guess = ask_to_enter_any_number()
result(random_number, users_guess)
print("The random number is :" + str(random_number))
print("The number you guessed:" + str(users_guess))






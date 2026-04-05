from typing import Final
import random


LOWER_LIMIT: Final[int] = 0
UPPER_LIMIT: Final[int] = 100
count = 0
random_number: int = random.randint(LOWER_LIMIT, UPPER_LIMIT)


def bot_message(msg: str) -> None:
    print(f'Bot: {msg}')



bot_message('Welcome to GuessThatNumber™!')
bot_message(f'Guess a number between {LOWER_LIMIT} & {UPPER_LIMIT}.')


while True:
    
    try:
        user_guess: int = int(input('You: '))
    except ValueError as e:
        bot_message(f'{e}, please only use numbers.')
        continue

    count += 1

    
    if user_guess > random_number:
        bot_message('The number is lower.')
    elif user_guess < random_number:
        bot_message('The number is higher.')
    else:
        bot_message('You guessed correctly! You win!')
        bot_message(f'It took you {count} tries.')
        break


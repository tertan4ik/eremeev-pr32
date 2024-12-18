import random

def guess_number_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Привет! Я загадал число от 1 до 100. Попробуй угадать его!")

    while True:
        try:
            user_guess = int(input("Введите ваше предположение: "))
            attempts += 1  
            if user_guess < secret_number:
                print("Загаданное число больше. Попробуйте ещё раз.")
            elif user_guess > secret_number:
                print("Загаданное число меньше. Попробуйте ещё раз.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
                break 
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    guess_number_game()

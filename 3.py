import random

def get_card_value(card):
    if card == "шестёрка":
        return 6
    elif card == "семёрка":
        return 7
    elif card == "восьмёрка":
        return 8
    elif card == "девятка":
        return 9
    elif card == "десятка":
        return 10
    elif card == "валет":
        return 2
    elif card == "дама":
        return 3
    elif card == "король":
        return 4
    elif card == "туз":
        return 11
    return 0

def main():

    deck = [
        "шестёрка", "семёрка", "восьмёрка", "девятка", "десятка", "валет", 
        "дама", "король", "туз"
    ] * 4 
    random.shuffle(deck)

    score = 0

    print(deck)

    print("Добро пожаловать в игру в Очко!")

    while True:
   

        if score >= 21:
            break
               
        user_input = input(f"Ваши очки: {score}. Хотите взять карту? (y/n): ").lower()

        if user_input == "n":
            print(f"Вы завершили игру с {score} очками. До свидания!")
            break
        elif user_input == "y":
    
            card = deck.pop()

            card_value = get_card_value(card)

            score += card_value
            print(f"Вы взяли карту: {card}. Она дает {card_value} очков.")
            if score == 21:
                print(f"Поздравляем! Вы выиграли с {score} очками!")
                break

            elif score > 21:
                print(f"Увы, вы проиграли с {score} очками. До свидания!")
                break

        else:
            print("Пожалуйста, ответьте 'y' или 'n'.")
            continue

if __name__ == "__main__":
    main()

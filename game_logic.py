import random
from decouple import config

def calculate_result(bet, entered_slot, winning_slot):
    if entered_slot == winning_slot:
        return bet * 2
    else:
        return -bet

def check_balance(balance):
    if balance > 0:
        return "WIN!"
    elif balance < 0:
        return "lose:("
    else:
        return "tie"

def main():
    my_money = int(config("MY_MONEY"))

    while True:
        print(f'Ваш текущий баланс: {my_money}')
        bet = int(input('Введите ставку: '))
        entered_slot = int(input('Введите слот (от 1 до 30): '))
        winning_slot = random.randint(1, 30)

        result = calculate_result(bet, entered_slot, winning_slot)
        my_money += result

        print(f'Выигрышний слот: {winning_slot}')
        print(f'Ваш результат: {"Выиграли" if result > 0 else "Проиграли"}')
        print(f'Ваш баланс: {my_money}')

        play_again = input("Хотите сыграть снова? (да/нет): ")
        if play_again.lower() != "да":
            break

    game_outcome = check_balance(my_money)
    print(f'Итог игры: {game_outcome}')

if __name__ == "__main__":
    main()
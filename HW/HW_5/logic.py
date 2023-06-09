
# Логика выигрыша или проигрыша в отдельном файле Правила игры такие :
# Есть массив из чисел от 1 до 30, каждый раз вы делаете ставку на определенную слоту из чисел и ставите деньги
# Рандомно выбирается выигрышная слота, если вы выигрываете, вам причисляется удвоенная сумма, той которую вы поставили, если вы загадали не выигрышную слоту - теряете поставленную сумму
# В начале игры у вас также есть деньги например 1000$, но в конце мы понимаем вы в выигрыше или в проигрыше значение переменной начального капитала должно считываться со скритой переменной под названием MY_MONEY из файла .env
# После каждой ставки вам задается вопрос хотите ли вы сыграть еще, если да - то делаете ставку, если нет - то подводится итог игры


import random
import player
MY_MONEY = player.config('MY_MONEY',cast=int)
SLOTS = list(range(1, 37))

def play_game(bet):
    winning_slot = random.choice(SLOTS)
    if winning_slot == bet:
        return bet * 2
    else:
        return -bet

while MY_MONEY > 0:
    print("Ваш Баланс: $", MY_MONEY)
    bet = int(input("На какой слот вы хотите поставить? (Введите число от 1 до 36): "))
    if bet < 1 or bet > 36:
        print("НЕПРАВИЛЬНОЕ ЧИСЛО Введите число от 1 до 36.")
        continue

    result = play_game(bet)
    MY_MONEY += result

    if result > 0:
        print("Поздравляем, вы выиграли! Ваш выигрыш составил $", result)
    else:
        print("К сожалению, вы проиграли. Ваша потеря составила $", -result)

    play_again = input("Хотите ли вы продолжить играть? (y/n): ")
    if play_again.lower() == "n":
        break

if MY_MONEY > 100:
    print("Поздравляем, вы выиграли игру! Ваш капитал составляет $", MY_MONEY)
else:
    print("К сожалению, вы проиграли игру. Ваш капитал составляет $", MY_MONEY)

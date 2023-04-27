
from decouple import config
MY_MONEY = config("MY_MONEY",cast=int)

def update_money(balance ,amount):
    return balance + amount

def check_balance(balance, amount):
    if balance < amount:
        return False
    else:
        return True

import random

#generate random account number for individuals

def generate_account_number():
    """Intialize str with '20' to store account number"""
    account_number = '20'
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    for num in range(8): # 8 numbers to be selected at random
        rand_number = random.choice(numbers)
        account_number += rand_number
    return account_number

account_number = generate_account_number()
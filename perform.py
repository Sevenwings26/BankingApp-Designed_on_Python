
import sys

from app_database import *

balance = 0

def validation():
    account_number = (input('Enter your account number: '))
    validate_acct = (input("Supply Secret pin:"))
    for customer in customers:
        if customer['account_number'] == account_number and customer['pin'] == validate_acct:
            print("Validation Successful, proceed! ")
            return
    else:
        print("""Incorrect Pin... 
                # Do you have an account with us? 
                To open an account, Press 1
                To quit, press 0""")
        user_choice = input('>>>> ')
        if user_choice == "1":
            create_account()            
        else:
            sys.exit


def operation():
    validation()
    print(""" 
            1. Deposit 
            2. Inquiry
            3. Withdraw
            4. Exit
            Enter 1/2/3/4
        """)
    
    choice = input(".... ")
    if choice == "1":
        global balance
        amt = float(input("How much are you depositing: "))
        balance = balance + amt
        print(f"Your balance is N{balance}")
    elif choice == "2":
        for customer in customers:
            print(f"{customer['first_name']}, your account balance is {balance}")
    elif choice == "3":
        
        withdraw = float(input("Enter ammount to withdraw: N"))
        if withdraw < balance:
            new_balance = balance - withdraw
            for customer in customers:
                print(f"{customer['first_name']}, {withdraw} has been deducted from your account. \n")
                print(f" Your New balance is N{new_balance}. \n")
        else:
            print("You are low on credit. ")
    else:
        sys.exit 
    
    
# global deduction
        # print("""a. 2,000        b. 5,000
        #          c. 10,000       d. 15,000 
        #          e. Enter amount. """)
        # # withdraw = 
        # a = 2000
        # b = 5000
        # c = 10000
        # d = 15000
        
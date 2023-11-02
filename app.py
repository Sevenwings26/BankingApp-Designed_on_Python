#INTRO 
"""Banking Application Software"""
"""Functions -
------- open account 
        display account info.
        deposit 
        withdraw
        check balance
        reach customer care for complaints """

#  START here
#import app modules 
from app_database import *
import display as d
from perform import *
from app_database import *


# Program starts running 

bank_name = "evergreen"
print(f"\t Welcome to {bank_name.upper()} bank. \n\t Experince the Extraordinary!!!")
print("------------------------------------------------------------------------------------------------- ")

while True:
    """Guide """
    print("""        
            To OPEN an acoount, press 1
            To DISPLAY account, press 2
            To PERFORM TRANSACTIONS, press 3
            To QUIT, press q\n""")
    
    choice = input('>>>> ').lower().strip()
    if choice == '1':
        """Create account details and also generate account number """
        create_account()
    elif choice == '2':
        d.display()
    elif choice == '3':
            operation()
    elif choice == "q":
        break



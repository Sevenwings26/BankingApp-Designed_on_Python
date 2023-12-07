
from app_database import *

# customers = []
def display():
    if customers:
        for i, customer in enumerate(customers, start=1):
            print(f"Customer: {i}")
            print('First name:', customer['first_name'])
            print('Second name:', customer['second_name'])
            print('last name:', customer['last_name'])
            print('Phone number:', customer['phone_number'])
            # print(f"Age- {customer['age']}")
            print(f"Date of birth: {customer['birth_day']} - {customer['birth_month']} - {customer['birth_year']}")
            print('E-mail: ', customer['email'])
            print('account_number',customer['account_number'])
            
    else:
        print("No account added")
   
print(display())

         
            
             
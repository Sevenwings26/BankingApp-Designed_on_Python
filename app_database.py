"""
        MODULE contains:
                database connections
                create_account() function for registration
                other functions working registration
""" 


import mysql.connector

# Import account number module to generate unique account number
from acct_number import account_number

# Initialize an empty list to store customer data
customers = []

# Database connection setup
# users_info = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="arowosola1449",  # Replace with your MySQL password
#     database="green_bank",
#     auth_plugin='mysql_native_password'
# )

# users_cursor = users_info.cursor()

# # Create the "customer" table if it doesn't exist
# users_cursor.execute("CREATE TABLE IF NOT EXISTS customer (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(30), second_name VARCHAR(30), last_name VARCHAR(30), birth_day VARCHAR(2), birth_month VARCHAR(2), birth_year INT, age INT, phone_number BIGINT, email VARCHAR(45), pin VARCHAR(4), account_number VARCHAR(11))")

# Function to fetch 11-digit phone number
def get_phone_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and len(user_input) == 11:
            return int(user_input)
        else:
            print('Invalid phone number. Enter your 11-digit phone number.')

# Function to fetch a 4-digit secret PIN
def secret_pin(pin):
    while True:
        user_pin = input(pin)
        if user_pin.isdigit() and len(user_pin) == 4:
            return user_pin
        else:
            print("Pin must be 4 digits!")

# Collect customer information
def create_account():
    print("Open an account\n")
    first_name = input('Input your first name: ').title().strip()
    second_name = input('Input your second name: ').title().strip()
    last_name = input('Input your last name: ').title().strip()
    
    phone_number = get_phone_number('Enter your 11-digit phone number: ')
    
    birth_day = input('Input Day of birth: ')
    birth_month = input('Input Month of birth: ')
    birth_year = int(input('Input year of birth: '))
    
    age = 2023 - birth_year
    
    email = input('Email: ')
    
    pin = secret_pin('Enter your 4-digit PIN: ')
    
    print(f"{first_name}, thank you for opening an account with us!\n")
    print(f"Customer {first_name}, your account number is: {account_number}.\n")

    # Save customer data into a dictionary
    customers_info = {
        'first_name': first_name,
        'second_name': second_name,
        'last_name': last_name,
        'birth_day': birth_day,
        'birth_month': birth_month,
        'birth_year': birth_year,
        'age': age,
        'phone_number': phone_number,
        'email': email,
        'pin': pin,
        'account_number': account_number
    }
    
    # Append the dictionary to the list
    customers.append(customers_info)
    
    # # Insert customer data into the database
    # users_input = ("INSERT INTO customer (first_name, second_name, last_name, birth_day, birth_month, birth_year, age, phone_number, email, pin, account_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    # inputs = (first_name, second_name, last_name, birth_day, birth_month, birth_year, age, phone_number, email, pin, account_number)
    
    # users_cursor.execute(users_input, inputs)
    # users_info.commit()



# BankApp - Python Banking Application
## Bank name - GREEN BANK

Welcome to the BankApp, a Python-based banking application designed to help you manage your accounts, perform transactions, and keep track of your finances. This application offers the following functionalities:

1. [Create Account](#create-account)
2. [Display Account Information](#display-account-information)
3. [Perform Transactions](#perform-transactions)

## Table of Contents
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Before using BankApp, you need to set up the required environment and dependencies.

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/bankapp.git
   ```

2. **Install Dependencies:**

   Navigate to the project directory and install the necessary Python dependencies.

   ```bash
   cd bankapp
   pip install -r requirements.txt
   ```

3. **Configure MySQL:**

   BankApp uses a MySQL database to store customer information. Make sure you have MySQL installed and create a database named `green_bank`. You can do this manually or by running the provided SQL script in `app_database.py`.

## Getting Started

1. **Generate Account Number:**

   The `acct_number.py` module contains a function that generates unique account numbers for customers, starting with "20" to indicate the bank's prefix.

2. **Create Account:**

   The `app.py` module is the main application starter. Run it to create a new bank account. During account creation, you will be prompted to provide various details such as your name, date of birth, phone number, email, and a 4-digit PIN. Your account number will be generated, and your information will be stored in the MySQL database.

3. **Display Account Information:**

   Use the `display.py` module to display customer details by providing your account number. This can help you verify your account information.

4. **Perform Transactions:**

   The `perform.py` module contains functions for performing basic banking operations such as deposit, withdrawal, and balance inquiry. Use this module to manage your funds.

## Usage

1. **Create an Account:**

   Run the `app.py` module to create a new account and follow the on-screen instructions. After successfully creating an account, you will receive an account number.

   ```bash
   python app.py
   ```

2. **Display Account Information:**

   To display your account details, run the `display.py` module and provide your account number.

   ```bash
   python display.py
   ```

3. **Perform Transactions:**

   Use the `perform.py` module to perform banking operations. You can deposit, withdraw, or check your account balance.

   ```bash
   python perform.py
   ```

## Contributing

We welcome contributions to BankApp! If you have any ideas, improvements, or bug fixes, please create a pull request or open an issue on the [GitHub repository](https://github.com/yourusername/bankapp).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

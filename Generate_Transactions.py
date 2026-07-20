import pandas as pd
import random
from faker import Faker
from pathlib import Path


fake = Faker()

# Find project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folder
DATA_DIR = BASE_DIR / "Data"


# Load accounts
accounts_df = pd.read_csv(
    DATA_DIR / "Accounts.csv"
)


transactions = []


transaction_types = [
    "Deposit",
    "Withdrawal",
    "Payment"
]


categories = [
    "Salary",
    "Groceries",
    "Rent/Mortgage",
    "Utilities",
    "Shopping",
    "Dining",
    "Entertainment",
    "Transfer",
    "Interest"
]


transaction_id = 900000


# Generate transactions
for _, account in accounts_df.iterrows():

    # Determine transaction frequency
    if account["Account_Type"] == "Checking":
        num_transactions = random.randint(10, 40)

    elif account["Account_Type"] == "Savings":
        num_transactions = random.randint(2, 10)

    else:
        # CD accounts have fewer transactions
        num_transactions = random.randint(1, 3)


    for _ in range(num_transactions):

        account_type = account["Account_Type"]


        # Make transaction behavior realistic
        if account_type == "Certificate of Deposit":

            transaction_type = "Deposit"
            category = "Interest"

            amount = round(
                random.uniform(20, 500),
                2
            )


        elif account_type == "Savings":

            transaction_type = random.choice(
                ["Deposit", "Withdrawal"]
            )

            category = random.choice(
                ["Transfer", "Interest", "Savings"]
            )

            amount = round(
                random.uniform(50, 5000),
                2
            )


        else:

            transaction_type = random.choice(
                transaction_types
            )

            category = random.choice(
                categories
            )

            amount = round(
                random.uniform(10, 5000),
                2
            )


        transaction = {

            "Transaction_ID": transaction_id,

            "Account_ID": account["Account_ID"],

            "Transaction_Date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ),

            "Transaction_Type": transaction_type,

            "Category": category,

            "Amount": amount

        }


        transactions.append(transaction)

        transaction_id += 1



transactions_df = pd.DataFrame(transactions)


# Save dataset
transactions_df.to_csv(
    DATA_DIR / "Transactions.csv",
    index=False
)


print("Transactions dataset created successfully!")
print(transactions_df.head())

print(
    f"\nTotal Transactions: {len(transactions_df):,}"
)
import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake = Faker()

# Find project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folder location
DATA_DIR = BASE_DIR / "Data"

# Load customers
customers_df = pd.read_csv(
    DATA_DIR / "Customers.csv",
    parse_dates=["Customer_Since"]
)

accounts = []

account_types = ["Checking", "Savings", "Certificate of Deposit"]

account_id = 500000

for _, customer in customers_df.iterrows():

    # Every customer gets one checking account
    checking_balance = random.randint(500, 15000)

    accounts.append({
        "Account_ID": account_id,
        "Customer_ID": customer["Customer_ID"],
        "Account_Type": "Checking",
        "Balance": checking_balance,
        "Open_Date": fake.date_between(
            start_date=customer["Customer_Since"],
            end_date="today"
        )
    })

    account_id += 1

    # 70% chance of a savings account
    if random.random() < 0.70:

        savings_balance = int(customer["Income"] * random.uniform(0.15, 1.50))

        accounts.append({
            "Account_ID": account_id,
            "Customer_ID": customer["Customer_ID"],
            "Account_Type": "Savings",
            "Balance": savings_balance,
            "Open_Date": fake.date_between(
                start_date=customer["Customer_Since"],
                end_date="today"
            )
        })

        account_id += 1

    # 20% chance of a CD account
    if random.random() < 0.20:

        cd_balance = int(customer["Income"] * random.uniform(0.50, 3.00))

        accounts.append({
            "Account_ID": account_id,
            "Customer_ID": customer["Customer_ID"],
            "Account_Type": "Certificate of Deposit",
            "Balance": cd_balance,
            "Open_Date": fake.date_between(
                start_date=customer["Customer_Since"],
                end_date="today"
            )
        })

        account_id += 1


accounts_df = pd.DataFrame(accounts)

accounts_df.to_csv(
    DATA_DIR / "Accounts.csv",
    index=False
)

print("Accounts dataset created successfully!")
print(accounts_df.head())
print(f"\nTotal Accounts: {len(accounts_df):,}")
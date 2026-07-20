import pandas as pd
import random
from faker import Faker
from pathlib import Path


fake = Faker()


# Find project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folder
DATA_DIR = BASE_DIR / "Data"


# Load customers
customers_df = pd.read_csv(
    DATA_DIR / "Customers.csv"
)


loans = []


loan_types = [
    "Mortgage",
    "Auto Loan",
    "Personal Loan",
    "Business Loan"
]


loan_statuses = [
    "Active",
    "Paid Off",
    "Defaulted"
]


loan_id = 700000


# Approximately 30% of customers have loans
customers_with_loans = customers_df.sample(
    frac=0.30,
    random_state=42
)


for _, customer in customers_with_loans.iterrows():

    loan_type = random.choice(loan_types)


    # Loan amounts based on loan type
    if loan_type == "Mortgage":

        loan_amount = random.randint(
            150000,
            600000
        )

        term = 30


    elif loan_type == "Auto Loan":

        loan_amount = random.randint(
            10000,
            60000
        )

        term = random.choice([3, 5, 6])


    elif loan_type == "Personal Loan":

        loan_amount = random.randint(
            1000,
            25000
        )

        term = random.choice([1, 3, 5])


    else:

        loan_amount = random.randint(
            25000,
            250000
        )

        term = random.choice([5, 10])


    # Higher income customers receive slightly better rates
    if customer["Income"] > 100000:
        interest_rate = round(
            random.uniform(3.5, 7.0),
            2
        )

    else:
        interest_rate = round(
            random.uniform(5.0, 12.0),
            2
        )


    # Default probability based on income
    if customer["Income"] < 50000:

        default_probability = 0.12

    else:

        default_probability = 0.04


    default_flag = (
        1 if random.random() < default_probability else 0
    )


    if default_flag == 1:
        status = "Defaulted"

    else:
        status = random.choice(
            ["Active", "Paid Off"]
        )


    loan = {

        "Loan_ID": loan_id,

        "Customer_ID": customer["Customer_ID"],

        "Loan_Type": loan_type,

        "Loan_Amount": loan_amount,

        "Interest_Rate": interest_rate,

        "Loan_Term_Years": term,

        "Loan_Status": status,

        "Default_Flag": default_flag,

        "Loan_Start_Date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )

    }


    loans.append(loan)

    loan_id += 1



loans_df = pd.DataFrame(loans)


# Save dataset
loans_df.to_csv(
    DATA_DIR / "Loans.csv",
    index=False
)


print("Loans dataset created successfully!")
print(loans_df.head())

print(
    f"\nTotal Loans: {len(loans_df):,}"
)
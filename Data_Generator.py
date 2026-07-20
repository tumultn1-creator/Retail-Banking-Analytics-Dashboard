import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

num_customers = 50000

customers = []

states = [
    "New Jersey",
    "New York",
    "Pennsylvania",
    "California",
    "Texas",
    "Florida",
    "Illinois",
    "Virginia",
    "North Carolina",
    "Georgia"
]

employment_status = [
    "Full-Time",
    "Part-Time",
    "Self-Employed",
    "Retired",
    "Unemployed"
]

for i in range(num_customers):

    customer = {
        "Customer_ID": 100000 + i,
        "First_Name": fake.first_name(),
        "Last_Name": fake.last_name(),
        "Age": random.randint(18, 75),
        "Gender": random.choice(["Male", "Female"]),
        "State": random.choice(states),
        "Income": random.randint(30000, 200000),
        "Employment_Status": random.choice(employment_status),
        "Customer_Since": fake.date_between(
            start_date="-10y",
            end_date="today"
        )
    }

    customers.append(customer)


customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "Data/Customers.csv",
    index=False
)

print("Customers dataset created successfully!")
print(customers_df.head())

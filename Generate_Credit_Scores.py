import pandas as pd
import random
from pathlib import Path


# Find project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folder
DATA_DIR = BASE_DIR / "Data"


# Load customers
customers_df = pd.read_csv(
    DATA_DIR / "Customers.csv"
)


credit_scores = []


credit_id = 800000


for _, customer in customers_df.iterrows():

    income = customer["Income"]
    age = customer["Age"]


    # Higher income generally improves credit score
    base_score = random.randint(550, 750)


    if income > 100000:
        base_score += random.randint(20, 60)

    elif income < 50000:
        base_score -= random.randint(10, 40)


    # Older customers tend to have longer credit history
    if age > 45:
        base_score += random.randint(5, 25)


    # Keep scores realistic
    credit_score = max(
        300,
        min(base_score, 850)
    )


    # Credit rating category

    if credit_score >= 750:
        rating = "Excellent"

    elif credit_score >= 700:
        rating = "Good"

    elif credit_score >= 650:
        rating = "Fair"

    else:
        rating = "Poor"



    # Risk category

    if credit_score >= 700:
        risk = "Low"

    elif credit_score >= 600:
        risk = "Medium"

    else:
        risk = "High"



    credit = {

        "Credit_ID": credit_id,

        "Customer_ID": customer["Customer_ID"],

        "Credit_Score": credit_score,

        "Credit_Rating": rating,

        "Risk_Category": risk,

        "Credit_Check_Date": "2026-01-01"

    }


    credit_scores.append(credit)

    credit_id += 1



credit_df = pd.DataFrame(credit_scores)


# Save dataset

credit_df.to_csv(
    DATA_DIR / "Credit_Scores.csv",
    index=False
)


print("Credit Scores dataset created successfully!")
print(credit_df.head())

print(
    f"\nTotal Credit Records: {len(credit_df):,}"
)
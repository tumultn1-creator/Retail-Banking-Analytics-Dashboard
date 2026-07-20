import subprocess
from pathlib import Path


# Find Python folder
PYTHON_DIR = Path(__file__).resolve().parent


scripts = [
    "Generate_Customers.py",
    "Generate_Accounts.py",
    "Generate_Transactions.py",
    "Generate_Loans.py",
    "Generate_Credit_Scores.py"
]


print("Starting Banking Analytics Data Pipeline...\n")


for script in scripts:

    print(f"Running {script}...")

    subprocess.run(
        [
            "python",
            str(PYTHON_DIR / script)
        ]
    )

    print(f"{script} completed!\n")


print("================================")
print("Banking Analytics Data Pipeline Complete!")
print("All datasets generated successfully.")
print("================================")
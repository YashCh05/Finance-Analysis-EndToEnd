import pandas as pd
import numpy as np
import random
import datetime as dt

# Departments
departments = ["HR", "IT", "Finance", "Sales", "Marketing", "Operations", "Legal", "Support", "Procurement", "R&D"]

# Categories
expense_categories = ["Travel", "Software", "Supplies", "Utilities", "Training", "Maintenance", "Advertising", "Contractors"]

# Regions
regions = ["North", "South", "East", "West", "Central", "International", "Online", "Corporate"]

# Payment modes
payments = ["Card", "Bank Transfer", "UPI", "Cash"]

# Generate large finance dataset
data = []
for i in range(1, 2001):
    date = dt.date(2025, random.randint(1, 12), random.randint(1, 28))
    dept = random.choice(departments)
    category = random.choice(expense_categories)
    region = random.choice(regions)
    payment = random.choice(payments)
    
    revenue = random.randint(5000, 150000)
    expense = random.randint(2000, int(revenue * 0.8))
    profit = revenue - expense

    data.append([i, date, dept, category, region, payment, revenue, expense, profit])

df = pd.DataFrame(data, columns=[
    "Transaction_ID", "Date", "Department", "Expense_Category",
    "Region", "Payment_Method", "Revenue", "Expense", "Profit"
])

# Save file
df.to_csv("finance_day12_transactions.csv", index=False)

df.head()



dept_data = {
    "Department": departments,
    "Manager": ["Amit", "Neha", "Vikram", "Sonia", "Ravi", "Karan", "Shruti", "Kabir", "Tara", "Divya"],
    "Employees_Count": [random.randint(10, 60) for _ in departments]
}

df_dept = pd.DataFrame(dept_data)
df_dept.to_csv("finance_day12_departments.csv", index=False)
df_dept



region_data = {
    "Region": regions,
    "Country": ["India", "India", "India", "India", "India", "US", "Online", "India"],
    "Currency": ["INR", "INR", "INR", "INR", "INR", "USD", "Mixed", "INR"]
}

df_region = pd.DataFrame(region_data)
df_region.to_csv("finance_day12_regions.csv", index=False)
df_region

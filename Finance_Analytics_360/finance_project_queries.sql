-- Creating databse 
CREATE DATABASE finance_day12;
USE finance_day12;

-- Renaming tables 
RENAME TABLE finance_day12_transactions TO finance_transactions;
RENAME TABLE finance_day12_departments TO  departments;
RENAME TABLE finance_day12_regions TO regions;

-- Revenue by Department 
CREATE VIEW v_revenue_by_department AS
SELECT
     Department,
     SUM(Revenue) AS Total_Revenue,
     SUM(Expense) AS Total_Expense,
     SUM(Profit) AS Total_Profit
FROM finance_transactions
GROUP BY Department;

-- Monthly Summary 
CREATE VIEW v_monthly_summary AS
SELECT
     MONTH(Date) AS Month_Num,
     MONTHNAME(Date) AS Month,
     SUM(Revenue) AS Total_Revenue,
     SUM(Expense) AS Total_Expense,
     SUM(Profit) AS Total_Profit
FROM finance_transactions
GROUP BY Month_Num,Month
ORDER BY Month_Num;

-- Region Performance
CREATE VIEW v_region_performance AS
SELECT
     Region,
     SUM(Revenue) AS Revenue,
     SUM(Expense) AS Expense,
     SUM(Profit) AS Profit
FROM finance_transactions
GROUP BY Region;

-- Top Profit Transaction 
CREATE VIEW v_top_profit_transaction AS
SELECT
     *
FROM finance_transactions
ORDER BY Profit DESC
LIMIT 100;

-- Finance Master for Power BI
CREATE VIEW v_finance_master AS
SELECT
     f.Transaction_ID,
     f.Date,
     f.Department,
     f.Expense_Category,
     f.Region,
     f.Payment_Method,
     f.Revenue,
     f.Expense,
     f.Profit,
     d.Manager,
     d.Employees_Count,
     r.Country,
     r.Currency
FROM finance_transactions AS f
LEFT JOIN departments AS d ON f.Department = d.department 
LEFT JOIN regions AS r ON f.Region = r.Region;

SELECT *
FROM 
v_finance_master
LIMIT 100;

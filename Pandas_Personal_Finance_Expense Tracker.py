import pandas as pd

#loaad the csv data
# Load your expenses dataset into a DataFrame

expenses=pd.read_csv('expenses.csv')
print(expenses)
print(expenses.columns)
#calculate total amount
# Sum of all transactions (income + expenses)
print(expenses['amount'].sum())

#Positive amounts → income
income=expenses['amount'][expenses['amount']>0]
print(income)
# Negative amounts → expenses/bills
bills=expenses['amount'][expenses['amount']<0]
print(bills)

# Group expenses by category
# Aggregate total expenses for each category

expenses_by_category=expenses[expenses['amount']<0].groupby('category')['amount'].sum()
print(expenses_by_category)

#the biggest expenses category
# Biggest expense is the most negative value

biggest_expenses=expenses_by_category.min()
amount_category=expenses_by_category.idxmin()
print(biggest_expenses,' With ',amount_category)
#identify high-spending transactions

high_spending_day=expenses[expenses['amount']<0]#.groupby('date')['amount']
print(high_spending_day.head(1))

# Transactions where spending > $20

high_spending_days=high_spending_day[high_spending_day['amount']<-20]
print(high_spending_days)

# Total expenses per day
# Group expenses by date to see daily totals

total_expenses_per_day=expenses[expenses['amount']<0].groupby('date')['amount'].sum()
print(total_expenses_per_day)

#running total of all transactions to see balance over time

balance=expenses['amount'].cumsum()
print(balance)
expenses['balance']=balance
print(expenses)
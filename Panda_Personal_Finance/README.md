# Panda Personal Finance

A Python project that uses `pandas` to analyze personal income and expenses from a CSV file.

## Files

- `personal_finance.py`: main script that loads and analyzes the data.
- `expenses.csv`: the dataset, with one transaction per row.

## Requirements

- Python 3
- The `pandas` library:

```
pip install pandas
```

## Data format

The script expects an `expenses.csv` file with at least these columns:

| Column | Description |
|--------|-------------|
| `date` | Date of the transaction |
| `category` | Category of the transaction (food, transport, etc.) |
| `amount` | Positive for income, negative for expenses |

## How to run

Make sure `expenses.csv` is in the same folder as the script, then run:

```
python personal_finance.py
```

## What the script does

1. Loads the transactions into a DataFrame with `pd.read_csv`.
2. Calculates the total amount of all transactions.
3. Separates income (positive amounts) from bills (negative amounts).
4. Groups expenses by category and finds the category where the most money was spent.
5. Finds high-spending transactions (more than $20).
6. Calculates the total expenses for each day.
7. Computes a running balance with `cumsum()` and adds it as a new `balance` column.

## Concepts practiced

- Reading CSV files with pandas
- Filtering data with conditions (boolean indexing)
- `groupby` and aggregation (`sum`)
- `idxmin` to find the category with the largest expense
- Running totals with `cumsum`

import csv
from datetime import datetime

def add_expense(date, category, description, amount):
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")

def view_expenses():
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Description: {row[2]}, Amount: ₹{row[3]}")

def analyze_expenses():
    categories = {}
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            category = row[1]
            amount = float(row[3])
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("Expense Analysis:")
    for category, total_amount in categories.items():
        print(f"Category: {category}, Total Spent: ₹{total_amount:.2f}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            amount = input("Enter the amount (in INR): ")
            add_expense(date, category, description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            analyze_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
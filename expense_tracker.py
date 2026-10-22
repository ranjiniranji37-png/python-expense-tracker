"""
Expense Tracker - Python Mini Project
Codomax Digital Solutions AI & ML Internship - Module 2
Author: Ranjini K
"""

import json
import os
from datetime import date

DATA_FILE = "expenses.json"


def load_expenses():
    """Load expenses from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    title = input("Enter expense title: ").strip()
    category = input("Enter category (Food/Travel/Shopping/Bills/Other): ").strip().title()
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expenses.append({
        "title": title or "Untitled",
        "category": category or "Other",
        "amount": amount,
        "date": str(date.today()),
    })
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n{:<4} {:<12} {:<18} {:<12} {:>10}".format("No", "Date", "Title", "Category", "Amount"))
    print("-" * 60)
    for i, e in enumerate(expenses, start=1):
        print("{:<4} {:<12} {:<18} {:<12} {:>10.2f}".format(
            i, e["date"], e["title"][:17], e["category"], e["amount"]))
    print("-" * 60)


def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        number = int(input("Enter expense number to delete: "))
        removed = expenses.pop(number - 1)
        save_expenses(expenses)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid expense number.")


def show_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    total = sum(totals.values())
    print("\n--- Expense Summary ---")
    for category, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        percent = amount / total * 100
        print(f"{category:<12} {amount:>10.2f}  ({percent:.1f}%)")
    print("-" * 30)
    print(f"{'Total':<12} {total:>10.2f}")
    print(f"Highest spending category: {max(totals, key=totals.get)}")


def main():
    expenses = load_expenses()
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Summary by Category")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            show_summary(expenses)
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

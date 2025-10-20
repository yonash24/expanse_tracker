# Main.py

import sys
from tabulate import tabulate
import mysql.connector

from Expense import Expense
from FoodExpense import FoodExpense
from UtilityExpense import UtilityExpense
from TravelExpense import TravelExpense

def connect_database():
    try:
        return mysql.connector.connect(
           host='localhost',
           user='root',
           password='YOUR_PASSWORD_HERE',
           database='expense_tracker'
       )
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        print("Please ensure your MySQL server is running and the password in Main.py and Expense.py is correct.")
        sys.exit(1)

def view_all_expenses():
    try:
        connection = connect_database()
        cursor = connection.cursor()
        query = "SELECT id, date, category, amount, description FROM expenses ORDER BY date DESC"
        cursor.execute(query)
        records = cursor.fetchall()
        
        if not records:
            print("\nNo expenses found.")
            return False
        
        headers = ["ID", "Date", "Category", "Amount", "Description"]
        print("\n--- All Expenses ---")
        print(tabulate(records, headers=headers, tablefmt="grid"))
        return True
    
    except mysql.connector.Error as err:
        print(f"Error fetching expenses: {err}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_expense_details():
    try:
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        extra_info = input("Enter extra info (e.g., store name, payment method): ")
        return amount, description, extra_info
    except ValueError:
        print("\nInvalid amount. Please enter a number.")
        return None, None, None

def add_expense():
    print("\n--- Add New Expense ---")
    print("Select Category:")
    print("1. Food")
    print("2. Utility")
    print("3. Travel")
    
    try:
        choice = int(input("Enter your choice (1-3): "))
        amount, description, extra_info = get_expense_details()
        
        if amount is None:
            return
            
        expense = None
        if choice == 1:
            expense = FoodExpense(amount, description, extra_info)
        elif choice == 2:
            expense = UtilityExpense(amount, description, extra_info)
        elif choice == 3:
            expense = TravelExpense(amount, description, extra_info)
        else:
            print("Invalid category choice.")
            return
        
        expense.add_to_database()
        
    except ValueError:
        print("\nInvalid choice. Please enter a number.")

def remove_expense():
    print("\n--- Remove Expense ---")
    if not view_all_expenses():
        return

    try:
        expense_id = int(input("Enter the ID of the expense to remove: "))
        generic_expense = Expense(0, "", "", "") 
        generic_expense.remove_from_database(expense_id)

    except ValueError:
        print("\nInvalid ID. Please enter a number.")

def main():
    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Remove an expense")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_all_expenses()
            elif choice == 3:
                remove_expense()
            elif choice == 4:
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                
        except ValueError:
            print("\nInvalid input. Please enter a number.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")


if __name__ == '__main__':
    with open('ql -u root -p', 'r') as f:
        log_content = f.read()
        if 'Active: inactive (dead)' in log_content:
            print("Warning: Your MySQL service appears to be inactive.")
            print("Please start it with a command like 'sudo service mysql start' before running the program.")
    main()
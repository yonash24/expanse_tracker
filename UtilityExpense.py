from Expense import Expense
import mysql.connector
import pandas as pd

class UtilityExpense(Expense):

    def __init__(self, amount, description, extra_info, category='Utility'):
        super().__init__(amount, description,category, extra_info)


    def add_to_database(self):
        super().add_to_database()
    def remove_from_database(self, utility_expense_id):
        super().remove_from_database(utility_expense_id)

    def update_in_database(self,utility_expense_id):
        super().update_in_database(utility_expense_id)

    def display_details(self):
        super().display_details()

    def get_utility_expenses(self):
        connect = self.connect_database()
        cursor = connect.cursor()
        query = "SELECT amount FROM expenses WHERE category = Food"
        cursor.execute(query)
        amount = cursor.fetchall()
        cursor.close()
        connect.close()

        return amount

    def get_daily_utility_expense(self):
        pass

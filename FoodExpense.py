from Expense import Expense
import mysql.connector

class FoodExpense(Expense):

    def __init__(self, amount, description,  extra_info, category = 'Food'):
        super().__init__( amount, description, category, extra_info)


    def add_to_database(self):
        super().add_to_database()


    def remove_from_database(self,food_expense_id):
        super().remove_from_database(food_expense_id)


    def update_in_database(self,food_expense_id):
        super().update_in_database(food_expense_id)


    def display_details(self):
        super().display_details()

    def get_food_expenses(self):
        pass

    def get_daily_food_expense(self):
        pass
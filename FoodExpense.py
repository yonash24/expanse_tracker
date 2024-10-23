from Expense import Expense
import mysql.connector

class FoodExpense(Expense):

    def __init__(self, amount, description,  extra_info, category = 'Food'):
        super().__init__( amount, description, category, extra_info)


    def add_to_database(self):
        super().add_to_database()


    def remove_from_database(self):
        super().remove_from_database()


    def update_in_database(self):
        super().update_in_database()


    def display_details(self):
        super().display_details()


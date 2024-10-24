from Expense import Expense
import mysql.connector

class TravelExpense(Expense):

    def __init__(self, amount, description, extra_info, category='Travel'):
        super().__init__( amount, description, category,extra_info)


    def add_to_database(self):
        super().add_to_database()

    def remove_from_database(self,travel_expense_id):
        super().remove_from_database(travel_expense_id)

    def update_in_database(self,travel_expense_id):
        super().update_in_database(travel_expense_id)

    def display_details(self):
        super().display_details()


    def get_travel_expenses(self):
        pass

    def get_daily_travel_expense(self):
        pass
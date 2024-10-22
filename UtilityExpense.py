from Expense import Expense
import mysql.connector

class UtilityExpense(Expense):

    def __init__(self, amount, description,category, extra_info, utility_type):
        super().__init__(amount, description,category, extra_info)
        self.utility_type = utility_type

    def add_to_database(self):
        pass
    def remove_from_database(self):
        pass

    def update_in_database(self):
        pass

    def display_details(self):
        pass



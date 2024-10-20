from Expense import Expense

class UtilityExpense(Expense):

    def __init__(self, date, amount, description, utility_type):
        super().__init__(date, amount, description)
        self.utility_type = utility_type

    def add_to_database(self):
        pass
    def remove_from_database(self):
        pass

    def update_in_database(self):
        pass

    def display_details(self):
        pass



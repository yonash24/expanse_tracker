from Expense import Expense

class FoodExpense(Expense):

    def __init__(self, date, amount, description, meal_type):
        super().__init__(date, amount, description)
        self.meal_type = meal_type

    def add_to_database(self):
        pass

    def remove_from_database(self):
        pass


    def update_in_database(self):
        pass


    def display_details(self):
        pass


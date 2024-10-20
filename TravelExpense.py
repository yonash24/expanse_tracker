from Expense import Expense

class TravelExpense(Expense):

    def __init__(self, date, amount, description, destination):
        super().__init__(date, amount, description)
        self.destination = destination

    def add_to_database(self):
        pass
    def remove_from_database(self):
        pass

    def update_in_database(self):
        pass

    def display_details(self):
        pass



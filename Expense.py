from abc import ABC, abstractmethod


class Expense(ABC):

    def __init__(self, date, amount, description):
        self.date = date
        self.amount = amount
        self.description = description

    @abstractmethod
    def add_to_database(self):
        pass
    @abstractmethod
    def remove_from_database(self):
        pass

    @abstractmethod
    def update_in_database(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


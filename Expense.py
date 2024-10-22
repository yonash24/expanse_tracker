from abc import ABC, abstractmethod
import datetime
from unicodedata import category

import mysql.connector

class Expense(ABC):

    def __init__(self, amount, description, category, extra_info):
        self.date =  datetime.datetime.now()
        self.amount = amount
        self.description = description
        self.category = category
        self.extra_info = extra_info

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


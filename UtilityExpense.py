from Expense import Expense
import mysql.connector
from datetime import date

class UtilityExpense(Expense):
    """
    Represents a utility-specific expense, inheriting from the base Expense class.
    """

    # Initializes a UtilityExpense object.
    def __init__(self, amount, description, extra_info, category='Utility'):
        super().__init__(amount, description, category, extra_info)

    # Note: The methods add_to_database, remove_from_database, update_in_database,
    # and display_details are inherited directly from the Expense class
    # and do not need to be redefined here unless you want to change their behavior.

    # Retrieves all utility expense amounts from the database.
    def get_utility_expenses(self):
        try:
            connect = self.connect_database()
            cursor = connect.cursor()
            query = "SELECT amount FROM expenses WHERE category = %s"
            cursor.execute(query, ('Utility',))
            amounts = cursor.fetchall()
            # The query returns a list of tuples, e.g., [(100,), (50,)]; this extracts the numbers.
            return [item[0] for item in amounts]
        except mysql.connector.Error as err:
            print(f"Error fetching utility expenses: {err}")
            return []
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()

    # Calculates the total utility expenses for the current day.
    def get_daily_utility_expense(self):
        try:
            connect = self.connect_database()
            cursor = connect.cursor()
            # This query sums amounts for the 'Utility' category where the date matches today.
            query = "SELECT SUM(amount) FROM expenses WHERE category = %s AND DATE(date) = %s"
            cursor.execute(query, ('Utility', date.today()))
            result = cursor.fetchone()[0]
            # If no expenses are found, the result is None; we return 0 instead.
            return float(result) if result is not None else 0.0
        except mysql.connector.Error as err:
            print(f"Error fetching daily utility expense: {err}")
            return 0.0
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
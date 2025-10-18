
from Expense import Expense
import mysql.connector
from datetime import date

class TravelExpense(Expense):
    """
    מייצג הוצאת נסיעות ספציפית, יורש ממחלקת הבסיס Expense.
    """


    def __init__(self, amount, description, extra_info, category='Travel'):
        super().__init__(amount, description, category, extra_info)


    def get_travel_expenses(self):
        try:
            connect = self.connect_database()
            cursor = connect.cursor()
            query = "SELECT amount FROM expenses WHERE category = %s"
            cursor.execute(query, ('Travel',))
            amounts = cursor.fetchall()

            return [item[0] for item in amounts]
        except mysql.connector.Error as err:
            print(f"Error fetching travel expenses: {err}")
            return []
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()

    def get_daily_travel_expense(self):
        try:
            connect = self.connect_database()
            cursor = connect.cursor()

            query = "SELECT SUM(amount) FROM expenses WHERE category = %s AND DATE(date) = %s"
            cursor.execute(query, ('Travel', date.today()))
            result = cursor.fetchone()[0]

            return float(result) if result is not None else 0.0
        except mysql.connector.Error as err:
            print(f"Error fetching daily travel expense: {err}")
            return 0.0
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
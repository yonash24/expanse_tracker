from Expense import Expense
import mysql.connector
from datetime import date

class FoodExpense(Expense):


    def __init__(self, amount, description, extra_info, category='Food'):
        super().__init__(amount, description, category, extra_info)

    def get_food_expenses(self):
        try:
            connect = self.connect_database()
            cursor = connect.cursor()
            query = "SELECT amount FROM expenses WHERE category = %s"
            cursor.execute(query, ('Food',))
            amounts = cursor.fetchall()
            return [item[0] for item in amounts]
        except mysql.connector.Error as err:
            print(f"Error fetching food expenses: {err}")
            return []
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()

    def get_daily_food_expense(self):
        try:
            connect = self.connect_database()
            cursor = connect.cursor()
            query = "SELECT SUM(amount) FROM expenses WHERE category = %s AND DATE(date) = %s"
            cursor.execute(query, ('Food', date.today()))
            result = cursor.fetchone()[0]
            return float(result) if result is not None else 0.0
        except mysql.connector.Error as err:
            print(f"Error fetching daily food expense: {err}")
            return 0.0
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
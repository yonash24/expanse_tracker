import datetime
import mysql.connector



class Expense:
    def __init__(self, amount, description, category, extra_info):
        self.date =  datetime.datetime.now()
        self.amount = amount
        self.description = description
        self.category = category
        self.extra_info = extra_info

    def connect_database(self):
       return mysql.connector.connect(
           host='localhost',
           user='root',
           database='expense_tracker'
       )

    def add_to_database(self):
            connection = self.connect_database() #establish connection to db
            cursor = connection.cursor()   #create cursor object
            query = '''
                INSERT INTO expenses(amount, description category, extra_info ,date)
                VALUES(%S, $s, $s, $s, $s)
            '''
            values = (self.amount, self.description, self.category, self.extra_info, self.date) #the values we sign for each parameter at the quey
            cursor.execute(query,values)    #execute in mysql query with the values
            connection.commit()     #commit the transaction
            cursor.close()      # close the cursor
            connection.close()      #close the connection

    def remove_from_database(self, expense_id):
            connection = self.connect_database()
            cursor = connection.cursor()
            query = '''
                DELETE FROM expenses
                WHERE id = %s;
            '''
            cursor.execute(query,expense_id)
            connection.commit()
            cursor.close()
            connection.close()

    def update_in_database(self, expense_id):
            connection = self.connect_database()
            cursor = connection.cursor()
            query = '''
                UPDATE expenses 
                SET date = $s, amount = %s, description = %s, category = $s, extra_info = %s
                WHERE id = $s
            '''
            values = (self.date, self.amount, self.description, self.category, self.extra_info, expense_id)
            cursor.execute(query,values)
            connection.commit()
            cursor.close()
            connection.close()

    def display_details(self):
            return f"Date: {self.date}, Amount:{self.amount}, Description:{self.description}, Category:{self.category}, Extra Info:{self.extra_info}"

















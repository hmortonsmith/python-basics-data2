import pyodbc


class Conn_ms_sql():
    # when we initialise, make the connection
    def __init__(self, server='localhost,1433', database='Northwind', username='SA', password='Passw0rd2018'):
        # Our variables to create a connection
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.docker_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')
        self.cursor = self.docker_conn.cursor()

    def sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_all_products(self):
        # query db for all products
        # iterate and use fetchone
            # going to actually print
        query = self.sql_query("SELECT * FROM Products")
        while True:
            row = query.fetchone()
            if row is None:
                break
            print(row)

    def average_unit_price(self):
        query = self.sql_query("SELECT * FROM Products")
        all_unit_prices = []
        while True:
            row = query.fetchone()
            if row is None:
                break
            all_unit_prices.append(int(row.UnitPrice))
        avg_unit_price = sum(all_unit_prices) / len(all_unit_prices)
        return avg_unit_price

    def print_product_details(self, product_name):
        query = self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKE '%{product_name}%'")
        while True:
            row = query.fetchone()
            if row is None:
                break
            else:
                return row

# end

from connection_db_oop import *

northwind_db = Conn_ms_sql()

# print(northwind_db.sql_query("SELECT TOP 10 * FROM Products"))
#
# northwind_db.print_all_products()
#
# print(northwind_db.average_unit_price())

# filter products by name
print(northwind_db.print_product_details('Chai'))

# filter customer via company name

# filter customer via country


# import connection
# import passenger class

# load db information
# create passenger object from db information
# save it to db (sql)

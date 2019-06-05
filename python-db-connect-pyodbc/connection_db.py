import pyodbc

# Our variables to create a connection
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Making a connection
docker_northwind_cc = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')

# Creating a cursor allowing us to execute SQL functions on connected db
cursor = docker_northwind_cc.cursor()
#print(cursor)

# # Maintains state
# cursor.execute("SELECT * FROM Customers WHERE city LIKE 'London';")
#
# # fetch one
# # row = cursor.fetchone()
# # print(row)
#
# # fetch all
# rows_all = cursor.fetchall()
#
# print(len(rows_all))
# for data in rows_all:
#     print('Company Name:', data.CompanyName, '\nFax Number:', data.Fax, '\nName of Contact:', data.ContactName, '\n\n')
#

# find companies without a fax number
# cursor.execute("SELECT * FROM Customers WHERE Fax is NULL;")
# rows_all = cursor.fetchall()
# for data in rows_all:
#     print('Company Name:', data.CompanyName, '\nPhone Number:', data.Phone, '\nName of Contact:', data.ContactName, '\n\n')
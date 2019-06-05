from connection_db import *
import csv

rows = cursor.execute("SELECT * FROM Customers WHERE City = 'London' AND (ContactName LIKE '%n%' OR ContactName LIKE '%m%')")
final_useful_data = []
while True:
    record = rows.fetchone()
    if record is None:
        break
    else:
        print(record.ContactName)

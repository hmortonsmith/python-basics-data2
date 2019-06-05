from connection_db import *
import csv

# I want all employees in london that have a 'b' or a 'c' in their name
# i should be able to ask you to
    # print using a while loop and fetchone
    # get a CSV out with the relevant data

rows = cursor.execute("SELECT * FROM Customers WHERE City = 'London' AND (ContactName LIKE '%n%' OR ContactName LIKE '%m%')")
final_useful_data = []
while True:
    record = rows.fetchone()
    if record is None:
        break
    else:
        useful_data = []
        useful_data.append(record.CompanyName)
        useful_data.append(record.ContactName)
        useful_data.append(record.Address)
        useful_data.append(record.PostalCode)
        useful_data.append(record.Phone)
        final_useful_data.append(useful_data)


#print(useful_data)
new_file = open('customer_specific_criteria.csv', 'w', newline='')
    # write to that file
with new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerows(final_useful_data)

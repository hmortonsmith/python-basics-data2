# fetchall is dangerous
# fetchall can deplete our instant memory if there is too much data
# bringing our serves to a halt

# we can use a while loop, fetching one at a time
# be aware of query optimisation for external DB services and hosted DBs. These usually charge per call on DB

from connection_db import *

rows = cursor.execute('SELECT * FROM Products')

while True:
    record = rows.fetchone()
    if record is None:
        break
    else:
        print(record.UnitPrice)

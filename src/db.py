import pyodbc

db_file = 'C:/Users/Matej/Desktop/Seal-Pattern-Recognition/Seal_centre_db/seal_demo/seal_demo.mdb'

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;' % db_file)

cursor = conn.cursor()

cursor.execute('select * from IDs')

for line in cursor.fetchall():
    print(line)


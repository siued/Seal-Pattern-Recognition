import requests

if  input('delete all images? (y/n)') != 'y':
    exit()

url = "http://localhost:8080/api/image"

res = requests.delete(url, json={'gid_list': [1, 2, 3, 4, 5, 6, 7, 8, 9]})
print(res.json())



# DB code for future reference

# import pyodbc
#
# db_file = 'C:/Users/Matej/Desktop/Seal-Pattern-Recognition/Field_db/seal_demo/seal_demo.mdb'
#
# conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;' % db_file)
#
# cursor = conn.cursor()
#
# # table_name = 'sighting'
# #
# # for row in cursor.columns(table = table_name):
# #         print(row.column_name)
#
# # cursor.execute('update DataPath set Localpath = \'C:/Users/Matej/Desktop/Seal-Pattern-Recognition/Field_db/seal_demo/\'')
# # conn.commit()
#
# cursor.execute('select * from image')
#
# list = cursor.fetchall()
# # for row in list:
# #     print(row)
# print(len(list))

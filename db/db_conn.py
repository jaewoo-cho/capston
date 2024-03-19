import pymssql

server = '127.0.0.1:1433'
username = '***'
password = '***'
database = '***'

# MSSQL CONNECT
conn = pymssql.connect(server, username, password, database)
cursor = conn.cursor()

# SELECT
cursor.execute('SELECT * from test_table;')
for row in cursor:
    print(row)
    print("connect successfully!")
# # INSERT
# data = 'ABC!!'
# # syntax error 발생을 막기 위해, 쌍따옴표로 감싸줌
# query = "INSERT INTO POST (CONTENTS) VALUES ('" + str(data) + "')"
# cursor.execute(query)
# conn.commit()
#
# # UPDATE
# data = 'ABC!!'
# query = "UPDATE POST set CONTENTS = '" + str(data) + "'  where POST_NO = 11"
# cursor.execute(query)
# conn.commit()
#
# # DELETE
# data = 'ABC!!'
# query = "DELETE FROM POST WHERE CONTENTS = '" + str(data) + "'"
# cursor.execute(query)
# conn.commit()
#
# # Connect 종료
# conn.close()
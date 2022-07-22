import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", password = "root")
print(mydb)
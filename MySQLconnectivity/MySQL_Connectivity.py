import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", password = "root")
print(mydb)
#Create a cursor to execute queries
#cursor = mydb.cursor()
# Create a new database called sudhanshu123
#cursor.execute("Create database sudhanshu123")
# To show the databases
#cursor.execute("SHOW DATABASES")
#Create a Table in the database
#cursor.execute ("create table sudhanshu123.ineuron1(employee_id int(10), emp_name varchar(80), emp_emailid varchar(80),emp_salary int(6))")
#To show the entire table and data from the database
#cursor.execute("select * from  sudhanshu123.ineuron1")
#varchar always represents in single quotes
# To insert the data into the table created above
#cursor.execute("insert into sudhanshu123.ineuron1 values(101, 'kumar', 'sudh@ineuron.ai', 100)")
#cursor.execute("insert into sudhanshu123.ineuron1 values(101, 'kumar', 'sudh@ineuron.ai', 100)")
#cursor.execute("insert into sudhanshu123.ineuron1 values(101, 'kumar', 'sudh@ineuron.ai', 100)")
#cursor.execute("insert into sudhanshu123.ineuron1 values(101, 'kumar', 'sudh@ineuron.ai', 100)")
# Do not forget to commit the changes as below. commit is required to make the changes in the database
#mydb.commit()
#print(cursor.fetchall())
#cursor.execute("select * from  sudhanshu123.ineuron1")
#for i in cursor.fetchall():
    #print(i)
#This will show all the data from the selected/mentioned columns
#cursor.execute("select employee_id, emp_emailid from sudhanshu123.ineuron1")
#for i in cursor.fetchall():
    #print(i)
#cursor.execute('insert table sql_functions.conversion_function(Function_name varchar(10), syntax varchar (10), Description varchar(10))')
#cursor.execute("insert into sql_Functions.conversion_function values('conversion', 'dtypes')")
#cursor.execute("ALTER TABLE sql_Functions.conversion_function ADD syntax varchar(20)")
#cursor.execute("insert into sql_Functions.conversion_function values('PARSE', 'dtypes')")
#cursor.execute("insert into sql_Functions.conversion_function values('TRYCAST', 'dtypes')")
#cursor.execute("insert into sql_Functions.conversion_function values('TRYCONVERT', 'dtypes')")
#cursor.execute("insert into sql_Functions.conversion_function values('TRYPARSE', 'dtypes')")

#mydb.commit()




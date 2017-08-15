import pymysql

db=pymysql.connect(host="localhost",user="root",password="1234",database="python")
mycursor=db.cursor()
mycursor.execute("SHOW TABLES")
print(mycursor.fetchall())
mycursor.execute("""INSERT INTO employee(id,name) values(1,'saurav')""")
print(mycursor.fetchall())
mycursor.execute("SELECT * FROM employee")
print(mycursor.fetchall())

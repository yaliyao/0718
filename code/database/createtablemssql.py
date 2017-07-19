import pymssql

# Open database connection
db = pymssql.connect("192.168.88.90","pyuser","python","testdb" )
#db = pymssql.connect("192.168.88.90","sa","2Password!","testdb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """
   IF OBJECT_ID('EMPLOYEE', 'U') IS NOT NULL
      DROP TABLE EMPLOYEE
   CREATE TABLE EMPLOYEE (
   FIRST_NAME  VARCHAR(20) NOT NULL,
   LAST_NAME  VARCHAR(20),
   AGE INT,  
   SEX VARCHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)

# you must call commit() to persist your data 
# if you don't set autocommit to True
db.commit()

# disconnect from server
db.close()

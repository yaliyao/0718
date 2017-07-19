import pymssql

# Filename for CSV data
fname = 'dht22sensor.sh.csv'

# Open file for read
fp=open(fname,"r")

# Open database connection
db = pymssql.connect("100.20.240.1410","","","picachu" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

for line in fp:
    line = line.rstrip('\n')
    data = line.split(',')
    print(data)
    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO dht22data
         VALUES ('{}', {}, {})""".format(data[0], data[1], data[2])
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

# disconnect from server
db.close()

# close file
fp.close()

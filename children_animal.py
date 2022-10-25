# import sqlite3 module
import sqlite3

# create con object to connect
# the database family_db.db
con = sqlite3.connect("family_db.db")

# drop table
try:
    con.execute("DROP TABLE Children")
    print("data dropped successfully")
    con.execute("DROP TABLE Animals")
    print("data dropped successfully")
except:
    print("Creating new Tables.")
# create the cursor object
cur = con.cursor()
# execute the script by creating the table
# named children and insert the data
def children():
    cur.executescript("""
	create table children(
		child_id,
		child_name,
		c_Birth_date,
        c_Age
	);

    insert into Children values ( '1', 'Mylo','02/06/2014','8' );
    insert into Children values ( '2', 'Alanna' ,'05/25/2015','7' );
    insert into Children values ( '3', 'Georgie','11/12/2019','2'  );
    insert into Children values ( '4', '','','' );
    insert into Children values ( '5', '' ,'','' );
    insert into Children values ( '6', '','',''  );
    insert into Children values ( '7', '','',''  );
	""")

def animals():
    cur.executescript("""
	create table Animals(
		animal_id,
		animal_name,
		a_Birth_date,
        a_Age
	);
      
    insert into Animals values ( '4', 'Princes','06/03/2018','5' );
    insert into Animals values ( '5', 'Lacey' ,'12/25/2019','2' );
    insert into Animals values ( '6', 'Izzy','08/12/2020','2'  );
    insert into Animals values ( '7', 'Blue','06/22/2021','1'  );	
	""")
children()
print("Children table created.")
print("Children Table: ")
# display the data in the table by
# executing the cursor object
cur.execute("SELECT * from Children")
# fetch all the data
print(cur.fetchall())
print()

animals()
print("Animal table created.")
print("Animal Table: ")
# display the data in the table by
# executing the cursor object
cur.execute("SELECT * from Animals")
# fetch all the data
print(cur.fetchall())
print()

# Query for Union
sql = '''SELECT child_id, child_name, c_Birth_date, c_Age 
FROM children 
UNION
SELECT animal_id, animal_name, a_Birth_date, a_Age
FROM Animals;'''
print("Union With false Entries:") 
# Executing the query
cur.execute(sql)
# Fetching rows from the result table
result = cur.fetchall()
for row in result:
   print(row)


    
sql = 'DELETE FROM children WHERE child_id="4"'
cur.execute(sql)
sq2 = 'DELETE FROM children WHERE child_id="5"'
cur.execute(sq2)
sq3 = 'DELETE FROM children WHERE child_id="6"'
cur.execute(sq3)
sq4 = 'DELETE FROM children WHERE child_id="7"'
cur.execute(sq4)

sql = '''SELECT child_id, child_name, c_Birth_date, c_Age 
FROM children 
UNION
SELECT animal_id, animal_name, a_Birth_date, a_Age
FROM Animals;'''
  
print("")
print("Union where False Entries have been deleted:")
# Executing the query
cur.execute(sql)
# Fetching rows from the result table
result = cur.fetchall()
for row in result:
   print(row)

average = (8 + 7 + 2 + 5 + 2 + 2 + 1)/ 7

print("The average age of minors is: ", round(average))

con.commit()








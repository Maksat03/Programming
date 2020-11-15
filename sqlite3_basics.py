import sqlite3 # sqlite3 is package for works with data/databases

# Drop database table
conn = sqlite3.connect("db_file.db") # connection with db file
cursor = conn.cursor() # cursor for execute something (для SQL запроса)

cursor.execute("DROP TABLE IF EXISTS db") # Drop db tabel if exists

cursor.close() # Close cursor
conn.close() # Close connection



input("Continue? (y/n)\n")



# Create new database table
conn = sqlite3.connect("db_file.db") # connection with db file
cursor = conn.cursor() # cursor for execute something (для SQL запроса)

# columns for database table
columns = ''' 
          id                    INTEGER PRIMARY KEY,
          name                  TEXT,
          surname               TEXT,
          age                   INTEGER
          '''
        # columns names         data type(for save data)
cursor.execute('''CREATE TABLE IF NOT EXISTS db({columns})'''.format(columns=columns)) # Create database table

cursor.close() # Close cursor
conn.close() # Close connection



input("Continue? (y/n)\n")



# Inserting variables to database table
conn = sqlite3.connect("db_file.db") # connection with db file
cursor = conn.cursor() # cursor for execute something (для SQL запроса)

cursor.execute("INSERT INTO db VALUES(1, 'Unknown', 'Kantai', 16)")                 # Example #1\
cursor.execute("INSERT INTO db (name) VALUES('Maksat')")                            # Example #2 \
cursor.execute("INSERT INTO db (surname) VALUES('Kantai')")                         # Example #3  \ Inserting variables to
cursor.execute("INSERT INTO db (name) VALUES(?)", ("Maksat", ))                     # Example #4  /      database table
cursor.execute("INSERT INTO db (surname) VALUES(?)", ("Kantai", ))                  # Example #5 /
cursor.execute("INSERT INTO db (name, surname) VALUES(?, ?)", ("Maksat", "Kantai")) # Example #6/

people = [
        (7, 'Sayat', 'Afeiev', 16),
        (8, 'Zhasiya', 'Serikkyzy', 15),
        (9, 'Batyrbek', 'Orazymbetov', 51),
        (10, 'Akmaral', 'Pernesheva', 47),
]
cursor.executemany("INSERT INTO db VALUES(?, ?, ?, ?)", people)

conn.commit() # commit(*совершить) / save change(*сохранить изменения)

cursor.close() # Close cursor
conn.close() # Close connection



input("Continue? (y/n)\n")



def print_res(additional_text="\n"):
    """
    function named 'print_res' need for fetch data and print them
    """
    print(additional_text)
    conn.commit() # if just selected data from db table, then no need write this. This need write when something changed
    data = cursor.fetchall() # fetch all data
    print(data) # print fetched data
    [print(row) for row in data] # print all rows of fetched data
    print("\n\n\n")

print("Function named 'print_res' created\n"+print_res.__doc__)
input("Continue? (y/n)\n")

# Read from (SELECT) Database table
conn = sqlite3.connect("db_file.db") # connection with db file
cursor = conn.cursor() # cursor for execute something (для SQL запроса)

# Example #1
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text="Select *(all) data from db table") # print result

# Example #2
cursor.execute('SELECT * FROM db WHERE name = "Maksat"') # Select *(all) data from db table where variable name = "Maksat"
print_res(additional_text='Select *(all) data from db table where variable name = "Maksat"') # print result

# Example #3
cursor.execute('SELECT * FROM db WHERE age > 15') # Select *(all) data from db table where age > 15
print_res(additional_text='Select *(all) data from db table where age > 15') # print result

# Example #4
cursor.execute('SELECT name, surname FROM db WHERE age > 15') # Select variables name & surname from db table where age > 15
print_res(additional_text='Select variables name & surname from db table where age > 15') # print result

# Example #5
cursor.execute('SELECT * from db WHERE (name, surname) = (?, ?)', ("Maksat", "Kantai")) #  Select *(all) data from db table where name = "Maksat", surname = "Kantai"
print_res(additional_text='Select *(all) data from db table where name = "Maksat", surname = "Kantai"') # print result

# Example #6
cursor.execute('SELECT name from db') # Select all variables named name from db table
print_res(additional_text='Select all variables named name from db table') # print result

# Example #7
cursor.execute('SELECT name from db WHERE surname = ?', ("Kantai", )) # Select all variables named name from db table where surname = "Kantai"
print_res(additional_text='Select all variables named name from db table where surname = "Kantai"') # print result

# Example #8
cursor.execute('SELECT name, age from db WHERE (surname, age) = (?, ?)', ("Kantai", 16)) # Select all variables named name & age from db table where surname = "Kantai", age = 16
print_res(additional_text='Select all variables named name & age from db table where surname = "Kantai", age = 16') # print result

# Example #9
items = 'name, surname' # 'name'
cursor.execute('SELECT {items} FROM db WHERE id = ?'.format(items=items), (1, )) # Select all variables named name & surname from db table where id = 1
print_res(additional_text='Select all variables named name & surname from db table where id = 1') # print result

# Example #10 (fetchone, fetchmany)
cursor.execute("SELECT * FROM db") # Select *(all) data from db
data1 = cursor.fetchone() # fetch one data from all selected data
print("data1", data1) # (1, 'Unknown', 'Kantai', 16)
data2 = cursor.fetchone() # fetch one data from remaining selected data (1 data fetched, remaining 9 selected data)
print("data2", data2) # (2, 'Maksat', None, None)
data3 = cursor.fetchmany(2) # fetch 2 data from remaining selected data (2 data fetched, remaining 8 selected data)
[print("data3", row) for row in data3] # (3, None, 'Kantai', None) \n (4, 'Maksat', None, None)
data4 = cursor.fetchmany(2) # fetch 2 data from remaining selected data (4 data fetched, remaining 6 selected data)
[print("data4", row) for row in data4] # (5, None, 'Kantai', None) \n (6, 'Maksat', 'Kantai', None)
data5 = cursor.fetchone() # fetch one data from remaining selected data (6 data fetched, remaining 4 selected data)
print("data5", data5) # (7, 'Sayat', 'Afeiev', 16)
data6 = cursor.fetchone() # fetch one data from remaining selected data (7 data fetched, remaining 3 selected data)
print("data6", data6) # (8, 'Zhasiya', 'Serikkyzy', 15)
data7 = cursor.fetchmany(3) # fetch one data from remaining selected data (8 data fetched, remaining 2 selected data)
print("data7", data7) # [(9, 'Batyrbek', 'Orazymbetov', 51), (10, 'Akmaral', 'Pernesheva', 47)]
data8 = cursor.fetchone() # all selected data fetched, no selected data left
print(data8) # None
print("\n\n\n")

# Example #11 (fetchall*2)
cursor.execute("SELECT * FROM db") # Select *(all) data from db
print_res(additional_text='Fetchall*2') # print result
print_res(additional_text='Fetchall*2') # printed "[]"

# Example #12 (select all with rowid)
cursor.execute("SELECT rowid, * FROM db") # Select *(all) data from db with row id
data9 = cursor.fetchmany(3) # fetch 3 data from all selected data
[print(row) for row in data9] # (1, 1, 'Unknown', 'Kantai', 16) \n (2, 2, 'Maksat', None, None) \n (3, 3, None, 'Kantai', None)
print("\n\n\n")
cursor.fetchall() # fetch all selected data

# Example #13 (LIKE command)
# команда LIKE используется при поиске частичных фраз. В нашем случае, мы искали по всей таблице фамили, которые имена начинаются с "Maks". Знак процента (%) является подстановочным оператором.
cursor.execute("SELECT surname FROM db WHERE name LIKE 'Maks%'") 
data10 = cursor.fetchall() # fetch all selected data
[print(row) for row in data10] # (None,) \n (None,) \n ('Kantai',)
print("\n\n\n")

cursor.close() # Close cursor
conn.close() # Close connection



input("Continue? (y/n)\n")



# Update data in db table
conn = sqlite3.connect("db_file.db") # connection with db file
cursor = conn.cursor() # cursor for execute something (для SQL запроса)

# Example #1
cursor.execute('UPDATE db SET age = 99 WHERE name = "Maksat"') # update variable 'age' to 99 where variable 'name' = "Maksat"
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text="update variable 'age' to 99 where variable 'name' = 'Maksat'") # print result
input("Continue? (y/n)\n")

# Example #2
item = "surname"
cursor.execute('UPDATE db SET {item} = ? WHERE name = ?'.format(item=item), ("KANTAI", "Maksat")) # update [item] = 'surname' to "KANTAI" where variable 'name' = 'Maksat'
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text="update [item] = 'surname' to 'KANTAI' where variable 'name' = 'Maksat'") # print result
input("Continue? (y/n)\n")

# Example #3
cursor.execute('UPDATE db SET age = ? WHERE (surname, name) = (?, ?)', (100, "KANTAI", "Maksat")) # update variable 'age' to 100 where variables surname = "KANTAI" & name = "Maksat"
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text='update variable "age" to 100 where variables surname = "KANTAI" & name = "Maksat"') # print result
input("Continue? (y/n)\n")

# Example #4
cursor.execute('UPDATE db SET name = "Unknown", age = 0') # Update all variables named 'name', 'age' to "Unknown", 0 in db table
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text='Update all variables named "name", "age" to "Unknown", 0 in db table') # print result
input("Continue? (y/n)\n")

# Example #5
cursor.execute('UPDATE db SET (name, surname , age) = ("Maksat", "Kantai", 17)') # Update all variables named 'name', 'surname', 'age' to "Maksat", "Kantai", 17 in db table
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text='Update all variables named "name", "surname", "age" to "Maksat", "Kantai", 17 in db table') # print result
input("Continue? (y/n)\n")

# Example #6
cursor.execute('UPDATE db SET (name, surname , age) = ("MAKSAT", "KANTAI", 18) WHERE (name, surname, age) = ("Maksat", "Kantai", 17)') # Update all variables named 'name', 'surname', 'age' to "MAKSAT", "KANTAI", 18 where variables named 'name', 'surname', 'age' equals "Maksat", "Kantai", 17
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text='Update all variables named \'name\', \'surname\', \'age\' to "MAKSAT", "KANTAI", 18 where variables named \'name\', \'surname\', \'age\' equals "Maksat", "Kantai", 17') # print result
input("Continue? (y/n)\n")

# Just
cursor.execute('UPDATE db SET age = 100 WHERE id = 1')
cursor.execute('UPDATE db SET name = "Unknown" WHERE id = 2')
cursor.execute('UPDATE db SET (name, surname, age) = ("Maks", "Kantai", 17) WHERE id = 3')
cursor.execute('UPDATE db SET (name, surname, age) = ("M", "K", 1) WHERE id = 4')
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text='Just') # print result

cursor.close() # Close cursor
conn.close() # Close connection



input("Continue? (y/n)\n")



# Delete data from db table
conn = sqlite3.connect("db_file.db") # connection with db file
cursor = conn.cursor() # cursor for execute something (для SQL запроса)

# Example #1
cursor.execute('DELETE FROM db WHERE age = 100') # delete row from db where age = 100
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text='delete row from db where age = 100') # print result
input("Continue? (y/n)\n")

# Example #2
cursor.execute('DELETE from db where name = ?', ("Unknown", )) # delete row from db where name = "Unknown"
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text='delete row from db where name = "Unknown"') # print result
input("Continue? (y/n)\n")

# Example #3
cursor.execute('DELETE from db where (name, surname, age) = (?, ?, ?)', ("M", "K", 1)) # delete row from db where name = "M" & surname = "K" & age = 1
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text='delete row from db where name = "M" & surname = "K" & age = 1') # print result
input("Continue? (y/n)\n")

# Example #4
cursor.execute('DELETE FROM db') # delete all row from db
conn.commit() # commit(*совершить) / save change(*сохранить изменения)
cursor.execute('SELECT * FROM db') # Select *(all) data from db table
print_res(additional_text='delete all row from db') # print result

cursor.close() # Close cursor
conn.close() # Close connection



input("Continue? (y/n)\n")



# SQLite3 datetime
from datetime import datetime # import class datetime from module datetime for works with date and time
conn = sqlite3.connect("db_file.db") # connection with db file
cursor = conn.cursor() # cursor for execute something (для SQL запроса)

cursor.execute("DROP TABLE IF EXISTS db") # Drop database tabel
cursor.execute('''CREATE TABLE IF NOT EXISTS db(id INTEGER PRIMARY KEY, name TEXT, joining_date timestamp)''') # Create database table

cursor.execute('INSERT INTO db VALUES(?, ?, ?)', (1, "Maks", datetime.now())) # Inserting variables to db table
conn.commit() # save change

cursor.execute('SELECT * FROM db') # Select *(all) data from db
data = cursor.fetchall() # fetch all selected data
[print(item) for item in data[0]] # print result

cursor.close() # Close cursor
conn.close() # Close connection



input("Continue? (y/n)\n")



# SQLite3 datatype BLOB (*for images)

# Drop and re-create database table
conn = sqlite3.connect("db_file.db") # connection with db file
cursor = conn.cursor() # cursor for execute something (для SQL запроса)

cursor.execute("DROP TABLE IF EXISTS db") # Drop db tabel if exists
cursor.execute('''CREATE TABLE IF NOT EXISTS db(id INTEGER PRIMARY KEY, img BLOB)''') # Create database table

# Save image 'test1.png' to db
with open("test1.png", 'rb') as img:
  cursor.execute("INSERT INTO db (img) VALUES(?)", (img.read(),)) # Insert variable to db
  conn.commit() # commit(*совершить) / save change(*сохранить изменения)

# Get image from db and save with name 'test2.png'
cursor.execute("SELECT img FROM db WHERE id = 1") # Select image from db where id = 1
data = cursor.fetchone() # fetch one selected data

with open('test2.png', 'wb') as img:
  img.write(data[0])

cursor.close() # Close cursor
conn.close() # Close connection



# THE END

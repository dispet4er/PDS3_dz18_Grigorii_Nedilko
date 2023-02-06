import sqlite3
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Borntorun4569",
    database = "my_first_db"
)

# mycursor = mydb.cursor()
# sql = "CREATE DATABASE my_first_db"
# mycursor.execute(sql)

# mycursor = mydb.cursor()
# sql = "CREATE TABLE student (id int, name varchar(255))"
# mycursor.execute(sql)

# mycursor = mydb.cursor()
# sql = "CREATE TABLE employee (id int auto_increment PRIMARY KEY, name varchar(255), salary int(6))"
# mycursor.execute(sql)

# mycursor = mydb.cursor()
# sql = "ALTER TABLE student ADD PRIMARY KEY (id)"
# mycursor.execute(sql)

# mycursor = mydb.cursor()
# sql = "INSERT INTO student (id, name) VALUES (01, 'John')"
# mycursor.execute(sql)

mycursor = mydb.cursor()
sql = "INSERT INTO employee (id, name, salary) VALUES (01, 'John', 10000)"
mycursor.execute(sql)

mydb.commit()
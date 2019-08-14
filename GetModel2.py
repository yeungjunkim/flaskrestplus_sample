#!/usr/bin/python
import MySQLdb

encoding = "utf-8" 

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                        user="testuser",         # your username
                        passwd="testpassword",  # your password
                        db="model_storage",        # name of the data base
					    charset='utf8',
   		    		    use_unicode=True)
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM model_list")

# print all the first cell of all the rows
for row in cur.fetchall():
       print("BIGINT = ", row[0], )
       print("FILE_NAME = ", row[1])
       print("MODEL_NAME  = ", row[2])
       print("MODEL_VERSION  = ", row[3], "\n")
       print("CREATE_DATE  = ", row[4])
       print("MODEL_DESC  = ", row[5], "\n")
       print("ARGS_DESC  = ", row[6], "\n")

db.close()
from __future__ import print_function
#---------------------------------------------------------------------#
#Author: Megan Zimmerman
#Program: MySQL Query Runner
#Date: 10/15/16
#Description: Using the mysql.connector library this code takes in 
# a name of a database and a string of a query as command line
# arguments and then prints out the results of the query on that
# database if a database is not given then it prints out the databases 
# available, if a database is given and a query is not given, it 
# prints out the tables in that database. 
#
# To run on local machines:
# 	replace credentials in connection command on line 50
#	have MySQL server running
#	use run command with desired query and database name
#
# run command:
# 	python accessDb.py <databaseName> "<query>"
#
#---------------------------------------------------------------------#
import mysql.connector
import sys


#---------------------------String Formating Functions---------------------------------#

def formatTable(tableStr):
	mystring = ""
	mystring = (("{}".format(tableStr)).replace('(u\'','')).replace('\',)','')
	return mystring

def formatValues(valueStr):
	mystring = ("{}".format(valueStr)).replace('(','').replace(',',' ').replace(')','')
	return mystring

#--------------------------------------------------------------------------------------#



#Not going to return an error if they don't give me an argument, 
# but instead will just look at the tables in mysql default folder
# if an argument is given, it will attempt to look at that db
referenceDb = 'mysql'
if len(sys.argv)>1:
	referenceDb = sys.argv[1]


#Establishing connection to database and cursor

# REPLACE CREDENTIALS HERE
cnct = mysql.connector.connect(user='myusername', password='mypassword', host='localhost', database=referenceDb)
cursor = cnct.cursor()

#Getting the query to use on the database
if len(sys.argv)>2:
	query = sys.argv[2]
elif len(sys.argv)>1:
	query = ("SHOW TABLES")
else:
	query = ("SHOW DATABASES")


#Executes the query on the given database
cursor.execute(query)

#A list to hold the names of all of the values in what query returned
inResult = []

#Formating the output of the query into readible strings
if query == "SHOW TABLES" or query == "SHOW DATABASES":
	for value in cursor:
		inResult.append(formatTable(value))
else:
	for value in cursor:
		inResult.append(formatValues(value))


#outputing
print('The query '+query+' on '+referenceDb+' returned the following:')
opstring = ""
queryList = query.split()
if len(queryList) >2:

	opstring = queryList[1]+' '+queryList[2]+' '+queryList[3]
else:
	opstring = query

#formating for header
print ('-------',end='')
print ('-'*len(opstring), end='')
print('-------')

print('       '+opstring+'    ') 

print ('-------',end='')
print ('-'*len(opstring), end='')
print('-------')

#printing results
for result in inResult:
	print(' ',end='')
	print(result)

#Closing connection to cursor, then closing connection to db
cursor.close()
cnct.close()

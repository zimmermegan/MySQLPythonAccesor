# MySQLPythonAccesor
A small python script for accessing your SQL databases without having to log in when you're being lazy

# Description:
Using the mysql.connector library this code takes in  a name of a database and a string of a query as command line arguments and then prints out the results of the query on that database if a database is not given then it prints out the databases available, if a database is given and a query is not given, it prints out the tables in that database. 

# Running instructions:
  -Download python connector for mysql here https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html <br>
  -Replace credentials in connection command on line 50<br>
  -have MySQL server running<br>
  -use the following run command with desired database name and query<br>

# Command
  python accessDb.py \<databaseName> "\<query>"

# Example Usage 
<b>Giving database and query</b>

python accessDb.py classicmodels "SELECT COUNT(*) FROM customers"
 
The query SELECT COUNT(*) FROM customers on classicmodels returned the following:

\------------------------------------- <br>
       COUNT(*) FROM customers    
\------------------------------------- <br>
 122 



<b> Giving database without a query </b>

python accessDb.py classicmodels 

The query SHOW TABLES on classicmodels returned the following:

\------------------------- <br>
       SHOW TABLES    
\------------------------- <br>
customers<br>
employees<br>
offices<br>
orderdetails<br>
orders<br>
payments<br>
productlines<br>
products<br>


<b> Not giving database or query </b>

python accessDb.py 

The query SHOW DATABASES on mysql returned the following:

\---------------------------- <br>
       SHOW DATABASES    
\---------------------------- <br>
 information_schema<br>
 classicmodels<br>
 mysql<br>
 performance_schema<br>
 sys<br>

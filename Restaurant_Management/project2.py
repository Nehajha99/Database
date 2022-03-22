import mysql.connector

# connrcting
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Nehajha$00",
database = "Restaurant_management")


myacces = mydb.cursor()
# myacces.execute("CREATE DATABASE Restaurant_management")
# myacces.execute("show databases")
# for database in myacces:
#     print(database)



# myacces.execute("create table Restaurant_item (List_of_food varchar(100), Beverage varchar(100))")
# myacces.execute("desc Restaurant_item")
# myacces.execute("SHOW TABLES")
# for table in myacces:
#     print(table)




# sql  = "INSERT INTO Restaurant_item (List_of_food, Beverage) VALUES(%s ,%s)"
# val = [
#     ("Tomato sauce","Water"),
#     ("Meat and Seafood","Tea"),
#     ("Pasta and Rice","Coffee"),
#     ("Sweet Potatoes","Sparkling drinks"),
#     ("Beans and Lentils"," Juices"),
#     ("pizza","Energy drink"),
#     ("fish and chips","Mocktails"),
#     ("sandwiches","Milkshakes") 
#     ]
# myacces.executemany(sql,val)
# mydb.commit()


### select quary
# myacces.execute("SELECT * FROM Restaurant_item")
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)



### Where filter
# sql = "SELECT * FROM Restaurant_item WHERE  List_of_food = 'fish and chips'"
# myacces.execute(sql)
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)



#### Like filter
# sql = "SELECT * FROM Restaurant_item WHERE List_of_food Like 'S%'"
# myacces.execute(sql)
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)



##### Sort ascending order
# sql = "SELECT * FROM Restaurant_item ORDER BY List_of_food"
# myacces.execute(sql)
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)



##### Sort descending order
# sql = "SELECT * FROM Restaurant_item ORDER BY List_of_food DESC"
# myacces.execute(sql)
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)




#### delete items
# sql = "DELETE FROM Restaurant_item WHERE List_of_food = 'fish and chips'"
# myacces.execute(sql)
# mydb.commit()
# myacces.execute("SELECT * FROM Restaurant_item")
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)




##### update
# sql = "UPDATE Restaurant_item SET Beverage = 'Coffee' WHERE Beverage = 'water'"
# myacces.execute(sql)
# mydb.commit()
# myacces.execute("SELECT * FROM Restaurant_item")
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)





#### Limit
# myacces.execute("SELECT * FROM Restaurant_item LIMIT 5")
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)



















    

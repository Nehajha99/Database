import mysql.connector

#### Salary table
# Employee_code = int(input("enter the code"))
# Employee_name = input("enter the name : ")
# Attendance = input("enter A for Absent and P for present :")
# Leave_Taken = int(input("enter no. of leaves :"))
# Basic_salary = int(input(" enter the basic salary :"))
# DA = int(input("Enter the DA amount :"))
# PF = int(input("Enter the PF amount : "))
# Gross_Salary = Basic_salary+DA+PF
# EPF = int(input("Enter the EPF amount: "))
# Leave_CutOut = Leave_Taken *100
# Net_Salar = Gross_Salary-EPF-Leave_CutOut



#### personal information table
# Employee_code = int(input("Enter the emp id:  "))
# Emp_address = input("Enter the address:  ")
# Emp_number = input("Enter the phone number:  ")
# blood_group = input("Enter the blood Group:  ")
# Marital_status = input("Enter status:  ")


#### set connection 
mydb = mysql.connector.connect(host="localhost",
user="root",
password="Nehajha$00",
database = "Payroll_management_system")

myacces = mydb.cursor()



### show Databases
# myacces.execute("CREATE DATABASE Payroll_management_system") # for create
# myacces.execute("show databases")
# for i in myacces:
#     print(i)



#### Data Create table (salary table)
# myacces.execute("CREATE TABLE  Data (Employee_Code integer, Employee_name varchar(50), Attendance varchar(50), Leave_Taken integer, Basic_salary integer, DA integer, PF integer, Gross_Salary integer, EPF integer, Leave_CutOut integer, Net_Salar integer )")
# myacces.execute("desc Data") # show description
# myacces.execute("SHOW TABLES")
# for i in myacces:
#     print(i)




##### Data insert in table
# sql = "INSERT INTO Data (Employee_code, Employee_name, Attendance,Leave_Taken,Basic_salary,DA, PF,Gross_Salary, EPF, Leave_CutOut, Net_Salar ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# var = (Employee_code, Employee_name, Attendance,Leave_Taken,Basic_salary,DA, PF,Gross_Salary, EPF, Leave_CutOut, Net_Salar)
# myacces.execute(sql, var)
# mydb.commit()
# mydb.close()



##### Personal information table
# myacces.execute("CREATE TABLE Personal_data(Employee_Code integer, Emp_address varchar(50), Emp_number varchar(50), blood_group varchar(50), Marital_status varchar(50))")


#### insert data in Personal table
# sql = "INSERT INTO Personal_data (Employee_code, Emp_address, Emp_number,blood_group,Marital_status) VALUES (%s, %s,%s,%s,%s)"
# var = (Employee_code, Emp_address, Emp_number,blood_group,Marital_status)
# myacces.execute(sql, var)
# mydb.commit()


#### select
# myacces.execute("SELECT * FROM Personal_data")
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)




#### Select For see all row
# myacces.execute("SELECT * FROM Data")
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)



### Delete
# sql = "DELETE FROM Data WHERE Employee_name = '23'"
# myacces.execute(sql)
# mydb.commit()
# myacces.execute("SELECT * FROM Data")
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)




#####  where (filter)
# sql = "SELECT * FROM Data WHERE  Employee_name = 'eha' or  Employee_name = 'ishu'"
# myacces.execute(sql)
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)



### like
# sql = "SELECT * FROM Data WHERE Employee_name LIKE '%u'"
# myacces.execute(sql)
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)


#### sorting ascending order
# sql = "SELECT * FROM Data ORDER BY Employee_code"
# myacces.execute(sql)
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)



#### update
# sql = "UPDATE Personal_data  SET  Emp_address = 'Gurugram' WHERE Emp_address = 'rani bagh'"
# myacces.execute(sql)
# mydb.commit()
# myacces.execute("SELECT * FROM Personal_data")
# myresult = myacces.fetchall()
# for x in myresult:
#   print(x)



#### max Gross_Salary
# myacces.execute("SELECT MAX(Gross_Salary) AS Largst FROM Data")
# myresult = myacces.fetchall()
# print(myresult)


##### Join
# myacces.execute("select Data.Employee_name,Personal_data.Emp_address,Personal_data.Emp_number,Personal_data.Marital_status,Personal_data.blood_group,Data.Leave_Taken,Data.Gross_Salary,Data.Net_Salar from Data join Personal_data on Data.Employee_Code=Personal_data.Employee_Code;")
# myresult = myacces.fetchall()
# print(myresult)





# ETL oprations
#Creating DataFrame by using Python lists and Arrays

import pandas as pd
import numpy as np
names=['Yash','Pavan','koti','Sudheer','Aadhi','Modi','Kohli','Sachin','Dhoni','Virat']
marks=[35,36,37,38,40,29,70,65,50,45]
fee=np.array([1000,1500,2000,2500,3000,3500,4000,4500,5000,5500])
course=np.array(['Python','Django','Flask','UI','Oracle','Java','HTML','CSS','AWS','Power BI'])
location=np.array(['Guntur','Vij','Vizag','kadapa','Kakinada','Gujarath','Pune','Hyd','Chennai','Bang'])
emps={'EmpNames':names,'EmpMarks':marks,'EmpFees':fee,'EmpCourses':course,'EmpLocations':location}
sDF1=pd.DataFrame(data=emps)
print(sDF1)

#Creating DataFrame by using MYSQL database

import pymysql
import pandas as pd
connection=pymysql.connect(host='localhost',user='root',password='root',db='pandasdb1',charset='utf8')
c=connection.cursor()
c.execute('select * from Employees1')
data=c.fetchall()
names=[]
marks=[]
fee=[]
course=[]
location=[]
for i in data:
    names.append(i[0])
    marks.append(i[1])
    fee.append(i[2])
    course.append(i[3])
    location.append(i[4])
emps={'EmpNames':names,'EmpMarks':marks,'EmpFees':fee,'EmpCourses':course,'EmpLocations':location}
sDF2=pd.DataFrame(emps)
print(sDF2)

#Creating Dataframe by using Text file

import pandas as pd
data=open('filedata2.txt').read().split('\n')
names=[]
marks=[]
fee=[]
course=[]
location=[]
for i in data:
    x=i.split(',')
    names.append(x[0])
    marks.append(x[1])
    fee.append(x[2])
    course.append(x[3])
    location.append(x[4])
emps={'EmpNames':names,'EmpMarks':marks,'EmpFees':fee,'EmpCourses':course,'EmpLocations':location}
sDF3=pd.DataFrame(emps)
print(sDF3)

#Creating DataFrame by using  SQL Server

import pandas as pd
import pyodbc as odbc
connection=odbc.connect('DRIVER={SQL Server}; Server=ARUNA; Database=sqldb')
c=connection.cursor()
c.execute('select * from Emp')
data=c.fetchall()
names=[]
marks=[]
fee=[]
course=[]
location=[]
for i in data:
    names.append(i[0])
    marks.append(i[1])
    fee.append(i[2])
    course.append(i[3])
    location.append(i[4])
emps={'EmpNames':names,'EmpMarks':marks,'EmpFees':fee,'EmpCourses':course,'EmpLocations':location}
sDF4=pd.DataFrame(emps)
print(sDF4)

#Creating DataFrame from excel file

import pandas as pd
data=pd.read_excel(r'C:\Users\ADMIN\Desktop\Sql server\DAsql.xlsx')
sDF5=pd.DataFrame(data)
print(sDF5)
#Trasnforming all databases into one Dataframe

pdList=[sDF1,sDF2,sDF3,sDF4,sDF5]
new_sDF=pd.concat(pdList)
print(new_sDF)

#Craeting DataFrame to table

import pymysql
import pandas as pd
connection=pymysql.connect(host='localhost',user='root',password='root',db='pandasdb1',charset='utf8')
c1=connection.cursor()
for i,j in new_sDF.iterrows():
    c.execute('insert into Employees values(%s, %s, %s, %s, %s)',
              (j['EmpNames'],j['EmpMarks'],j['EmpFees'],j['EmpCourses'],j['EmpLocations']))
connection.commit()





#Required modules in stall before running this project by using "pip install" comand
# 1.pymysql
# 2.pyodbc or odbc
# 3.openpyxl
# 4.pandas
# 5.numpy

# After install done make sure your databases names and table header creation If you have any queriess please contact 8464002165 or sudarsan2165@gmail.com
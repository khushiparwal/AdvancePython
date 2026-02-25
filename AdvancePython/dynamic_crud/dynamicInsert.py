import pymysql

def insert1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    q1 = "insert into employee values(4,'seema','capgemini',80000,'2')"
    cursor.execute(q1)
    connection.commit()
    connection.close()
    print("Data inserted successfully by insert1")

def insert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    q2 = 'insert into employee values(%s ,%s,%s,%s,%s)'
    data = (5,'Diya','HCL',30000,2)
    cursor.execute(q2,data)
    connection.commit()
    connection.close()
    print("Data inserted successfully by insert2")

def insert3(id,name,company,salary,dept_id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    q3 = 'insert into employee values(%s ,%s,%s,%s,%s)'
    data = (id,name,company,salary,dept_id)
    cursor.execute(q3,data)
    connection.commit()
    connection.close()
    print("Data inserted successfully by insert3")

def insert4(data={}):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    id = data['id']
    name = data['name']
    company = data['company']
    salary = data['salary']
    dept_id = data['dept_id']
    q4 = 'insert into employee values(%s ,%s,%s,%s,%s)'
    data = (id,name,company,salary,dept_id)
    cursor.execute(q4,data)
    connection.commit()
    connection.close()
    print("Data inserted successfully by insert4")


#insert1()
#insert2()
#insert3(6,'Ravi','Intel',90000,1)
insert4({'id':9,'name':'Aman','company':'TCS','salary':10000,'dept_id':2})
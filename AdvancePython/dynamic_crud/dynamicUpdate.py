import pymysql

def update1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    q1 = 'update employee set salary = 90000 where id=4'
    cursor.execute(q1)
    connection.commit()
    connection.close()
    print("Data updated successfully by update1")

def update2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    q2 = "update employee set name = %s where id = %s"
    data = ('Ravi', 1)
    cursor.execute(q2, data)
    connection.commit()
    connection.close()
    print('data updated successfully by update2')

def update3(name,id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    q3 = "update employee set name = %s where id = %s"
    data = (name,id)
    cursor.execute(q3, data)
    connection.commit()
    connection.close()
    print('data updated successfully by update3')

def update4(data):
    name = data['name']
    salary = data['salary']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    q4 = "update employee set salary = %s where name = %s"
    data = (salary,name)
    cursor.execute(q4, data)
    connection.commit()
    connection.close()
    print('data updated successfully by update4')

update1()
update2()
update3('sangeeta',6)

params={}
params['name'] = 'sangeeta'
params['salary'] = 56000
update4(params)

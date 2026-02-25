import pymysql

def delete1():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    q1 = 'delete from employee where id=6'
    cursor.execute(q1)
    connection.commit()
    connection.close()
    print("Data deleted successfully by delete1")

def delete2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    q2 = 'delete from employee where id=%s'
    data = (9,)
    cursor.execute(q2,data)
    connection.commit()
    connection.close()
    print("Data deleted successfully by delete2")

def delete3(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
    cursor = connection.cursor()
    q3 = 'delete from employee where id=%s'
    data = (id,)
    cursor.execute(q3,data)
    connection.commit()
    connection.close()
    print("Data deleted successfully by delete3")

delete1()
delete2()
delete3(5)




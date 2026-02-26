import pymysql
def read1():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    q1 = 'select * from store'
    cursor.execute(q1)
    result = cursor.fetchall()
    print(result,'\n')
    for data in result:
        print(data)
    connection.commit()
    connection.close()
    print("data printed successfully")

def read2():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    q1 = 'select * from store'
    column_name=('id','item_name','price')
    cursor.execute(q1)
    result = cursor.fetchall()
    for data in result:
        print(data)
        print({column_name[i]: data[i] for i,_ in enumerate(data)})
    connection.commit()
    connection.close()
    print("data printed successfully")

def read3():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    #q1 = 'select * from store'
    q1 = 'select * from store where id=10'
    #q1 = 'select * from store where item_name='hat''
    #q1 = 'select * from store where price = 6000'
    cursor.execute(q1)
    result = cursor.fetchall()
    for data in result:
        print(data[0],'\t',data[1],'\t',data[2])
    connection.commit()
    connection.close()
    print("data printed successfully")

def read4(id,item_name,price):
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    q1 = 'select * from store '
    if id!= 0:
        q1 += "where id = "+str(id)
    if item_name !='':
        q1 += "where item_name like '"+item_name+"%'"
    if price != 0:
        q1 += "where price = "+str(price)
    cursor.execute(q1)
    result = cursor.fetchall()
    for data in result:
        print(data[0],'\t',data[1],'\t',data[2])
    connection.commit()
    connection.close()
    print("data printed successfully")

def read5(params={}):
    id = params.get('id',0)
    item_name = params.get('item_name','')
    price = params.get('price',0)
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    q1 = 'select * from store where 1=1 '
    if id!= 0:
        q1 += "and id = "+str(id)
    if item_name !='':
        q1 += "and item_name like '"+item_name+"%'"
    if price != 0:
        q1 += "and price = "+str(price)
    cursor.execute(q1)
    result = cursor.fetchall()
    for data in result:
        print(data[0],'\t',data[1],'\t',data[2])
    connection.commit()
    connection.close()
    print("data printed successfully")

def read6(params={}):
    id = params.get('id',0)
    item_name = params.get('item_name','')
    price = params.get('price',0)
    pageNo = params.get('pageNo',0)
    pageSize = params.get('pageSize',0)
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    q1 = 'select * from store where 1=1 '
    if id!= 0:
        q1 += "and id = "+str(id)
    if item_name !='':
        q1 += "and item_name like '"+item_name+"%'"
    if price != 0:
        q1 += "and price = "+str(price)
    if pageSize>0:
        offset = (pageNo-1)*pageSize
        q1 += "LIMIT "+str(offset)+","+str(pageSize)
    cursor.execute(q1)
    result = cursor.fetchall()
    for data in result:
        print(data[0],'\t',data[1],'\t',data[2])
    connection.commit()
    connection.close()
    print("data printed successfully")


#read1()
#read2()
#read3()
#read4(1,'',0)
params={'name':'e','pageNo':3,'pageSize':2}
#read5(params)
read6(params)

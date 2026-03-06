import pymysql

def employeein():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    cursor.callproc('employeein',[2])
    result = cursor.fetchall()
    for row in result:
        print(row)
    connection.close()

def employeeout():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    cursor.execute('call employeeout(@output)')
    cursor.execute('select @output')
    result = cursor.fetchall()
    print(result[0][0])
    connection.close()

def employeeinout():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    cursor.execute('set @input_output=1')
    cursor.execute('call employeeinout(@input_output)')
    cursor.execute('select @input_output')
    result = cursor.fetchall()
    print(result[0])
    connection.close()

employeein()
employeeout()
employeeinout()

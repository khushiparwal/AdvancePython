import pymysql
def testfunction():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
    cursor = connection.cursor()
    cursor.execute('select square(9)')
    result = cursor.fetchall()
    print(result[0][0])
    connection.close()

testfunction()
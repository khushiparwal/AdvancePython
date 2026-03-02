import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
try:
    connection.autocommit(False)
    q1 = 'insert into marksheet(107,"Ram",78,82,41)'
    q2 = 'insert into marksheet(108,"Manan",78,82,41)'
    q3 = 'insert into marksheet(107,"Ram",78,82,41)'
    cursor = connection.cursor()
    cursor.execute(q1)
    cursor.execute(q2)
    cursor.execute(q3)
    connection.commit()
    print("Data inserted successfully")
except Exception as e:
    print("Error occurred while inserting data: ",e)

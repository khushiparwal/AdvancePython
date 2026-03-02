import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays',autocommit=False)
cursor = connection.cursor()
try:
    print("Starting transaction")
    cursor.execute("insert into marksheet values(107,'Ram',78,95,41)")
    print("Creating savepoint sp1")
    cursor.execute("savepoint sp1")
    try:
        cursor.execute("insert into marksheet values(107,'Ram',78,95,41)")
        print("Creating savepoint sp2")
        cursor.execute("savepoint sp2")
    except Exception as e:
        print("Error occurred while inserting second record: ",e)
        print("rolling back to first record")
        cursor.execute("rollback to savepoint sp1")
    connection.commit()
    print("transaction committed")
except Exception as e:
    print("Error in transaction: ",e)
    connection.rollback()
finally:
    cursor.close()
    connection.close()

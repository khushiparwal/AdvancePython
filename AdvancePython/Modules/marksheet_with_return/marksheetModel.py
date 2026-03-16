import pymysql
class marksheetModel:
    def nextpk(self):
        pk = 0
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'select max(rollno) from marksheet'
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk+1

    def add(self,data):
        rollno = marksheetModel.nextpk(self)
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'insert into marksheet values(%s,%s,%s,%s,%s)'
        data = (rollno,name,physics,chemistry,maths)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self,data):
        rollno = data['rollno']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'update marksheet set name=%s, physics=%s, chemistry=%s, maths=%s where rollno=%s'
        data = (name,physics,chemistry,maths,rollno)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("data updated successfully")

    def delete(self,rollno):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'delete from marksheet where rollno=%s'
        data=(rollno)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("data deleted successfully")

    def findbyrollno(self,rollno):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'select * from marksheet where rollno=%s'
        data = (rollno)
        cursor.execute(q1, data)
        result = cursor.fetchall()
        columnName = ("id", "rollNo", "name", "physics", "chemistry", "maths")
        res = []
        for data in result:
            #print(data[0],'\t',data[1],'\t',data[2],'\t',data[3],'\t',data[4])
            res.append({columnName[i]:data[i] for i,_ in enumerate(data)})
        connection.commit()
        connection.close()
        return res

    def search(self,data):
        rollno = data.get('rollno',0)
        name = data.get('name','')
        pageNo = data.get('pageNo',0)
        pageSize = data.get('pageSize',0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'select * from marksheet where 1=1'
        if name != '':
            q1 += " and name='"+name+"'"
        if rollno != 0:
            q1 += " and rollno="+str(rollno)
        if pageSize>0:
            offset = (pageNo-1)*pageSize
            q1 += " limit "+str(offset)+","+str(pageSize)
        cursor.execute(q1)
        columnName = ("id", "rollNo", "name", "physics", "chemistry", "maths")
        result = cursor.fetchall()
        res = []
        for data in result:
            #print(data[0],'\t',data[1],'\t',data[2],'\t',data[3],'\t',data[4])
            res.append({columnName[i]: data[i] for i,_ in enumerate(data)})
        connection.commit()
        connection.close()
        return res

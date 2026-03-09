import pymysql

class warehousestaffModel:
    def nextpk(self):
        pk=0
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'select max(staffId) from warehousestaff'
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk+1

    def insert(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        staffId = self.nextpk()
        staffName = data['staffName']
        role = data['role']
        salary = data['salary']
        q1 = 'insert into warehousestaff values(%s,%s,%s,%s)'
        data = (staffId,staffName,role,salary)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print('Data inserted successfully')

    def update(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        staffId = data['staffId']
        staffName = data['staffName']
        role = data['role']
        salary = data['salary']
        q1 = 'update warehousestaff set staffName=%s, role=%s, salary=%s where staffId=%s'
        data = (staffName, role, salary,staffId)
        cursor.execute(q1, data)
        connection.commit()
        connection.close()
        print('Data updated successfully')

    def delete(self,staffId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'delete from warehousestaff where staffId=%s'
        data = staffId
        cursor.execute(q1, data)
        connection.commit()
        connection.close()
        print('Data deleted successfully')

    def search(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        staffId = data.get('staffId',0)
        staffName = data.get('staffName','')
        role = data.get('role','')
        salary = data.get('salary',0)
        pageNo = data.get('pageNo',0)
        pageSize = data.get('pageSize',0)
        q1 = 'select * from warehousestaff where 1=1 '
        if staffId != 0:
            q1 += " and staffId="+str(staffId)
        if staffName != '':
            q1 += " and staffName='"+staffName+"'"
        if role != '':
            q1 += " and role='"+role+"'"
        if salary != 0:
            q1 += " and salary="+str(salary)
        if pageSize>0:
            offset = (pageNo-1)*pageSize
            q1 += " limit "+str(offset)+","+str(pageSize)
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            print(data[0],"\t",data[1],"\t",data[2],"\t",data[3])
        connection.close()








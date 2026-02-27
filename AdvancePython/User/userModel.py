import pymysql
class userModel:
    def nextpk(self):
        pk = 0
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'select max(id) from user'
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk+1

    def add(self,data):
        id = userModel.nextpk(self)
        firstname = data['firstname']
        lastname = data['lastname']
        loginId = data['loginId']
        password = data['password']
        dob = data['dob']
        address = data['address']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'insert into user values(%s,%s,%s,%s,%s,%s,%s)'
        data = (id,firstname,lastname,loginId,password,dob,address)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self,data):
        id = data['id']
        firstname = data['firstname']
        lastname = data['lastname']
        loginId = data['loginId']
        password = data['password']
        dob = data['dob']
        address = data['address']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'update user set firstname=%s, lastname=%s, loginId=%s, password=%s, dob=%s, address=%s where id=%s'
        data = (firstname,lastname,loginId,password,dob,address,id)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("data updated successfully")

    def delete(self,id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'delete from user where id=%s'
        data=(id)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("data deleted successfully")

    def read(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'select * from user '
        cursor.execute(q1)
        result = cursor.fetchall()
        columnname=('id','firstname','lastname','loginId','password','dob','address')
        res = []
        for x in result:
            print({columnname[i] : x[i] for i, _ in enumerate(x)})
            res.append({columnname[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def findbyid(self,id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'select * from user where id=%s'
        data = (id)
        cursor.execute(q1, data)
        result = cursor.fetchall()
        columnname=('id','firstname','lastname','loginId','password','dob','address')
        res = []
        for x in result:
            print({columnname[i] : x[i] for i, _ in enumerate(x)})
            res.append({columnname[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def findbyloginId(self,loginId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'select * from user where loginId=%s'
        data = (loginId)
        cursor.execute(q1, data)
        result = cursor.fetchall()
        columnname=('id','firstname','lastname','loginId','password','dob','address')
        res = []
        for x in result:
            print({columnname[i] : x[i] for i, _ in enumerate(x)})
            res.append({columnname[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def search(self,data):
        firstname = data.get('firstname','')
        dob = data.get('dob',0)
        pageNo = data.get('pageNo',0)
        pageSize = data.get('pageSize',0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'select * from user where 1=1'
        if firstname != '':
            q1 += " and firstname='"+firstname+"'"
        if dob != 0:
            q1 += " and dob="+str(dob)
        if pageSize>0:
            offset = (pageNo-1)*pageSize
            q1 += " limit "+str(offset)+","+str(pageSize)
        cursor.execute(q1)
        result = cursor.fetchall()
        columnname = ('id', 'firstname', 'lastname', 'loginId', 'password', 'dob', 'address')
        res = []
        for x in result:
            print({columnname[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnname[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res




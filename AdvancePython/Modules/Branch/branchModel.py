import pymysql

class branch:
    def nextpk(self):
        pk = 0
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'select max(branchId) from branch'
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk+1

    def insert(self,data):
        branchId = self.nextpk()
        branchCode = data['branchCode']
        branchName = data['branchName']
        branchLocation = data['branchLocation']
        branchStatus = data['branchStatus']
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'insert into branch values(%s,%s,%s,%s,%s)'
        data = (branchId,branchCode,branchName,branchLocation,branchStatus)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self,data):
        branchId = data['branchId']
        branchCode = data['branchCode']
        branchName = data['branchName']
        branchLocation = data['branchLocation']
        branchStatus = data['branchStatus']
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'update branch set branchCode=%s, branchName=%s, branchLocation=%s, branchStatus=%s where branchId=%s'
        data=(branchCode,branchName,branchLocation,branchStatus,branchId)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self,branchId):
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'delete from branch where branchId=%s'
        data = branchId
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def search(self,data):
        branchId = data.get('branchId',0)
        branchCode = data.get('branchCode','')
        branchName = data.get('branchName','')
        branchLocation = data.get('branchLocation','')
        branchStatus = data.get('branchStatus','')
        pageNo = data.get('pageNo',0)
        pageSize = data.get('pageSize',0)
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'select * from branch where 1=1 '
        if branchId != 0:
            q1 += ' and branchId = '+str(branchId)
        if branchCode != '':
            q1 += " and branchCode='"+branchCode+"'"
        if branchName != '':
            q1 += " and branchName like '%"+branchName+"%'"
        if branchLocation != '':
            q1 += " and branchLocation='"+branchLocation+"'"
        if branchStatus != '':
            q1 += " and branchStatus='"+branchStatus+"'"
        if pageSize>0:
            offset = (pageNo-1)*pageSize
            q1 += ' limit '+str(offset)+","+str(pageSize)
        cursor.execute(q1)
        result = cursor.fetchall()
        res = []
        columnName = ('branchId','branchCode','branchName','branchLocation','branchStatus')
        for x in result:
            res.append({columnName[i]:x[i] for i,_ in enumerate(x)})
        connection.commit()
        connection.close()
        return res
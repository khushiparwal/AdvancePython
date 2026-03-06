import pymysql
class medicineModel:
    def nextpk(self):
        pk = 0
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'select max(medicineId) from medicine'
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
        medicineId = self.nextpk()
        medicineName = data['medicineName']
        price = data['price']
        expiryDate = data['expiryDate']
        q1 = 'insert into medicine values(%s,%s,%s,%s)'
        data = (medicineId,medicineName,price,expiryDate)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        medicineId = data['medicineId']
        medicineName = data['medicineName']
        price = data['price']
        expiryDate = data['expiryDate']
        q1 = 'update medicine set medicineName=%s, price=%s, expiryDate=%s where medicineId=%s'
        data = (medicineName, price, expiryDate, medicineId)
        cursor.execute(q1, data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self,medicineId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'delete from medicine where medicineId=%s'
        data = medicineId
        cursor.execute(q1, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def search(self,data):
        medicineId = data.get('medicineId',0)
        medicineName = data.get('medicineName','')
        price = data.get('price',0)
        expiryDate = data.get('expiryDate','')
        pageNo = data.get('pageNo',0)
        pageSize= data.get('pageSize',0)
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'select * from medicine where 1=1 '
        if medicineId != 0:
            q1 += ' and medicineId = '+str(medicineId)
        if medicineName != '':
            q1 += " and medicineName like '%"+medicineName+"%'"
        if price != 0:
            q1 += ' and price = '+str(price)
        if expiryDate != '':
            q1 += ' and expiryDate =  '+str(expiryDate)
        if pageSize >0:
            offset = (pageNo-1)*pageSize
            q1 += ' limit '+str(offset)+','+str(pageSize)
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            print(data[0],"\t",data[1],"\t",data[2],"\t",data[3])
        connection.commit()
        connection.close()




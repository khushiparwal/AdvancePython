import pymysql
from pymysql import connect


class product:
    def nextpk(self):
        pk = 0
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'select max(productId) from product'
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk+1

    def add(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        productId = self.nextpk()
        productCode = data['productCode']
        productName = data['productName']
        price = data['price']
        status = data['status']
        q1 = 'insert into product values(%s,%s,%s,%s,%s)'
        data = (productId,productCode,productName,price,status)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        productId = data['productId']
        productCode = data['productCode']
        productName = data['productName']
        price = data['price']
        status = data['status']
        q1 = 'update product set productCode=%s, productName=%s, price=%s, status=%s where productId = %s'
        data = (productCode,productName,price,status,productId)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self,productId):
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'delete from product where productId=%s'
        data=productId
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def search(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        productId = data.get('productId',0)
        productCode = data.get('productCode','')
        productName = data.get('productName','')
        price = data.get('price',0)
        status = data.get('status','')
        pageNo = data.get('pageNo',0)
        pageSize = data.get('pageSize',0)
        q1 = 'select * from product where 1=1 '
        if productId!=0:
            q1 += ' and productId='+str(productId)
        if productCode != '':
            q1 += " and productCode='"+productCode+"'"
        if productName != '':
            q1 += " and productName like '%"+productName+"%'"
        if price != 0:
            q1 += " and price="+str(price)
        if status != '':
            q1 += " and status='"+status+"'"
        if pageSize>0:
            offset=(pageNo-1)*pageSize
            q1 += " limit "+str(offset)+","+str(pageSize)
        cursor.execute(q1)
        result = cursor.fetchall()
        res = []
        columnName = ('productId','productCode','productName','price','status')
        for x in result:
            res.append({columnName[i]:x[i] for i,_ in enumerate(x)})
        connection.commit()
        connection.close()
        return res

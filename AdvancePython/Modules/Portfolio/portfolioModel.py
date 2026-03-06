import pymysql
class portfolioModel:
    def nextpk(self):
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        q1 = 'select max(portfolioId) from portfolio'
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk+1

    def insert(self,data):
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        portfolioId = self.nextpk()
        portfolioName = data['portfolioName']
        totalValue = data['totalValue']
        createDate = data['createDate']
        q1 = 'insert into portfolio values(%s,%s,%s,%s)'
        data = (portfolioId,portfolioName,totalValue,createDate)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        portfolioId = data['portfolioId']
        portfolioName = data['portfolioName']
        totalValue = data['totalValue']
        createDate = data['createDate']
        q1 = 'update portfolio set portfolioName=%s, totalValue=%s, createDate=%s where portfolioId=%s'
        data = (portfolioName,totalValue,createDate,portfolioId)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self,portfolioId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'delete from portfolio where portfolioId = %s'
        data = portfolioId
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def search(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        portfolioId = data.get('portfolioId',0)
        portfolioName = data.get('portfolioName','')
        totalValue = data.get('totalValue',0)
        createDate = data.get('createDate','')
        pageNo = data.get('pageNo',0)
        pageSize = data.get('pageSize',0)
        q1 = 'select * from portfolio where 1=1 '
        if portfolioId != 0:
            q1 += ' and portfolioId='+str(portfolioId)
        if portfolioName != '':
            q1 += " and portfolioName='"+portfolioName+"'"
        if totalValue != 0:
            q1 += ' and totalValue='+str(totalValue)
        if createDate != '':
            q1 += " and createDate='"+createDate+"'"
        if pageSize > 0:
            offset = (pageNo-1)*pageSize
            q1 += ' limit '+str(offset)+','+str(pageSize)
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            print(data[0],"\t",data[1],"\t",data[2],"\t",data[3])
        connection.commit()
        connection.close()


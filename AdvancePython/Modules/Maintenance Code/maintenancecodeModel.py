import pymysql
class maintenancecodeModel:
    def nextpk(self):
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
        cursor = connection.cursor()
        pk = 0
        q1 = 'select max(maintenanceId) from maintenancecode'
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
        maintenanceId = self.nextpk()
        maintenanceCode = data['maintenanceCode']
        equipmentName = data['equipmentName']
        maintenanceDate = data['maintenanceDate']
        technicianName = data['technicianName']
        maintenanceStatus = data['maintenanceStatus']
        q1 = 'insert into maintenancecode values(%s,%s,%s,%s,%s,%s)'
        data = (maintenanceId,maintenanceCode,equipmentName,maintenanceDate,technicianName,maintenanceStatus)
        cursor.execute(q1,data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        maintenanceId = data['maintenanceId']
        maintenanceCode = data['maintenanceCode']
        equipmentName = data['equipmentName']
        maintenanceDate = data['maintenanceDate']
        technicianName = data['technicianName']
        maintenanceStatus = data['maintenanceStatus']
        q1 = 'update maintenancecode set maintenanceCode=%s, equipmentName=%s, maintenanceDate=%s, technicianName=%s, maintenanceStatus=%s where maintenanceId=%s'
        data = (maintenanceCode, equipmentName, maintenanceDate, technicianName, maintenanceStatus, maintenanceId)
        cursor.execute(q1, data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self,maintenanceId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'delete from maintenancecode where maintenanceId=%s'
        data = maintenanceId
        cursor.execute(q1, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def search(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        maintenanceId = data.get('maintenanceId',0)
        maintenanceCode = data.get('maintenanceCode','')
        equipmentName = data.get('equipmentName','')
        maintenanceDate = data.get('maintenanceDate','')
        technicianName = data.get('technicianName','')
        maintenanceStatus = data.get('maintenanceStatus','')
        pageNo = data.get('pageNo',0)
        pageSize = data.get('pageSize',0)
        q1 = 'select * from maintenancecode where 1=1 '
        if maintenanceId != 0:
            q1 += ' and maintenanceId='+str(maintenanceId)
        if maintenanceCode != '':
            q1 += " and maintenanceCode like '%"+maintenanceCode+"%'"
        if equipmentName != '':
            q1 += " and equipmentName like '%"+equipmentName+"%'"
        if maintenanceDate != '':
            q1 += " and maintenanceDate='"+maintenanceDate+"'"
        if technicianName != '':
            q1 += " and technicianName like '%"+technicianName+"%'"
        if maintenanceStatus != '':
            q1 += " and maintenanceStatus='"+maintenanceStatus+"'"
        if pageSize > 0:
            offset = (pageNo - 1) * pageSize
            q1 += " limit " + str(offset) + "," + str(pageSize)
        cursor.execute(q1)
        result = cursor.fetchall()
        res = []
        columnName = ('maintenanceId','maintenanceCode','equipmentName','maintenanceDate','technicianName','maintenanceStatus')
        for x in result:
            res.append({columnName[i]:x[i] for i,_ in enumerate(x)})
        connection.commit()
        connection.close()
        return res
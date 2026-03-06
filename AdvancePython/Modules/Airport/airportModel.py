import pymysql
class airportModel:
    def nextpk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'select max(airportId) from airport'
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def insert(self,data):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        airportId = airportModel.nextpk(self)
        airportName = data['airportName']
        city = data['city']
        country = data['country']
        q1 = 'insert into airport values(%s,%s,%s,%s)'
        data = (airportId, airportName, city, country)
        cursor = connection.cursor()
        cursor.execute(q1, data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self, data):
        airportId = data['airportId']
        airportName = data['airportName']
        city = data['city']
        country = data['country']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'update airport set airportName=%s, city=%s, country=%s where airportId=%s'
        data = (airportName, city, country, airportId)
        cursor.execute(q1, data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self, airportId):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        cursor = connection.cursor()
        q1 = 'delete from airport where airportId=%s'
        data = airportId
        cursor.execute(q1, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def search(self, data):
        airportId = data.get('airportId', 0)
        airportName = data.get('airportName', '')
        city = data.get('city', '')
        country = data.get('country', '')
        pageNo = data.get('pageNo', 0)
        pageSize = data.get('pageSize', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='rays')
        q1 = 'select * from airport where 1=1 '
        cursor = connection.cursor()
        if airportId != 0:
            q1 += 'and airportId = ' + str(airportId)
        if airportName != '':
            q1 += "and airportName = '" + airportName+"'"
        if city != '':
            q1 += "and city = '" + city+"'"
        if country != '':
            q1 += "and country = '" + country+"'"
        if pageSize > 0:
            offset = (pageNo - 1) * pageSize
            q1 += ' limit ' + str(offset) + ',' + str(pageSize)
        cursor.execute(q1)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
        connection.commit()
        connection.close()



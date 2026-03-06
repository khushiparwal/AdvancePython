from airportModel import airportModel
def testInsert():
    params={}
    params['airportName'] = 'indra gandhi international airport'
    params['city'] = ' new delhi'
    params['country'] = 'india'
    model = airportModel()
    model.insert(params)

def testUpdate():
    params={}
    params['airportId' ] = 2
    params['airportName'] = 'devi ahilyabai international airport'
    params['city'] = ('indore')
    params['country'] = 'india'
    model = airportModel()
    model.update(params)

def testDelete():
    model = airportModel()
    model.delete(2)

def testSearch():
    params={}
    params['country'] = 'india'
    params['pageNo']=2
    params['pageSize'] = 1
    model = airportModel()
    model.search(params)

#testInsert()
#testUpdate()
#testDelete()
testSearch()
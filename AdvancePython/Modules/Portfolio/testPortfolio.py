from portfolioModel import portfolioModel

def testInsert():
    params={}
    params['portfolioName'] = 'crypto portfolio'
    params['totalValue'] = 100000
    params['createDate'] = '2020-03-25'
    model = portfolioModel()
    model.insert(params)

def testUpdate():
    params={}
    params['portfolioId'] = 6
    params['portfolioName'] = 'crypto portfolio'
    params['totalValue'] = 200000
    params['createDate'] = '2020-03-25'
    model = portfolioModel()
    model.update(params)

def testDelete():
    model = portfolioModel()
    model.delete(6)

def testSearch():
    params = {}
    params['portfolioName'] = 'retirement funds'
    params['pageNo'] = 1
    params['pageSize'] = 2
    model = portfolioModel()
    model.search(params)

#testInsert()
#testUpdate()
#testDelete()
testSearch()
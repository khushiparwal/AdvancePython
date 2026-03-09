from warehousestaffModel import warehousestaffModel

def testInsert():
    params={}
    params['staffName']= 'Rohit Patel'
    params['role'] = 'Manager'
    params['salary'] = 60000
    model = warehousestaffModel()
    model.insert(params)
def testUpdate():
    params={}
    params['staffId'] = 6
    params['staffName']='Rohit Sharma'
    params['role'] = 'Manager'
    params['salary'] = 50000
    model = warehousestaffModel()
    model.update(params)

def testDelete():
    model = warehousestaffModel()
    model.delete(6)

def testSearch():
    params={}
    params['salary']=60000
    model=warehousestaffModel()
    model.search(params)

#testInsert()
#testUpdate()
#testDelete()
testSearch()
from medicineModel import medicineModel
def testInsert():
    params = {}
    params['medicineName'] = 'dolo650'
    params['price'] = 40
    params['expiryDate'] = '2026-05-30'
    model = medicineModel()
    model.insert(params)

def testUpdate():
    params = {}
    params['medicineId'] = 3
    params['medicineName'] = 'dolo650'
    params['price'] = 40
    params['expiryDate'] = '2026-05-30'
    model = medicineModel()
    model.update(params)

def testDelete():
    model = medicineModel()
    model.delete(6)

def testSearch():
    params={}
    params['medicineName']='montair'
    model = medicineModel()
    model.search(params)

#testInsert()
#testUpdate()
#testDelete()
testSearch()
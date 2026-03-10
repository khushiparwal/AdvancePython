from maintenancecodeModel import maintenancecodeModel

def testInsert():
    params={}
    params['maintenanceCode']='MC106'
    params['equipmentName']='Forklift'
    params['maintenanceDate']='2026-02-28'
    params['technicianName']='Rajesh Singh'
    params['maintenanceStatus']='pending'
    model = maintenancecodeModel()
    model.insert(params)

def testUpdate():
    params={}
    params['maintenanceId']=6
    params['maintenanceCode'] = 'MC106'
    params['equipmentName'] = 'Forklift'
    params['maintenanceDate'] = '2026-03-28'
    params['technicianName'] = 'Rajesh Singh'
    params['maintenanceStatus'] = 'complete'
    model = maintenancecodeModel()
    model.update(params)

def testDelete():
    model = maintenancecodeModel()
    model.delete(6)

def testSearch():
    params={}
    params['technicianName']='ra'
    params['pageNo']=1
    params['pageSize']=2
    model = maintenancecodeModel()
    list = model.search(params)
    for data in list:
        print(data['maintenanceId'],'\t',data['maintenanceCode'],'\t',data['equipmentName'],'\t',
              data['maintenanceDate'],'\t',data['technicianName'],'\t',data['maintenanceStatus'])

#testInsert()
#testUpdate()
#testDelete()
testSearch()





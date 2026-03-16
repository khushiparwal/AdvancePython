from marksheetModel import marksheetModel
def testAdd():
    params={}
    params['name']='Naman'
    params['physics']=76
    params['chemistry']=61
    params['maths']=90
    model = marksheetModel()
    model.add(params)

def testUpdate():
    params={}
    params['rollno']=105
    params['name'] = 'Rohan'
    params['physics'] = 72
    params['chemistry'] = 81
    params['maths'] = 58
    model = marksheetModel()
    model.update(params)

def testDelete():
    model = marksheetModel()
    model.delete(101)

def testfindbyrollno():
    model = marksheetModel()
    list = model.findbyrollno(103)
    for data in list:
        print(data['rollno'],'\t',data['name'],'\t',data['physics'],'\t',data['maths'],'\t',data['chemistry'])

def testsearch():
    params={}
    #params['rollno'] = 102
    #params['name'] = 'Shyam'
    params['pageNo']=2
    params['pageSize']=2
    model = marksheetModel()
    list = model.search(params)
    for data in list:
        print(data['rollno'], '\t', data['name'], '\t', data['physics'], '\t',data['chemistry'],'\t', data['maths'])


#testAdd()
#testUpdate()
#testDelete()
#testfindbyrollno()
testsearch()
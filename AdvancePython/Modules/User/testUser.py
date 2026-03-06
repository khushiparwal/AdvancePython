from userModel import userModel

def testadd():
    params={}
    params['firstname']='Hiya'
    params['lastname']='Kapoor'
    params['loginId']=105
    params['password']='hiya'
    params['dob']=['2003-03-26']
    params['address']='Indore'
    model = userModel()
    model.add(params)

def testupdate():
    params={}
    params['id']=105
    params['firstname'] = 'Hiya'
    params['lastname'] = 'Kapoor'
    params['loginId'] = 105
    params['password'] = 'hiya'
    params['dob'] = ['2003-03-26']
    params['address'] = 'Gurgaon'
    model = userModel()
    model.update(params)

def testdelete():
    model = userModel()
    model.delete(6)

def testread():
    model = userModel()
    model.read()

def testfindbyid():
    model = userModel()
    model.findbyid(2)

def testfindbyloginid():
    model = userModel()
    model.findbyloginId(103)

def testsearch():
    params={}
    params['pageNo']=2
    params['pageSize']=2
    model = userModel()
    model.search(params)

#testadd()
#testupdate()
#testdelete()
#testread()
#testfindbyid()
#testfindbyloginid()
testsearch()
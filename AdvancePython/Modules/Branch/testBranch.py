from branchModel import branch

def testinsert():
    params = {}
    params['branchCode'] = 'BR006'
    params['branchName'] = 'Southeast Region Branch'
    params['branchLocation'] = 'Hyderabad'
    params['branchStatus'] = 'Inactive'
    model = branch()
    model.insert(params)

def testupdate():
    params = {}
    params['branchId'] = 6
    params['branchCode'] = 'BR006'
    params['branchName'] = 'Southeast Region Branch'
    params['branchLocation'] = 'Hyderabad'
    params['branchStatus'] = 'Active'
    model = branch()
    model.update(params)

def testdelete():
    model = branch()
    model.delete(6)
def testsearch():
    params={}
    params['branchName'] = 'th'
    model = branch()
    list = model.search(params)
    for data in list:
        print(data['branchId'],'\t',data['branchCode'],'\t',data['branchName'],'\t',data['branchLocation'],'\t',
              data['branchStatus'])

#testinsert()
#testupdate()
#testdelete()
testsearch()

from productModel import product

def testadd():
    params={}
    params['productCode'] = 'P111'
    params['productName']='Camera'
    params['price'] = 1500.0
    params['status']='available'
    model = product()
    model.add(params)

def testupdate():
    params={}
    params['productId'] = '11'
    params['productCode'] = 'P111'
    params['productName'] = 'Camera'
    params['price'] = 1500.0
    params['status'] = 'Out of stock'
    model = product()
    model.update(params)

def testdelete():
    model = product()
    model.delete(11)

def testsearch():
    params={}
    params['productName'] = 'phone'
    model = product()
    list = model.search(params)
    for data in list:
        print(data['productId'],'\t',data['productCode'],'\t',data['productName'],'\t',
              data['price'],'\t',data['status'])

#testadd()
#testupdate()
#testdelete()
testsearch()


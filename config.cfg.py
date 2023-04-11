import shelve
shelf=shelve.open('cfg')
shelf['name'] = 'Alice'
shelf['age'] = 30
# print(shelf['list1'])
shelf.close()


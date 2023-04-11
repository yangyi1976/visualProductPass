import shelve

shelf=shelve.open('cfg')
shelf['ORCServer_IP'] = '172.16.18.127'
shelf['kernelWidth'] = '2'
shelf['kernelHeight'] ='5'
shelf['cameraWidth']='1900'
shelf['cameraHeight'] ='1600'
shelf['ocuppyMin'] ='7'
shelf['ocuppyMax']='11'

shelf.close()



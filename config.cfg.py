import shelve

shelf=shelve.open('cfg')
shelf['ORCServer_IP'] = '172.16.18.127'
shelf['kernelWidth'] = '2'
shelf['kernelHeight'] ='5'
shelf['cameraWidth']='1920'
shelf['cameraHeight'] ='1080'
shelf['ocuppyMin'] ='7'
shelf['ocuppyMax']='11'
shelf['cameraIndex']='0'
shelf['storeFilesDays']='90'
shelf['upload_servIp']='10.8.0.0'
shelf['upload_servPort']='80'
shelf['upload_servAPI']='/upload/'

shelf.close()



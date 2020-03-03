#
#    Module: rest_api.py
#
#    General REST-API
#
#    Ver-0.20, 20200218, debug prints to syserr
#
#    $ python ./rest_api  <IP>  <sub_url> <body> <method> <uid> <pwd>
#
#    return REST api
#
import os
import sys
import traceback
import json
import requests
#import read_credentials

#
def rest_api(url, payload, method, user, password):
#
#    print "ip=%s" % ip
#    print "sub_url=%s" % sub_url
#    print "body=%s" % payload
#    print "method=%s" % method
   
    URL= url
    print >> sys.stderr,  "url=%s" % URL
    
    jpayload=json.dumps(payload)

    headers={'Content-Type': 'application/json; charset=utf-8'} 

    uid = user
    pwd = password

    r = requests.Response()
    try:
        if (method == 'get'):
            r = requests.get(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
        elif (method == 'post'):
            r = requests.post(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
        elif (method == 'delete'):
            r = requests.delete(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
        elif (method == 'put'):
            r = requests.put(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
        else:            
            print >> sys.stderr, "Bad method %s. Program Abort!" % method
            exit()
    except requests.exceptions.RequestException as e:
        f_success = False
            
        print >> sys.stderr, "Requests Exception== %s" % e
        print >> sys.stderr, "Credentials: maybe not be reachable to Target!"
        r.status_code = 400
    else:
        if (r.status_code in [200,201,202,203,204,205,206]):
            f_success = True
            print >> sys.stderr,"(%s,*****):Credentials Success" % (uid)   # pwd
        else:     # case of Authentication Error.
            f_success = False
            print >> sys.stderr, "code=%s",r.status_code
            print >> sys.stderr, "(%s,%s):Credentials Fail!x" % (uid,pwd)

    return r

#######################

if (__name__=='__main__'):
    VIP='172.16.105.109'
    URL='https://'+VIP+':9440/' + 'PrismGateway/services/rest/v1/clusters/'

    payload={}

    r = requests.Response()
    r = rest_api(URL,payload,'get','admin','HA8kV2018/4u!')

    print r.text

    
    URL='https://172.16.105.109:9440/PrismGateway/services/rest/v2.0/storage_containers/'
    payload={"name":"CNTR02"}

    r = requests.Response()
    r = rest_api(URL,payload,'post','admin','HA8kV2018/4u!')

else:
    pass

#
#
#
#
#   Python to get cluster's ha status and disk(SSD) usage to check behavior in rebuild.
#
#   Ver-0.10: 07Feb2020, @tm
#
#
#
import os
import sys
import traceback
import requests as r
import json
import time
import rest_api as ra

def get_cluster_ha_status(ip,uid,pwd):
    URL = "https://" + ip + ":9440/PrismGateway/services/rest/v2.0/ha/"
    pld={}
    md='get'
    
    res = r.Response()
    res = ra.rest_api(url=URL,payload=pld,method=md,user=uid,password=pwd)

    return res

def get_cluster_disk_ssd_status(ip,uid,pwd):
    URL = "https://" + ip + ":9440/PrismGateway/services/rest/v2.0/disks/?search_string=SSD"
    pld={}
    md='get'
    
    res = r.Response()
    res = ra.rest_api(url=URL,payload=pld,method=md,user=uid,password=pwd)

    return res


def get_cluster_disk_ssd_usage():
    pass


if __name__=="__main__":
    VIP = "172.16.105.106"
    
    USER='admin'
    PASSWORD ='HA8kV2018/4u!'

    t = int(time.time())
    res = r.Response()
    res = get_cluster_ha_status(ip=VIP,uid=USER,pwd=PASSWORD)
    
    # print "Return_code:%d" % res.status_code
    # print "%s"  % res.text
    
#    num = 0
#    end = res.json()['metadata']['total_entities']

    print "TIME,",
    print "\t","FAILOVER_ENABLED,",
    print "\t","FAILOVER_IN_PROGRESS_HOST_UUID,",
    print "\t","HA_STATE,",
#        print "\t","STORAGE_USAGE(BYTES),",
#        print "\t","version,",
#        print "\t","model,",
#        print "\t","modelName,"
    print
    #
    print "%12d," % t ,
    print "\t%r," % res.json()['failover_enabled'],",",
    print "\t%s" % res.json()['failover_in_progress_host_uuids'],",",
    print "\t",res.json()['ha_state'],",",
#        print "\t",res.json()['entities'][num]['usage_stats']['storage.usage_bytes'],",",
#        print "\t",r.json()['entities'][num]['hypervisorTypes'],",",
#        print "\t",r.json()['entities'][num]['version'],",",
#        print "\t",r.json()['entities'][num]['rackableUnits'][0]['model'],",",
#        print "\t",r.json()['entities'][num]['rackableUnits'][0]['modelName'],","
    print
#        num+=1

    t = int(time.time())   
    res = r.Response()
    res = get_cluster_disk_ssd_status(ip=VIP,uid=USER,pwd=PASSWORD)
    
    #print "Return_code:%d" % res.status_code
    #print "%s"  % res.text

    num = 0
    end = res.json()['metadata']['total_entities']

    print ################################

    while num < end:
#        print ","+"Name,  ",
        print "ITME(on monitoring host),",
        print "\t","IP,",
        print "\t","ONLINE,",
        print "\t","DISK_STATUS,",
        print "\t","STORAGE_USAGE(BYTES),",
#        print "\t","version,",
#        print "\t","model,",
#        print "\t","modelName,"
        print
    #
        print "%12d," % t ,
        print res.json()['entities'][num]['host_name'],",",
        print "\t",res.json()['entities'][num]['online'],",",
        print "\t",res.json()['entities'][num]['disk_status'],",",
        print "\t",res.json()['entities'][num]['usage_stats']['storage.usage_bytes'],",",
#        print "\t",r.json()['entities'][num]['hypervisorTypes'],",",
#        print "\t",r.json()['entities'][num]['version'],",",
#        print "\t",r.json()['entities'][num]['rackableUnits'][0]['model'],",",
#        print "\t",r.json()['entities'][num]['rackableUnits'][0]['modelName'],","
        print
        num+=1
    
    print ###############
    print "End"



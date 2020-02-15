#
#
#
#
#   Python to get cluster's ha status and disk(SSD) usage to check behavior in rebuild.
#
#   Ver-0.13: 14Feb2020, change output format.
#   Ver-0.12: 08Feb2020, @tm, get&show disk id
#   Ver-0.11: 08Feb2020, @tm, timestamp
#   Ver-0.10: 07Feb2020, @tm, initial implementation
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
    
def print_cluster_ha_status(t,res):    
    print "TIME,      ",
    print "\t","FAILOVER_ENABLED,",
    print "\t","FAILOVER_IN_PROGRESS_HOST_UUID,",
    print "\t","HA_STATE,",
    print
    #
    print "%12d," % t ,
    print "\t%r," % res.json()['failover_enabled'],
    print "\t%s," % res.json()['failover_in_progress_host_uuids'],
    print "\t",res.json()['ha_state'],",",
    print

def get_cluster_disk_status(ip,uid,pwd):
    URL = "https://" + ip + ":9440/PrismGateway/services/rest/v2.0/disks/?search_string="
    pld={}
    md='get'
    
    res = r.Response()
    res = ra.rest_api(url=URL,payload=pld,method=md,user=uid,password=pwd)

    return res
    

def get_cluster_disk_ssd_usage():
    pass

def print_cluster_disk_usage(t,res):
    num = 0
    end = res.json()['metadata']['total_entities']

    while num < end:
        print "TIME(on monitoring host),",
        print "\tIP,",
        print "\tDISK ID,",
        print "\tTYPE,",
        print "\tONLINE,",
        print "\tDISK_STATUS,",
        print "\tSTORAGE_USAGE(BYTES),"
    #
        disk_id =res.json()['entities'][num]['id']
        id = disk_id[38:]
        
        print "%12d," % t ,
        print "\t%s," % res.json()['entities'][num]['host_name'],
        print "\t%s," % id.strip(),
        print "\t%s," % res.json()['entities'][num]['storage_tier_name'],
        print "\t%s," % res.json()['entities'][num]['online'],
        print "\t%s," % res.json()['entities'][num]['disk_status'],
        print "\t%s," % res.json()['entities'][num]['usage_stats']['storage.usage_bytes']
        
        num+=1
    
    ################################
    
    print "End"

def print_cluster_list_disk_usage(t,res):
    print  "%12d," % t ,
    num = 0
    end = res.json()['metadata']['total_entities']
    
    while num < end:
        ip_address=res.json()['entities'][num]['host_name']       
        tier = res.json()['entities'][num]['storage_tier_name']
        disk_id =res.json()['entities'][num]['id']
        id = disk_id[38:]
        u = res.json()['entities'][num]['usage_stats']['storage.usage_bytes']
        print "[%s,%s,%s,%s]," % (ip_address,tier,id,u) , 
        num +=1 

if __name__=="__main__":
    VIP = "172.16.105.106"
    
    USER='admin'
    PASSWORD ='HA8kV2018/4u!'

    t = int(time.time())
    res = r.Response()
    res = get_cluster_ha_status(ip=VIP,uid=USER,pwd=PASSWORD)

    # print "Return_code:%d" % res.status_code
    # print "%s"  % res.text
    
    print_cluster_ha_status(t,res)
    
    ################################

    t = int(time.time())   
    res = r.Response()
    res = get_cluster_disk_status(ip=VIP,uid=USER,pwd=PASSWORD)
    
    print_cluster_disk_usage(t,res)

    print_cluster_list_disk_usage(t,res)
    
    ################################
    
#   print "End"
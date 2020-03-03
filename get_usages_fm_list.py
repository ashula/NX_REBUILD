import sys
import os
import json
import argparse


if (__name__=='__main__'):

    parser = argparse.ArgumentParser(description = "read disk stats file and return time & [usages].")
    
#    parser.add_argument('-h','--help', help="Read data file and return time and usages.")
    parser.add_argument('-d','--dataf',type=str,help="data file name")
    
    args=parser.parse_args()
    
    if args.dataf:
       df = open(args.dataf,'r')
       
       for line in df:
           line=line[:len(line)-1]

           print "#"

           lst = eval(line)
           print lst
           print "##"
           print lst[0]
           print lst[1]
           print lst[len(lst)-10:]
           print "###"

           num=0
           print lst[0],

           print ', [' ,
           for dstats in lst[2:]:
               if dstats[2] == 'SSD':
                   if num==0:
                       print "%d" % dstats[3],
                   print ",%d" % dstats[3],
                   num+=1

           print ']'
           
       
       df.close()
     
    
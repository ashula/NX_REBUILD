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

           print >> sys.stderr,  "#"

           lst = eval(line)
           print >> sys.stderr, lst
           print >> sys.stderr, "##"
           print >> sys.stderr, lst[0]
           print >> sys.stderr, lst[1]
           print >> sys.stderr, lst[len(lst)-10:]
           print >> sys.stderr, "###"

           num=0
           print lst[0],

#           print ', [' ,
           print ', ' ,
           for dstats in lst[2:]:
               if dstats[2] == 'SSD':
                   if num==0:
                       print "%d" % dstats[3],
                   else:
                       print ",%d" % dstats[3],
                   num+=1

#           print ']'
           print
       
       df.close()
     
    
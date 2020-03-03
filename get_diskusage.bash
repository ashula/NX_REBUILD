#! /bin/bash
#
#  $1: output mode
#  $2: CVM IP address
#  $3: UID
#  $4: PWD
#
for i in {1..30}
do
    diskusage_record="_diskusage_log.txt"
    d="`date +%Y%m%d_%H%M`"
    c="$d$diskusage_record"

    echo $d
    echo $c
    echo $t

    python ./cluster_rebuild.py --f $1 -i $2 -u $3 -p $4   > $c
    echo $d
    sleep 120
done

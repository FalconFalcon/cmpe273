
import psutil
import subprocess
import os
import re
import collections
from pprint import pprint as pp
from itertools import groupby
from operator import itemgetter
from operator import attrgetter

out = psutil.net_connections(kind='tcp')
output = []
counter=0
groupingPID=sorted(out,key=attrgetter('pid')) #PIDs are grouped here
countingPID= collections.Counter(t[6] for t in groupingPID) 
sortedbyconnections=sorted(groupingPID,key=lambda t:countingPID[t[6]],reverse=True) #sort
print '"pid"','"laddr"','"raddr"','"status"'
for x in sortedbyconnections:
    pid = x.pid
    raddr = x.raddr
    laddr = x.laddr
    status = x.status
    if raddr:   #check if raddr is present
    	if laddr:   #check is laddr is present
    		laddr_str = laddr[0] + '@' + str(laddr[1]) 
    		raddr_st = raddr[0] + '@' + str(raddr[1])
    		output.append([pid,laddr_str,raddr_st,status])
# for key, items in groupby(output, itemgetter(0)):
#     print key
#     for subitem in items:
#         print subitem
#    print '-' * 65
for element in output:
    print ("\"%d\",\"%s\",\"%s\",\"%s\"" % (element[0], element[1], element[2], element[3]));


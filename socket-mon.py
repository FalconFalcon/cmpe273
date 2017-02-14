
import psutil
import subprocess
import os
import re
from pprint import pprint as pp

# print "List of all connections using sockets"

# class mysockets:
#      def __init__(self, pid, laddr, raddr, status):
#          self.pid = pid
#          self.laddr = laddr
#          self.raddr = raddr
#          self.status = status


out = psutil.net_connections()
#pp(out)
output = [];
out.sort(key=lambda a: a.pid, reverse=False)
print "pid"','"laddr"','"raddr"','"status"
for x in out:
    #print x.pid + "," str(x.laddr) "," + x.raddr + "," + x.status
    pid = x.pid
    raddr = x.raddr
    laddr = x.laddr
    status = x.status
    if raddr: 
    	laddr_str = laddr[0] + '@' + str(laddr[1]) 
    	raddr_st = raddr[0] + '@' + str(raddr[1])
    	output.append([pid,laddr_str,raddr_st,status])
for element in output:
	print ("\"%d\",\"%s\",\"%s\",\"%s\"" % (element[0], element[1], element[2], element[3]));

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


# hosts = [mysockets(1, "asdasd", "fghdfgdf", "dfgdfgdf"),
#          mysockets(26, "rtyrtyr", "rtyrty", "rtyrtyrt"),
#          mysockets(33, "rtyrtyr", "rtyrt", "rtyrtyrt"),
#          mysockets(4, "bfvbv", "cvbcvcv", "cvbcvbcvv")]

out = psutil.net_connections()
#pp(out)
out.sort(key=lambda a: a.pid, reverse=False)
print "pid"','"laddr"','"raddr"','"status"
for x in out:
    #print x.pid + "," str(x.laddr) "," + x.raddr + "," + x.status
    if x.raddr: print x.pid, x.raddr, x.laddr, x.status

#!/usr/bin/env python

################################################################################
#
# urllib function to get the public IP of the host computer.
# File inception on 2015-08-04 (Huki).
#
################################################################################

import re
import sys
if sys.version_info >= (3, 0):
  from urllib.request import urlopen
else:
  from urllib2 import urlopen

ip_check_url = 'http://checkip.dyndns.org'
ip_reg_exp = r'[0-9]+(?:\.[0-9]+){3}'

def GetPublicIpAddress():
  content = str(urlopen(ip_check_url, timeout=5).read())
  for ip in re.findall(ip_reg_exp, content):
    return ip

################################################################################

if __name__ == '__main__':
  print(GetPublicIpAddress())

#!/usr/bin/env python

################################################################################
#
# socket function to get the public IP address of the host computer.
# File inception on 2015-08-04 (Huki).
#
################################################################################

import re
import socket

ip_check_url = 'checkip.dyndns.org'
ip_request = 'GET / HTTP/1.1\r\nHost: ' + ip_check_url + '\r\nConnection: close\r\n\r\n'
ip_reg_exp = r'[0-9]+(?:\.[0-9]+){3}'

def GetPublicIpAddress():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((ip_check_url, 80))
  s.sendall(ip_request)
  content = ''
  while True:
    data = s.recv(8192)
    if not data: break
    content += data
  for ip in re.findall(ip_reg_exp, content):
    return ip

################################################################################

if __name__ == '__main__':
  print(GetPublicIpAddress())

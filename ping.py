from os import system

## This function pings for a response from 
## a potential ip address
def check(ip_addr):
  res = system("ping -c 1 " + ip_addr)
  if res == 0:
    return True
  else:
    return False

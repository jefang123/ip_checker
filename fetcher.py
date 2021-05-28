from datetime import date
import requests
# import ping

def fetch_ips():
  url = "https://raw.githubusercontent.com/stamparm/ipsum/master/levels/5.txt"
  res = requests.get(url)
  ip_list = res.text.split("\n")
  s = set()
  for i in ip_list:
    s.add(i)
    # if ping.check(i):
    # this source file validation check takes too long 
    # to set up synchronously, use asyncio 
  return(s)

class IPStorage:
  def __init__(self):
    self.fetchDate = date.today()
    self.ips = fetch_ips()
  def refresh(self):
    self.ips = fetch_ips()
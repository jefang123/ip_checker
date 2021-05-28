## checks validity of input ip_addr
def check(ip_addr):
  parts = ip_addr.split('.')
  for part in parts:
    try:
      i = int(part)
      if i < 0 or i > 255:
        return False
    except:
      # part is not integer string
      return False 
  return True
  
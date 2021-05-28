import json
import unittest
from random import choice, randrange
import fetcher
import checkip
from fetcher import IPStorage

from app import app 
app.testing = True

class TestSuite(unittest.TestCase):
  def test_correct_ip(self):
    nums = [str(randrange(0, 256)) for i in range(4)]
    ip = ".".join(nums)
    self.assertEqual(checkip.check(ip), True)

  def test_incorrect_ip(self):
    incorrect_ips = ['257.345.12.345', '-1.3.1.4', 'fake.ip.ad.ress']
    for ip in incorrect_ips:
      self.assertEqual(checkip.check(ip), False)

  def test_fetcher(self):
    store = IPStorage()
    fake_value = "THIS IS FAKE DATA"
    store.ips = fake_value
    store.refresh()
    self.assertNotEqual(store.ips, fake_value)
  
  def test_invalid_ips(self):
    msg = {'status': 400, 'reason': 'invalid ips given'}
    with app.test_client() as client:
      sent = {"ips": ['bad.ip', 'fake']}
      result = client.post(
        '/checkips',
        json = sent
      )
      self.assertEqual(json.loads(result.data), msg)
  
  def test_valid_ips(self):
    store = IPStorage()
    ips = [choice(tuple(store.ips)) for i in range(2)]
    with app.test_client() as client:
      sent = {"ips": ips}
      result = client.post(
        '/checkips',
        json = sent
      )
      self.assertEqual(json.loads(result.data), 2)


if __name__ == "__main__":
  unittest.main()
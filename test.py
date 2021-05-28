import unittest
from random import randrange
import fetcher
import checkip
from fetcher import IPStorage

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

if __name__ == "__main__":
  unittest.main()
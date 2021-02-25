import unittest
import fibonacci

class TestSeq(unittest.TestCase):
  def testInit(self):
    self.assertEqual(fibonacci.fun(0), 0)
  def testSum(self):
    self.assertEqual(fibonacci.fun(1)+fibonacci.fun(2), 2)
  def testSeq(self):
    self.assertEqual(fibonacci.fun(9), 34)

if __name__ == '__main__':
  unittest.main()
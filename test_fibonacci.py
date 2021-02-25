import unittest
import fibonacci

class TestSeq(unittest.TestCase):
  def testInit(self):
    self.assertEqual(fibonacci.fun(0), 0)
  def testSum(self):
    self.assertEqual(fibonacci.fun(1)+fibonacci.fun(2), 2)
  def testSeq(self):
    self.assertEqual(fibonacci.fun(9), 34)

#pytest

def test_base():
  x = 0
  assert fibonacci.fun(x) == 0
  assert fibonacci.fun(x+1) == 1

def test_sum():
  x = 2
  assert fibonacci.fun(x) == 1

def test_seq():
  x = 8
  assert fibonacci.fun(x) == 21

if __name__ == '__main__':
  unittest.main()
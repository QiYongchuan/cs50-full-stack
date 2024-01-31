import unittest

from prime import is_prime

class Tests(unittest.TestCase):
  def test_1(self):
    """Check that 1 is not prime."""
    self.assertFalse(is_prime(1))
    
  def test_2(self):
    """Check that 2 is not prime."""
    self.assertTrue(is_prime(2))
    
  def test_8(self):
    """Check that 8 is not prime."""
    self.assertFalse(is_prime(1))
    
  def test_11(self):
    """Check 11 is prime"""
    self.assertTrue(is_prime(11))
  
  def test_25(self):
    """Check 25 is not prime"""
    self.assertFalse(is_prime(25))
  
  def test_8(self):
    """Check 28 is not prime"""
    self.assertFalse(is_prime(8))
    
    
if __name__=="__main__":
  unittest.main();
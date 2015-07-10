import unittest

from invoice_calculator import divide_pay


class InvoiceCalculatorTests(unittest.TestCase):
  def testDividedFairly(self):
    # Test for correctly returned values if hours are correctly entered
    pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0})
    self.assertEqual(pay, {"Alice": 90.0, "Bob": 90.0, "Carol": 180.0})
  
  def testZeroHourPerson(self):
    # Test for person entering zero hours
    pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 6.0, "Carol": 0.0})
    self.assertEqual(pay, {"Alice": 120.0, "Bob": 240.0, "Carol": 0.0})
    
  def testZeroHoursTotal(self):
    # Test for no hours entered by any staff
    with self.assertRaises(ValueError):
      pay = divide_pay(360.0, {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0})
  
  def testNoPeople(self):
    # Test for no person entered (empty dictionary)
    with self.assertRaises(ValueError):
      pay = divide_pay(360.0, {})


if __name__ == "__main__":
  # Call to collect and run any tests contained in the file
  unittest.main()
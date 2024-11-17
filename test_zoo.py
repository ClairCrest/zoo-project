import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price_C1b1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "ERROR") # 1 Fault fixed

    def test_child_ticket_price_C1b2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)# 2 Fault fixed
    
    def test_child_ticket_price_C1b3(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100) # 3 Fault fixed

    def test_child_ticket_price_C1b4(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150) # 4 Fault fixed

    def test_child_ticket_price_C1b5(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100) 
    # Add your additional test cases here.

if __name__ == '__main__': #function
    unittest.main()
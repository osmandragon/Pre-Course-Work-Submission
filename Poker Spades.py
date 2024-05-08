import unittest

def check_straight(card1, card2, card3):
    cards = {'S2' :2,'S3' :3,'S4' :4,'S5' :5,'S6' :6,'S7' :7,'S8' :8,'S9' :9,'S10' :10,'SJ' :11,'SQ' :12,'SK' :13,'SA' :14}

class MyTestCase(unittest.TestCase):

    def test_check_straight(self):
        self.assertTrue(check_straight(5, 1, 3))
        self.assertTrue(check_straight(1, 1, 1))
        self.assertTrue(check_straight(0, 0, 0))
        self.assertTrue(check_straight(1, 2, 3))
        self.assertTrue(check_straight(5, 1, 9))

        self.assertFalse(check_straight(5, 1, 3))
        self.assertFalse(check_straight(1, 1, 1))
        self.assertFalse(check_straight(0, 0, 0))
        self.assertFalse(check_straight(1, 2, 3))
        self.assertFalse(check_straight(5, 1, 9))

if __name__ == '__main__':
    unittest.main()

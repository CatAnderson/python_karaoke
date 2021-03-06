import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Rizzo", 19, 50.00)
        self.guest_2 = Guest("Sandy", 18, 30.50)
        self.guest_3 = Guest("Danny Zuko", 20, 34.50)
        self.guest_4 = Guest("Frenchie", 16, 4.50)
    
    def test_guest_has_name(self):
        self.assertEqual("Rizzo", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(20, self.guest_3.age)

    def test_guest_has_money_in_wallet(self):
        self.assertEqual(30.50, self.guest_2.wallet)
    
    def test_alter_guest_wallet(self):
        self.guest_3.alter_guests_wallet_amount(5.50)
        self.assertEqual(29.00, self.guest_3.wallet)

    def test_guest_does_not_have_enough_money(self):
        self.assertEqual("Not enough money!", self.guest_4.alter_guests_wallet_amount(5.50))
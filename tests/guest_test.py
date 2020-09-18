import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_betty = Guest("Rizzo", 19, 50.00)
        self.guest_sandy = Guest("Sandy", 18, 30.50)
        self.guest_danny = Guest("Danny Zuko", 20, 34.50)
        self.guest_francesca = Guest("Frenchie", 16, 29.00)
    
    def test_guest_has_name(self):
        self.assertEqual("Rizzo", self.guest_betty.name)

    def test_song_has_age(self):
        self.assertEqual(20, self.guest_danny.age)

    def test_song_has_moeny_in_wallet(self):
        self.assertEqual(30.50, self.guest_sandy.wallet)
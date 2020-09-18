import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("T-Birds")
        self.room_2 = Room("Pink Ladies")

        self.song_1 = Song("Hopelessly Devoted To You", "Olivia Newton-John")
        self.song_2 = Song("Beauty School Drop-Out", "Frankie Avalon")
        self.song_3 = Song("Look at Me, I'm Sandra Dee", "Stockard Channing")
        self.song_list = [self.song_1, self.song_2]

        self.guest_betty = Guest("Rizzo", 19, 50.00)
        
        self.guest_danny = Guest("Danny Zuko", 20, 34.50)
        self.guest_francesca = Guest("Frenchie", 16, 4.50)
        self.guest_list = [self.guest_betty, self.guest_danny, self.guest_francesca]

    def test_karaoke_room_has_name(self):
        self.assertEqual("Pink Ladies", self.room_2.name)

    def test_karaoke_room_has_guests_in_it(self):
        self.assertEqual(3, len(self.guest_list))

    def test_karaoke_room_has_songs_to_sing(self):
        self.assertEqual(2, len(self.song_list))

    def test_adding_guest_to_karaoke_room(self):
        self.guest_sandy = Guest("Sandy", 18, 30.50)
        Room.check_in_guest_to_room(self, self.guest_sandy)
        self.assertEqual(4, len(self.guest_list))


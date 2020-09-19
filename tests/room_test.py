import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("T-Birds")
        self.room_2 = Room("Pink Ladies")

        self.song_1 = Song("Hopelessly Devoted To You", "Olivia Newton-John")
        self.song_2 = Song("Beauty School Drop-Out", "Frankie Avalon")
        self.song_list = [self.song_1, self.song_2]

        self.guest_1 = Guest("Rizzo", 19, 50.00)
        self.guest_2 = Guest("Danny Zuko", 20, 34.50)
        self.guest_3 = Guest("Frenchie", 16, 4.50)
        self.guest_list = [self.guest_1, self.guest_2, self.guest_3]


    def test_karaoke_room_has_name(self):
        self.assertEqual("Pink Ladies", self.room_2.name)

    def test_karaoke_room_has_guests_in_it(self):
        self.assertEqual(3, len(self.guest_list))

    def test_karaoke_room_has_songs_to_sing(self):
        self.assertEqual(2, len(self.song_list))

    def test_adding_guest_to_karaoke_room(self):
        self.guest_4 = Guest("Sandy", 18, 30.50)
        Room.check_in_guest_to_room(self, self.guest_4)
        self.assertEqual(4, len(self.guest_list))

    def test_removing_guest_from_karaoke_room(self):
        Room.check_out_guest_from_room(self, self.guest_2)
        self.assertEqual(2, len(self.guest_list))

    def test_adding_song_to_playlist(self):
        self.song_3 = Song("Look at Me, I'm Sandra Dee", "Stockard Channing")
        Room.adding_song_to_playlist(self, self.song_3)
        self.assertEqual(3, len(self.song_list))

    def test_karaoke_room_capacity(self):
        self.assertEqual(3, self.room_1.room_capacity)
    
    def test_no_space_left_in_karaoke_room(self):
        self.guest_4 = Guest("Sandy", 18, 30.50)
        Room.check_in_guest_to_room(self, self.guest_4)
        # self.assertEqual(3, len(self.guest_list))
        self.assertEqual("No spaces left", self.room_1.no_spaces_left_in_room(self.guest_list))
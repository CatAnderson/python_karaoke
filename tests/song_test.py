import unittest

# from src.guest import Guest
# from src.room import Room
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Hopelessly Devoted To You", "Olivia Newton-John")
        self.song_2 = Song("Beauty School Drop-Out", "Frankie Avalon")
        self.song_3 = Song("Look at Me, I'm Sandra Dee", "Stockard Channing")

    def test_song_has_title(self):
        self.assertEqual("Hopelessly Devoted To You", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Frankie Avalon", self.song_2.artist)

    
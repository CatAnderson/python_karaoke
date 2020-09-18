from src.song import Song
from src.guest import Guest

class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []
        self.room_capacity = 3
        self.entrance_fee = 5.50
        self.till = 0


    def check_in_guest_to_room(self, guest):
        self.guest_list.append(guest)

    def check_out_guest_from_room(self, guest):
        self.guest_list.remove(guest)

    def adding_song_to_playlist(self, song):
        self.song_list.append(song)

        
    

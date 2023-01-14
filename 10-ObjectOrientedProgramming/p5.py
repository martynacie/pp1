class music():
    def __init__(self, performer, song, album, year):
        self.performer = performer
        self.song = song
        self.album = album
        self.year = year
    def __str__(self) -> str:
        return "Performer:" 
        
my_music = music('Ed',"hearts","divide",2017)
print(my_music)  
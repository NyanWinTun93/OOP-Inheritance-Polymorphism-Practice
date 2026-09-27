class Media:
    def __init__(self, title):
        self.title = title
    def play(self):
        print(f'Playing media : {self.title}')
class Audio(Media):
    def __init__(self, title,duration):
        super().__init__(title)
        self.duration = duration
    def play(self):
        print(f'Playing audio : {self.title}')
class Podcast(Audio):
    def __init__(self, title,duration,host):
        super().__init__(title,duration)
        self.host = host
    def play(self):
        print(f'Playing podcast : {self.title} hosted by {self.host}.')
media = Media ('Python Basics')
media.play()
audio = Audio ('Relexing Music','4 minutes')
audio.play()
podcast = Podcast('AI Today',4,'John')
podcast.play()

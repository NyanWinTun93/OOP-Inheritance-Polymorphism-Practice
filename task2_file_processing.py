class FileProcessor:
    def __init__(self, filename):
        self.filename = filename
    def process(self):
        print(f'Processing {self.filename}')
class TextFile(FileProcessor):
    def process(self):
        print(f'Processing text file: {self.filename}')
class ImageFile(FileProcessor):
    def process(self):
        print(f'Processing image file: {self.filename}')
class AudioFile(FileProcessor):
    def process(self):
        print(f'Processing audio file: {self.filename}')
text1 = TextFile('notes.txt')
photo = ImageFile('photo.jpg')
audio = AudioFile('audio.mp3')
files = [text1, photo, audio]
for file in files:
    file.process()

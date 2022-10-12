class MediaPlayer:
    def open(self, filename):
        self.filename = filename

    def play(self):
        print('Воспроизведение ' + str(self.filename))


media1 = MediaPlayer()
media2 = MediaPlayer()


media1.open('filemedia1')
media2.open('filemedia2')

media1.play()
media2.play()




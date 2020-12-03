class Environment:

    def getTime(self):
        pass

    def playWavFile(self, file):
        pass

    def wavWasPlayed(self):
        pass

    def resetWav(self):
        pass


class Checker:

    def __init__(self):
        self.env = Environment()

    def remainder(self, file):
        time = self.env.getTime()
        if time > 17:
            self.env.playWavFile(file)
            return self.env.wavWasPlayed()
        else:
            return self.env.resetWav()

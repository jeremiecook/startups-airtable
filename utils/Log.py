from utils.Singleton import Singleton


class Log(Singleton):

    logs = []

    def info(self, text):
        self.logs.append(text)

    def print(self):
        for text in self.logs:
            print(text)

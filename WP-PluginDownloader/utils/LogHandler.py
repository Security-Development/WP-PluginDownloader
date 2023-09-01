from sys import exit
from utils.ColorInterface import ColorInterface

# use utils
ColorInterface = ColorInterface()

class LogHandler:
    def __init__(self):
        self.prefix = "[ WP-PluginDownloader {0} ] : "

    def error_msg(self, text):
        exit("{0}{1}{2}{3}".format(ColorInterface.RED, self.prefix.format("Error"), str(text), ColorInterface.DEFAULT))
    
    def info_msg(self, text):
        print("{0}{1}{2}{3}".format(ColorInterface.GREEN, self.prefix.format("Info"), str(text), ColorInterface.DEFAULT))

    def call_msg(self, text):
        print("{0}{1}{2}{3}".format(ColorInterface.BLUE, self.prefix.format("Call"), str(text), ColorInterface.DEFAULT))
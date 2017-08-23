from datetime import datetime
from termcolor import colored


class Logger:
    def __init__(self, tid):
        self.format = '%H:%M:%S'
        self.tid = tid

    def log(self, text, color=None):
        timestamp = datetime.now().strftime(self.format)
        if color is not None:
            try:
                text = colored(text, color)
            except:
                print 'WARNING: unrecognized color passed to logger instance'
        print('[{}] :: {}'.format(timestamp, text))

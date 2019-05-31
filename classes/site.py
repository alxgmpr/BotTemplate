import threading
from json import load
from time import time, sleep

from classes.logger import Logger
from classes.product import Product


class Site(threading.Thread):
    def __init__(self, tid, config_filename):
        threading.Thread.__init__(self)
        self.tid = tid
        self.start_time = time()
        self.log = Logger(tid).log
        with open(config_filename) as task_file:
            self.T = load(task_file)
        with open('config.json') as config_file:
            self.C = load(config_file)

    def wait(self):
        self.log('sleeping {} second(s)'.format(self.C['sleep_time']))
        sleep(self.C['sleep_time'])

    def get_products(self):
        self.log('getting some products')
        # idk make some requests here??
        self.wait()

    def match_products(self):
        self.log('comparing products', 'red')
        # idk do some keyword checking??
        self.wait()

    def add_to_cart(self):
        self.log('adding product to cart', 'blue')
        # idk add something to cart??
        self.wait()

    def checkout(self):
        self.log('checking out')
        # idk pay for the things in your cart??
        self.wait()

    def run(self):
        self.get_products()
        self.match_products()
        self.add_to_cart()
        self.checkout()
        self.log('time to checkout: {} sec'.format(abs(self.start_time-time())), 'green')

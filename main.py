from os import listdir
from termcolor import colored
from classes.site import Site
from classes.logger import Logger

# Bot template written by Alex Gompper, available under MIT license @ https://github.com/alxgmpr/BotTemplate
# Please don't remove this credit. If you like what I've done here, or make something cool with it, shout me out!
# twitter: @edzart


def main():
    log = Logger('M').log
    log(colored('main bot template made by Alex Gompper @573supreme', 'green'))
    threads = []
    i = 0
    for config in listdir('tasks'):
        if config in {'task.example.json'}:  # configs to ignore
            pass
        else:
            log('loading thread {} with config {}'.format(i, config))
            threads.append(Site(i, 'tasks/' + config))
            threads[i].start()
            i += 1

if __name__ == '__main__':
    main()

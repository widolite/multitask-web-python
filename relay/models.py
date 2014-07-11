#!/usr/bin/python
__author__ = "Ing. Hector Guerrero Landaeta"
__email__ = "hectorguerrero1866@gmail.com"
__api__ = "Multitask"
import RPi.GPIO as GPIO

# Create your models here.


class Relay(object):
    PINS = [4, 17, 27, 22, 25, 24, 23, 18]

    channel = ''

    status = ''

    name = ''

    def __str__(self):

        return "Channel %s" % self.pin

    def __init__(self, channel, name=''):

        """
        Setting the channel with the number of the board e.g if relay is 1 then channel is 4
         0   1   2  3  4   5   6   7
        [4, 17, 22, 7, 8, 25, 24, 23]
        The mode is in BCM for raspberry 2REV.
        The configuration can not be initialized with GPIO.HIGH because it causes the relay turns on by default
        and this is not the behavior we really want.
        :param channel:
        :param name:
        """
        self.pin = self.PINS[channel - 1]

        self.name = name

        self.channel = channel

        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pin, GPIO.OUT)

    @property
    def status(self):

        return GPIO.input(self.pin)

    def toggle(self, sec=0):

        from time import sleep

        if self.status == 0 and sec != 0:
            GPIO.output(self.pin, not self.status)

        GPIO.output(self.pin, not self.status)

        if sec != 0:
            sleep(sec)
            GPIO.output(self.pin, not self.status)
        else:
            return

        if self.status == 1:
            GPIO.cleanup(self.pin)


def main():
    parser = OptionParser(description="Command to interact with the GPIO of the raspberry", version="1.0", usage="")

    parser.add_option("-c", "--channel", dest="channel", help="Channel number to be activated")

    parser.add_option("-s", "--seconds", dest="sec", help="Seconds until the channel turn off")

    parser.add_option("-n", "--name", dest="name", help="Name to set to the channel")

    parser.add_option("-t", "--toggle", dest="toggle", help="Toggle the channel")

    parser.add_option("-S", "--status", dest="status", help="Get the status of the channel")

    options, arguments = parser.parse_args()

    options.channel = int(DEFAULTS['channel']) if not options.channel else int(options.channel)

    options.sec = float(DEFAULTS['sec']) if not options.sec else float(options.sec)

    options.name = DEFAULTS['name'] if not options.name else options.name

    if options.channel and options.status:

        channel = Relay(options.channel)

        sys.exit(channel.status)

    elif options.channel and options.toggle:

            channel = Relay(options.channel)

            channel.toggle(options.sec)

            sys.exit(channel.status)

    else:

        parser.print_help()


if __name__ == '__main__':
    from optparse import OptionParser

    import sys

    DEFAULTS = {'channel': '1', 'sec': '0.0', 'name': 'Channel'}

    main()
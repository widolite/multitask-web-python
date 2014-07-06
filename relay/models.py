__author__ = "Ing. Hector Guerrero Landaeta"
__email__ = "hectorguerrero1866@gmail.com"
__api__ = "Multitask"
import RPi.GPIO as GPIO

# Create your models here.


class Relay(object):
    PINS = [4, 17, 22, 7, 8, 25, 24, 23]

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


if __name__ == '__main__':
    pass
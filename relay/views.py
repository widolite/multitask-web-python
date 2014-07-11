import re
import json
import subprocess

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.http import Http404, HttpResponse

from relay.models import Relay



# Create your views here.


class DummyRelay(object):

    def __init__(self, channel, name='', status=''):

        self.name = name

        self.channel = channel

        self.status = status

def index(request):
    """
        Index of the system
    """
    channels_info = {'1': ['Garage'], '2': ['Backyard'], '3': ['Theater'], '4': ['Main Door'], '5': ['Garden'],
                '6': ['Back-Door']}

    channels = []

    context = {}

    for channel in range(1, 7):

        status = subprocess.call('sudo /var/www/html/relay/models.py -c %s -S 1' % channel, shell="True")

        channels.append(DummyRelay(channel, '%s' % channels_info[str(channel)][0], status))

    # Sort the list with the channel attribute of the Relay class
    channels = sorted(channels, key=lambda channel: channel.channel)

    context['channels'] = channels

    return render_to_response('multitask/index.html', context, context_instance=RequestContext(request))


def toggle_channel_async(request, channel_number='1'):
    regx = re.compile(r'\b[1-8]{1}\b')

    if request.method == 'GET':

        if not regx.match(channel_number):
            raise Http404

        status = subprocess.call('sudo /var/www/html/relay/models.py -c %s -s %s -t 1' % (channel_number, 0),
                                 shell="True")

        context = {'channel': channel_number, 'status': True if status == 0 else False}

        return HttpResponse(json.dumps(context), mimetype="application/json")

    raise Http404


def toggle_channel_sync(request, channel_number='1'):
    regx = re.compile(r'\b[1-8]{1}\b')

    if request.method == 'GET':

        if not regx.match(channel_number):
            raise Http404

        channel = Relay(int(channel_number), "")

        channel.toggle()

        return redirect('/apikeys/')

    raise Http404

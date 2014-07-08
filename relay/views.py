import re

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.http import Http404

from relay.models import Relay


# Create your views here.


def index(request):
    """
        Index of the system
    """
    channels = []

    context = {}

    for channel in range(1, 9):
        channels.append(Relay(channel, 'Channel%s' % channel))

    # Sort the list with the channel attribute of the Relay class
    channels = sorted(channels, key=lambda channel: channel.channel)

    context['channels'] = channels

    return render_to_response('multitask/index.html', context, context_instance=RequestContext(request))


def turns_on_channel(request, channel_number='1'):
    regx = re.compile(r'\b[1-8]{1}\b')

    if request.method == 'GET':

        if not regx.match(channel_number):
            raise Http404

        channel = Relay(int(channel_number), "")

        channel.toggle()

        return redirect('/apikeys/')

    raise Http404

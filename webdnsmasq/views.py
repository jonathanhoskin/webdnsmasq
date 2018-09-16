# webdnsmasq - web interface for dnsmasq
# Copyright (C) 2015 Tim Jungnickel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
import os
import collections

# all hosts will be resolved by the DNS server behind the stated IP
# pleas read the dnsmasq man page for /server entry
servers = [
    ('Facebook', {
        'domains': [ 'facebook.com', 'facebook.net', 'fbcdn.com', 'fbcdn.net' ],
        'blocked': False,
    }),
    ('Google', {
        'domains': [ 'google.com', 'google.co.nz' ],
        'blocked': False,
        'icon': 'https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg'
    }),
    ('Instagram', {
        'domains': [ 'instagram.com' ],
        'blocked': False,
    }),
    ('Snapchat', {
        'domains': [ 'snapchat.com', 'appspot.com' ],
        'blocked': False,
        'icon': 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Snapchat_logo.svg/300px-Snapchat_logo.svg.png'
    }),
    ('Spotify', {
        'domains': [ 'spotify.com' ],
        'blocked': False
    }),
    ('Youtube', {
        'domains': [ 'youtube.com' ],
        'blocked': False,
        'icon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/YouTube_social_red_squircle_%282017%29.svg/300px-YouTube_social_red_squircle_%282017%29.svg.png'
    }),
    ('Netflix', {
        'domains': [ 'netflix.com' ],
        'blocked': False
    }),
    ('Fortnite', {
        'domains': [ 'epicgames.com' ],
        'blocked': True,
        'icon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Fortnite.png/320px-Fortnite.png'
    }),
    ('Sims, FIFA, EA, Origin', {
        'domains': [ 'ea.com', 'origin.com' ],
        'blocked': True,
        'icon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Electronic-Arts-Logo.svg/240px-Electronic-Arts-Logo.svg.png'
    }),
    ('Roblox', {
        'domains': [ 'roblox.com' ],
        'blocked': True,
        'icon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Roblox_logo.svg/320px-Roblox_logo.svg.png'
    }),
    ('Slither.io', {
        'domains': [ 'slither.io' ],
        'blocked': True,
        'icon': 'https://upload.wikimedia.org/wikipedia/en/5/50/Slither.png'
    }),
    ('Diep.io', {
        'domains': [ 'diep.io' ],
        'blocked': True
    }),
    ('Kizi', {
        'domains': [ 'kizi.com' ],
        'blocked': True
    }),
    ('Friv', {
        'domains': [ 'friv.com' ],
        'blocked': True
    }),
]

serversDict = collections.OrderedDict(servers)

@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    return {'project': 'webdnsmasq',
            'servers': serversDict}

# View for save - no site will be generated
@view_config(route_name='save')
def save_view(request):
    global serversDict

    file = open('webdnsmasq-blocked.conf','w')

    for param in serversDict:
        if param in request.params:
            serversDict[param]['blocked'] = True
            for domain in serversDict[param]['domains']:
                file.write('server=/' + domain + "/\n")
        else:
            serversDict[param]['blocked'] = False

    file.close()
    notifyDnsmasq()

    if request.is_xhr:
        return Response()
    else:
        return HTTPFound(location='/')

def notifyDnsmasq():
    fifo = open('../../reloader.fifo','w')
    fifo.write("changed list\n")
    fifo.close()

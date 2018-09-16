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
from pyramid.httpexceptions import HTTPFound
import os
import collections

# all hosts will be resolved by the DNS server behind the stated IP
# pleas read the dnsmasq man page for /server entry
servers = [
    ('Facebook', {
        'domains': [ 'facebook.com', 'fbcdn.com' ],
        'blocked': False
    }),
    ('Google', {
        'domains': [ 'google.com' ],
        'blocked': False
    }),
    ('Instagram', {
        'domains': [ 'instagram.com' ],
        'blocked': False
    }),
    ('Snapchat', {
        'domains': [ 'snapchat.com', 'appspot.com' ],
        'blocked': False
    }),
    ('Spotify', {
        'domains': [ 'spotify.com' ],
        'blocked': False
    }),
    ('Youtube', {
        'domains': [ 'youtube.com' ],
        'blocked': False
    }),
    ('Netflix', {
        'domains': [ 'netflix.com' ],
        'blocked': False
    }),
    ('Fortnite', {
        'domains': [ 'epicgames.com' ],
        'blocked': True
    }),
    ('Sims, FIFA, EA, Origin', {
        'domains': [ 'ea.com', 'origin.com' ],
        'blocked': True
    }),
    ('Roblox', {
        'domains': [ 'roblox.com' ],
        'blocked': True
    }),
    ('Slither.io', {
        'domains': [ 'slither.io' ],
        'blocked': True
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
            for domain in serversDict[param]['domains']
                file.write('server=/' + domain + "/\n")
        else:
            serversDict[param]['blocked'] = False

    file.close()
    notifyDnsmasq()
    return HTTPFound(location='/')

def notifyDnsmasq():
    fifo = open('../../reloader.fifo','w')
    fifo.write("changed list\n")
    fifo.close()

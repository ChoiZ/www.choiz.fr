#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fran\xe7ois LASSERRE'
SITENAME = u'ChoiZ'
SITEURL = u'http://localhost:8000'
SITETITLE = u'Blog de François LASSERRE'
SITESUBTITLE = 'Je suis ingénieur informaticien, j\'aime le développement, le streaming, l\'Internet…<br><br>Depuis l\'an 2000, j\'ai fondé plusieurs webradios (Radio-Psylone, Live9 ou encore AddictRadio).<br>Je fais parti de l\'équipe de <a href="http://www.lagrosseradio.com">La Grosse Radio</a>.'
SITELOGO = u'avatar.png'

FAVICON = SITEURL + '/favicon.ico'
ROBOTS = 'index, follow'

# top menu
MAIN_MENU = False

PATH = 'content'

TIMEZONE = 'Europe/Paris'
THEME = 'Flexfork'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
         ('Home', '/'),
         ('Archives', '/archives'),
         ('Tags', '/tags'),
        )
         #('Pelican', 'http://getpelican.com/'),
         #('La Grosse Radio', 'http://www.lagrosseradio.com/'),

# Social widget
SOCIAL = (
          ('github', '//www.github.com/ChoiZ'),
          ('flickr', '//www.flickr.com/ChoiZ'),
          ('lastfm', '//www.last.fm/user/ChoiZ'),
          ('twitter', '//www.twitter.com/ChoiZ'),
          ('facebook', '//www.facebook.com/ChoiZ'),
          ('foursquare', '//www.foursquare.com/ChoiZ'),
          ('linkedin', '//www.linkedin.com/in/ChoiZ'),
         )

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'extra/avatar.png',
    'extra/README',
    ]

EXTRA_PATH_METADATA = {
    'extra/avatar.png': {'path': 'avatar.png'},
    'extra/README': {'path': 'README.md'},
    }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

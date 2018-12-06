#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Fran\xe7ois LASSERRE'
SITENAME = u'ChoiZ'
SITEURL = u'//www.choiz.fr'
SITETITLE = u'Blog technique de François LASSERRE'
SITESUBTITLE = 'Je suis ingénieur informatique, je travail en tant que DevOps chez <a href="//www.manomano.fr">ManoMano</a>. J\'aime le développement, le streaming, l\'Internet…<br><br>Depuis l\'an 2000, j\'ai fondé plusieurs webradios Radio-Psylone, Live9 ou encore AddictRadio. J\'aide actuellement l\'association <a href="https://www.frequence3.fr">Fréquence 3</a>'
#SITELOGO = u'avatar.png'

GITHUB_URL = 'https://github.com/choiz/choiz.github.io/tree/pelican'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

FAVICON = 'favicon.ico'
ROBOTS = 'index, follow'

# top menu
MAIN_MENU = False

PLUGINS = []#['post_revision']
PATH = 'content'

TIMEZONE = 'Europe/Paris'
THEME = 'Flexfork'

DEFAULT_LANG = u'fr'

PIWIK_URL = 'stats.rocketip.net'
PIWIK_SITE_ID = '7042kjNK6PYV9LoGM5np'

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
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/README'
    ]

EXTRA_PATH_METADATA = {
    'extra/avatar.png': {'path': 'avatar.png'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/README': {'path': 'README.md'},
    }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fran\xe7ois LASSERRE'
SITENAME = u'ChoiZ'
SITEURL = u'http://localhost:8000/'
SITETITLE = ''
SITESUBTITLE = 'Je suis Français, ingénieur informatique, j\'aime le développement web, les logiciels libres et l\'informatique.'
SITESUBTITLE2 = 'J\'ai fondé plusieurs webradios depuis l\'an 2000, actuellement je fais parti de l\'équipe de <a href="http://www.lagrosseradio.com">La Grosse Radio</a>.'
SITELOGO = u'http://33.media.tumblr.com/avatar_93efe3b6ac00_128.png'

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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

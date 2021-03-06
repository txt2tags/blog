#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Aurelio Jargas'
SITENAME = u'txt2tags blog'
SITEURL = ''

PATH = 'content'

THEME = 'relapse'

PLUGINS = ['txt2tags_reader']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Website', 'https://txt2tags.org'),
         ('Download', 'https://txt2tags.org/download'),
         ('GitHub', 'https://github.com/txt2tags'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/txt2tags'),
          ('Telegram', 'https://www.t.me/txt2tags'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matthieu Keller'
SITENAME = "maggick's logs"
SITEURL = '/blog'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/maggick'),
        ('Twitter', 'https://twitter.com/matthieukeller'),
        ('Linked In', 'https://linkedin.com/in/matthieukeller')
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/maggick/Documents/pelican-themes/bootstrap"

# Following items are often useful when publishing
DISQUS_SITENAME = "matthieukeller"
#GOOGLE_ANALYTICS = ""

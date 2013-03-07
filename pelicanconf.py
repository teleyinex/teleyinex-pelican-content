#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Daniel Lombraña González"
SITENAME = u"Daniel Lombraña González"
SITEURL = 'http://daniellombrana.es'
GOOGLE_ANALYTICS = 'UA-36769710-1'
TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

RELATIVE_URLS = True

THEME = 'basic'

NEWEST_FIRST_ARCHIVES = True

BIBTEX_FILE = 'bib/daniel-lombrana.bib'

PLUGINS = ['pelican.plugins.bibtex']

GOOGLE_AUTHOR = 'https://plus.google.com/105984938874365438913'

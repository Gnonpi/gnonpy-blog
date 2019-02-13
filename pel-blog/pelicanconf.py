#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from pathlib import Path

AUTHOR = 'Denis Viviès'
SITENAME = 'Gnonpy'
SITESUBTITLE = 'Step by step into software'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Theme related
theme_path = Path(__file__).parent.joinpath('themes/clean-blog')
THEME = str(theme_path)
HEADER_COVER = 'theme/images/home-bg-madrid-rebe-pascual-unsplash-cropped-darken.jpg'
STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/home-bg.jpg': {'path': 'home-bg-madrid-rebe-pascual-unsplash.jpg'}
}
FAVICON = 'favicon.ico'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github projects', 'https://github.com/Gnonpi/'),
         ('My current company', 'https://www.geoblink.com/'))

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/denis-vivi%C3%A8s-python/'),
         ('github', 'https://github.com/Gnonpi'),
         ('envelope', 'mailto:legnonpi@gmail.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DEFAULT_METADATA = {
    'status': 'draft'
}

# Plugins

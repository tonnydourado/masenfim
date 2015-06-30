#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colombiano'
TWITTER_USERNAME = 'tonnydourado'
SITENAME = u'Mas, Enfim.'
SITEURL = '/'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt-br'

DELETE_OUTPUT_DIRECTORY = True
AUTORELOAD_IGNORE_CACHE = True

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('Tags', 'tags.html'), ('Arquivos', 'archives.html'),)

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = ''
DISPLAY_CATEGORIES_ON_MENU = False

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 1000

THEME = 'themes/cait'

PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = ['assets']

# Assets and themes
WEBASSETS = True
THEME = './themes/cait'
# THEME = './themes/svbtle'
# THEME = './themes/pelican-sober'
# THEME = './themes/pelican-simplegrey'
# THEME = './themes/pelican-mockingbird'  # Interesting
# THEME = './themes/chunk'  # Also interesting
# THEME = './themes/iris'   # de repente dá pra arrumar ...
THEME = './themes/storm'  # promete tb
ASSET_SOURCE_PATHS = ['static']
ASSETS_RELATIVE = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

DISQUS_SITENAME = 'masenfim'
GOOGLE_ANALYTICS = 'UA-58308556-1'

SITEURL = 'masenf.im'
RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

FEED_ALL_ATOM = 'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Do not process drafts when generating the site for publication:
ARTICLE_EXCLUDES = ["drafts"]

#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @formatter:off
#
#                                             ,,
#                                             db
#     \
#     _\,,          `7MM  `7MM  `7MMpMMMb.  `7MM  ,p6"bo   ,pW"Wq.`7Mb,od8 `7MMpMMMb.
#    "-=\~     _      MM    MM    MM    MM    MM 6M'  OO  6W'   `Wb MM' "'   MM    MM
#       \\~___( ~     MM    MM    MM    MM    MM 8M       8M     M8 MM       MM    MM
#      _|/---\\_      MM    MM    MM    MM    MM 8M       8M     M8 MM       MM    MM
#     \        \      MM    MM    MM    MM    MM YM.    , YA.   ,A9 MM       MM    MM
#                     `Mbod"YML..JMML  JMML..JMML.YMbmd'   `Ybmd9'.JMML.   .JMML  JMML.
#
#                     written with <3 by Micha Grandel, talk@michagrandel.com
#                     
#                     Project:         https://github.com/michagrandel/BackUpApi
#                     Report a bug:    https://github.com/michagrandel/BackUpApi/issues
#                     Contribute:      https://github.com/michagrandel/BackUpApi/wiki/Contribute
#                     
#                     Facebook:        https://me.me/micha.animator
#                     Instagram:       @michagrandel
#                     -----------------------------------------------------------------
#                     
#                     Licensed under the Apache License, Version 2.0 (the 'License');
#                     you may not use this file except in compliance with the License.
#                     You may obtain a copy of the License at
#                     
#                     http://www.apache.org/licenses/LICENSE-2.0
#                     
#                     Unless required by applicable law or agreed to in writing,
#                     software distributed under the License is distributed on an
#                     'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
#                     either express or implied. See the License for the specific
#                     language governing permissions and limitations under the License.
#                     -----------------------------------------------------------------
#                     @formatter:on

"""
:mod:`Backup.py` -- Backup data from local machine to a server API

.. module:: Backup.py
   :platform: Unix, Windows
   :synopsis: Describe your module in one sentence
.. moduleauthor:: Micha Grandel <talk@michagrandel.de>
"""

from __future__ import unicode_literals, print_function
from io import open
import six
import sys
import os
import platform
import json
from jinja2 import Environment, PackageLoader, select_autoescape

from flask import Flask
from flup.server.fcgi import WSGIServer

__status__ = 'development'
__author__ = 'Micha Grandel'
__version__ = '0.1.0'
__copyright__ = 'written with <3 by Micha Grandel'
__license__ = 'Apache License, Version 2.0'
__contact__ = 'http://github.com/michagrandel'


if 'uberspace' in platform.node.lower():
    UBERSPACE = True
    if os.path.expanduser('~/bin') not in sys.path:
        sys.path.append(os.path.expanduser('~/bin'))

apiv01 = Flask(__name__)


@apiv01.route('/')
def hello():
    """ just a simple hello world to test server configuration """
    return '<em>Hello World!</em>'


@apiv01.route('/hello')
def hello():
    """ just a simple hello world to test server configuration """
    return '<em>Hello World!</em>'


@apiv01.route('/version')
def version():
    """ returns API version in json format"""
    version = __version__.split('.')
    return json.dumps({
        'version':__version__,
        'major': version[0],
        'minor': version[1] if len(version) > 1 else '0',
        'release': version[2] if len(version) > 2 else '0'
    })


@apiv01.route('/about')
def about():
    """ returns information about the API """
    return json.dumps({'version':__version__})


def main():
    """ run API as WSGI Server Application """
    if 'uberspace' in platform.node.lower():
        WSGIServer(apiv01).run()


if __name__ == '__main__':
    main()

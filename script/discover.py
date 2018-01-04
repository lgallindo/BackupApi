#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @formatter:off
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
# @formatter:on

""" Discover and run unit tests """

from unittest import TestLoader, TextTestRunner

__status__ = 'development'
__author__ = 'Micha Grandel'
__version__ = '0.1.0'
__copyright__ = 'written with <3 by Micha Grandel'
__license__ = 'Apache License, Version 2.0'
__contact__ = 'http://github.com/michagrandel'

if __name__ == '__main__':
    test_suite = TestLoader().discover('test')
    TextTestRunner(verbosity=2).run(test_suite)

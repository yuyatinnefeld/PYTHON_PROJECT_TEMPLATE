#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
---------------------------------------------
# PYTHON TEMPLATE
# (C) 2021 Yuya Tinnefeld, Düsseldorf, Germany
# email: yuyatinnefeld@gmail.com
---------------------------------------------
"""

import sys
import os

cwd = os.getcwd()
dir_over = os.path.dirname(cwd)
sys.path.insert(1, f'{dir_over}/conf/')
from sample_api import sampleAPIClass

api = sampleAPIClass()
get_key = api.key
get_secret = api.secret

print(f'🐍 key: {get_key}')
print(f'🐍 secret: {get_secret}')
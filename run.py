# -*- coding: utf-8 -*-
'''
Created on:    Apr 18, 2014
@author:        vahid
'''

from cherryblog import start

import sys
import argparse
import os.path
thisdir = os.path.dirname(__file__)
config_path = os.path.abspath(os.path.join(thisdir,'development.conf'))
parser = argparse.ArgumentParser(description='Simple blogging system, using cherrypy')

parser.add_argument('-c','--config-file', dest='config_files', nargs='?', action='append', default=[config_path],help='YAML configuration file')

if __name__ == '__main__':
    args = parser.parse_args()
    start(config_files=args.config_files)
    sys.exit(0)

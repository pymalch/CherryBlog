# -*- coding: utf-8 -*-
'''
Created on:    Apr 18, 2014
@author:        vahid
'''
from cherrypy import expose, tools

class Root(object):

    @expose
    @tools.mako(filename='index.mak')
    def index(self):
        return dict(page_title='CherryBlog')


# -*- coding: utf-8 -*-
'''
Created on:    Apr 18, 2014
@author:        pymalch
'''
from cherrypy import expose, tools, request, HTTPRedirect
from cherryblog.models import Post
import cherrypy

SESSION_KEY = '_cp_username'


class Root(object):
    def check_access(func):
        def decorate(*args,**kwargs):
            if not cherrypy.session.get(SESSION_KEY):
                raise HTTPRedirect('/?NotAuthorisedAction')
            else:
                return func(*args,**kwargs)

        return decorate

    @expose
    @tools.mako(filename='index.mak')
    def index(self):
        posts = request.db.query(Post).all()
        return dict(page_title='CherryBlog', posts=posts)

    @expose
    def doLogin(self, username=None, password=None):

        if username in ('admin', 'administrator') and password == 'admin':
            cherrypy.session[SESSION_KEY] = cherrypy.request.login = username
        else:
            cherrypy.session['MESSAGE'] = u"Incorrect username or password."

        raise HTTPRedirect("/")

    @expose
    def doLogout(self):
        cherrypy.session[SESSION_KEY] = cherrypy.request.login = None
        raise HTTPRedirect("/")

    @expose
    @check_access
    def add(self, **kwargs):

        if kwargs['title'] == None or kwargs['content'] == None:
            cherrypy.session['MESSAGE']= u"Please Fill All Post Fields!"
            raise HTTPRedirect('/')

        blog = Post(title=kwargs['title'], content=kwargs['content'])
        request.db.add(blog)

        raise HTTPRedirect("/")


    @expose
    @check_access
    def delete(self, *args):

        if args == None:
            raise HTTPRedirect('/?message=Please specify an id! ')

        request.db.query(Post).filter_by(id=args[0]).delete()

        raise HTTPRedirect("/")



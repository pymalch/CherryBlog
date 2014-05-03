# -*- coding: utf-8 -*-
'''
Created on:    Apr 18, 2014
@author:        vahid
'''
from cherrypy import expose, tools, request, HTTPRedirect
from cherryblog.tools.sqlalchemy_tool import SATool
from cherryblog.models import Post
import cherrypy

SESSION_KEY = '_cp_username'





class Root(object):
    message = ''


    def check_access(func):
        def decorate(*args):
            if not cherrypy.session.get(SESSION_KEY):
                raise HTTPRedirect('/?dddd')
            else:
                return func( *args)
        return decorate

    @expose
    @tools.mako(filename='index.mak')
    def index(self, **args):
        posts = request.db.query(Post).all()
        if 'message' in args:
            self.message = args['message']
        return dict(page_title='CherryBlog', posts=posts, message=self.message)

    @expose
    def doLogin(self, username=None, password=None):

        error_msg = check_credentials(username, password)
        if error_msg:
            raise HTTPRedirect('/?message=%s ' % (error_msg))

        else:
            #regenerate()
            cherrypy.session[SESSION_KEY] = cherrypy.request.login = username
            raise HTTPRedirect("/")

    @expose
    def doLogout(self):
        cherrypy.session[SESSION_KEY] = cherrypy.request.login = None
        raise HTTPRedirect("/")

    @expose
    @check_access
    def add(self, **kwargs):

        if kwargs['title'] == None or kwargs['content'] == None:
            raise HTTPRedirect('/?message=Please Fill All Post Fields! ')

        blog = Post(title=kwargs['title'], content=kwargs['content'])
        request.db.add(blog)

        raise HTTPRedirect("/")


    @expose
    @check_access
    def delete(self, *args):

        if args == None:
            raise HTTPRedirect('/?message=Please specify an id! ')

        request.db.query(Post).filter_by(id =args[0]).delete()

        raise HTTPRedirect("/")

def check_credentials(username, password):
    if username is None or password is None:
        return u"Error: Username or Password is not filled!"

    elif username in ('admin', 'administrator') and password == '123':
        return None
    else:
        return u"Incorrect username or password."


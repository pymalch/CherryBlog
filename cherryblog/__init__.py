

__version__ = '0.1.0'
import cherrypy as cp
import os.path
from pymlconf import ConfigManager
import CherrypyMako
import CherrypyElixir
root_dir = os.path.abspath(os.path.dirname(__file__))

__default_config = """
db_uri: sqlite:///../data/cherryblog.db
"""


def start(config_files=None):
    global config

    # Preparing config
    config= ConfigManager(__default_config,files=config_files)


    # Setting up cherrypy tools
    CherrypyMako.setup()
    from cherryblog.plugins.sqlalchemy_plugin import  SAEnginePlugin
    from cherryblog.tools.sqlalchemy_tool import  SATool
    SAEnginePlugin(cp.engine).subscribe()
    cp.tools.db = SATool()

    # Importing models and controllers
    from cherryblog.controllers import Root
    from cherryblog.models import Post


    # Configuring cherrypy
    cp_config = {'global': {
        'tools.mako.directories': [os.path.join(root_dir,'views')],
        'tools.staticdir.root':  root_dir,
        'tools.db.on'    : True,
        'tools.sessions.on' : True,
        'tools.sessions.storage_type' : 'ram',
        #'tools.sessions.storage_path' : 'sessionsPath',
        'tools.sessions.timeout' : 60 ,
       },'/public': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir':  'public'
       }
    }

    # Starting the server
    cp.quickstart(Root(),'',config=cp_config)

__all__ = ['start','__version__']
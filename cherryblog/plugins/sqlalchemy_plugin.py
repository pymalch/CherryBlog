__author__ = 'pylover'


from cherrypy.process import wspbus, plugins
from sqlalchemy import create_engine
import os
from cherryblog.models import  BaseModel

class SAEnginePlugin(plugins.SimplePlugin):
    def __init__(self, bus):
        """
        The plugin is registered to the CherryPy engine and therefore
        is part of the bus (the engine *is* a bus) registery.

        We use this plugin to create the SA engine. At the same time,
        when the plugin starts we create the tables into the database
        using the mapped class of the global metadata.




        Finally we create a new 'bind' channel that the SA tool
        will use to map a session to the SA engine at request time.
        """
        plugins.SimplePlugin.__init__(self, bus)
        self.sa_engine = None
        self.bus.subscribe("bind", self.bind)

    def start(self):
        db_path = os.path.abspath(os.path.join(os.curdir, '..','data'))
        from cherryblog import config
        self.sa_engine = create_engine(config.db_uri, echo=True)
        BaseModel.metadata.create_all(self.sa_engine)

    def stop(self):
        if self.sa_engine:
            self.sa_engine.dispose()
            self.sa_engine = None

    def bind(self, session):
        session.configure(bind=self.sa_engine)

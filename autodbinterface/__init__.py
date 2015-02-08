# -*- coding: utf-8 -*-
__version__ = '0.1.0'

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


class AutoDataface:
    def __init__(self, engine_url):
        self.engine = create_engine(engine_url)
        self.Base = automap_base()
        self.Base.prepare(self.engine, reflect=True)
        self.session = Session(self.engine)
        self.query = self.session.query
        for name, table in self.Base.classes.items():
            setattr(self, name, table)
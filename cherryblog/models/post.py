# -*- coding: utf-8 -*-
'''
Created on:    Apr 18, 2014
@author:        vahid
'''


from sqlalchemy import Column
from sqlalchemy.types import Unicode, Integer, Text, DateTime
from cherryblog.models import BaseModel
from datetime import datetime
from sqlalchemy.schema import Sequence


class Post(BaseModel):
    __tablename__ = 'post'
    id = Column(Integer, Sequence('post_id_seq') ,primary_key=True)
    title = Column(Unicode(500),nullable=False,index=True)
    content = Column(Text)
    entry_time = Column(DateTime,nullable=False,default=datetime.now)

# -*- coding: utf-8 -*-
'''
Created on:    Apr 18, 2014
@author:        vahid
'''


from elixir import Entity, Field, Text, Unicode, DateTime, OneToMany

class Post(Entity):
    title = Field(Unicode(500),required=True,index=True)
    content = Field(Text)
    entry_time = Field(DateTime,required=True),
    keywords = ManyToMany( Keyword )

Class Keyword():
    title


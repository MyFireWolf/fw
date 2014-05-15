#!/usr/bin/python
#coding: utf-8
from sqlalchemy import *
from sqlalchemy.orm import *
engine=create_engine("sqlite:///test.db",echo=True)
metadate=MetaData(engine)
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
	""" Performs database connection using settings.py
	Returns sqlalchemy engine from instace 
	"""
	#return create_engine(URL(**settings.DATABASE))
	return create_engine('mysql+pymysql://root:root@localhost:3306/scrape?charset=utf8',convert_unicode=True)

def create_cyclone_table(engine):
	DeclarativeBase.metadata.create_all(engine)


class Cyclones(DeclarativeBase):
	"""Sqlalchemy cyclone models"""
	__tablename__="cyclones"

	id = Column(Integer, primary_key=True)
	title = Column('title', String(64000))
	link = Column('link', String(64000), nullable=True)
	location = Column('location', String(64000), nullable=True)
	forecast = Column('forecast', String(64000), nullable=True)
	history = Column('history', String(64000), nullable=True)


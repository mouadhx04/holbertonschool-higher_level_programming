#!/usr/bin/python3
""" class definition of State in Base"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(
        'id',
        Integer,
        unique=True,
        nullable=False,
        primary_key=True)
    name = Column(
        'name',
        String(128),
        nullable=False)

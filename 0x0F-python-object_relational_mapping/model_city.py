#!/usr/bin/python3
""" class definition of State in Base"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from model_state import Base


class City(Base):
    __tablename__ = 'cities'
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
    state_id = Column(
        'state_id',
        Integer,
        ForeignKey('states.id'),
        nullable=False)

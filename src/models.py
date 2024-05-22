import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    nombre = Column(String)
    apellido = Column(String)
    fecha_subscripcion = Column(DateTime, default=datetime.utcnow)
    favoritos = relationship('Favorito', back_populates='usuario')

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    clima = Column(String)
    personajes = relationship('Personaje', back_populates='planeta')

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    altura = Column(Integer)
    peso = Column(Integer)
    genero = Column(String)
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    planeta = relationship('Planeta', back_populates='personajes')

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    usuario = relationship('Usuario', back_populates='favoritos')
    planeta = relationship('Planeta')
    personaje = relationship('Personaje')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

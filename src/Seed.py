 #_ ❤__________________OMR________________________________________________ ❤

from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, declarative_base

# ❤_________________________________________________________________________ ❤

Base = declarative_base()

class Semente(Base):
    __tablename__ = 'tbl_semente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(90), nullable=False)
    quantidade_agua_por_regada = Column(String(60), nullable=False)
    regadas_por_semana = Column(String(60), nullable=False)
    tempo_cultivo = Column(Integer, nullable=False)
    recomendacoes = Column(Text, nullable=False)
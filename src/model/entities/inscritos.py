from src.model.configs.base import Base
from sqlalchemy import Column,String,Integer,ForeignKey
from .eventos import Eventos #Mostra pra classe Subscriber que a classe Eventos também existe Método 1 (permite relaciona-los)

class Inscritos(Base):
  __tablename__ = "Inscritos"

  id = Column(Integer,primary_key=True,autoincrement=True)
  nome = Column(String,nullable=False)
  email = Column(String,nullable=False)
  link = Column(String, nullable=True)
  evento_id = Column(Integer,ForeignKey("Eventos.id"))  #ID do evento é relacionado com o de inscrito 
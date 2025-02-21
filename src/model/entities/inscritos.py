from src.model.configs.base import Base
from sqlalchemy import column,String,Integer,ForeignKey

class Inscritos(Base):
  __tablename__ = "Inscritos"

id = column(Integer,primary_key=True,autoincrement=True)
nome = column(String,nullable=False)
email = column(String,nullable=False)
link = column(String, nullable=True)
event_id = column(Integer,ForeignKey("Eventos.id"))  #ID do evento é relacionado com o de inscrito 
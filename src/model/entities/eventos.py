from src.model.configs.base import Base
from sqlalchemy import column,String, Integer
class Eventos(Base):
  __tablename__ = "Eventos"

  id = column(Integer,primary_key=True, autoincrement=True)
  nome = column(String,nullable=False) 
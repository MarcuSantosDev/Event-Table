from src.model.configs.connection import DBConnectionHandler #Conexão com o banco
from src.model.entities.eventos import Eventos #Entidade de eventos
from .interfaces.eventos_repository import EventosRepositoryInterface


class EventosRepository(EventosRepositoryInterface):
  #Adicionar no Banco de Dados
  def insert(self,event_name: str)-> None: 
    with DBConnectionHandler() as db:
      try:
        new_event = Eventos(nome=event_name)
        db.session.add(new_event) #Adiciona a seção um novo evento
        db.session.commit()
      except:  
        db.session.rollback() #Volta o banco para o estado anterior
        raise Exception #Levanta a exceção
      
  #Buscar no Banco de Dados
  def select_event(self,event_name:str)-> Eventos: 
    with DBConnectionHandler() as db:
      data = (
        db.session
        .query(Eventos)
        .filter(Eventos.nome == event_name)
        .one_or_none()
      )
      return data
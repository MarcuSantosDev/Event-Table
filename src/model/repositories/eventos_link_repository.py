import random #gerador de números aleatórios
from src.model.configs.connection import DBConnectionHandler #Conexão com o banco
from src.model.entities.eventos_link import EventosLink #Entidade de eventos link
from src.model.repositories.interfaces.eventos_link_repository import EventosLinkRepositoryInterface


class EventosLinkRepository(EventosLinkRepositoryInterface
):
  #Adicionar no Banco de Dados
  def insert(self,event_id:int, subscriber_id:int)-> str: 
    with DBConnectionHandler() as db:
      try:
        link_final = ''.join(random.choices('0123456789', k=7)) #Link aleatório
        formatted_link = f'evento-{event_id}-{subscriber_id}-{link_final}'

        new_events_link = EventosLink(
            evento_id=event_id,
            inscrito_id=subscriber_id,
            link= formatted_link
            )
        db.session.add(new_events_link) #Adiciona a seção um novo evento
        db.session.commit()
        return formatted_link
      except:  
        db.session.rollback() #Volta o banco para o estado anterior
        raise Exception #Levanta a exceção
      
  #Buscar no Banco de Dados
  def select_events_link(self,event_id:int, subscriber_id:int)-> EventosLink: 
    with DBConnectionHandler() as db:
      data = (
        db.session
        .query(EventosLink)
        .filter(EventosLink.evento_id == event_id,
                EventosLink.inscrito_id == subscriber_id)
        .one_or_none()
      )
      return data
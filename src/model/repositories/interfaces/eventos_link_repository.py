from abc import ABC, abstractmethod
import random #gerador de números aleatórios
from src.model.configs.connection import DBConnectionHandler #Conexão com o banco
from src.model.entities.eventos_link import EventosLink #Entidade de eventos link
 

   
class EventosLinkRepositoryInterface(ABC):
  #Adicionar no Banco de Dados
  @abstractmethod
  def insert(self,event_id:int, subscriber_id:int)-> str: 
    pass

  @abstractmethod 
  #Buscar no Banco de Dados
  def select_events_link(self,event_id:int, subscriber_id:int)-> EventosLink: 
     pass
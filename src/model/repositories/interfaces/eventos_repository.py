from abc import ABC, abstractmethod
from src.model.entities.eventos import Eventos #Entidade de eventos

class EventosRepositoryInterface(ABC):
   
   @abstractmethod # Se passar a classe como herança, a classe que esta recebendo obrigatoriamente tem que implentar insert (tipagem)
   def insert(self,event_name: str)-> None: 
     pass
  
  # Se passar a classe como herança, a classe que esta recebendo obrigatoriamente tem que implentar insert (tipagem)
   @abstractmethod
   def select_event(self,event_name:str)-> Eventos: 
      pass
from abc import ABC, abstractmethod
from src.model.entities.inscritos import Inscritos #Entidade de eventos
 
class SubscribersRepositoryInterface(ABC):
  #Adicionar no Banco de Dados
  @abstractmethod
  def insert(self,subscriber_infos: dict)-> None: 
    pass
  
  @abstractmethod
  def select_subscriber(self,email:str, evento_id:int)-> Inscritos: 
    pass
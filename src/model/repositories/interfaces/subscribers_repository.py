from abc import ABC, abstractmethod
from src.model.entities.inscritos import Inscritos #Entidade de eventos
 
class SubscribersRepositoryInterface(ABC):
  #Adicionar no Banco de Dados
  @abstractmethod  # Se passar a classe como herança, a classe que esta recebendo obrigatoriamente tem que implentar insert (tipagem)
  def insert(self,subscriber_infos: dict)-> None: 
    pass
  
  @abstractmethod # Se passar a classe como herança, a classe que esta recebendo obrigatoriamente tem que implentar insert (tipagem)
  def select_subscriber(self,email:str, evento_id:int)-> Inscritos: 
    pass
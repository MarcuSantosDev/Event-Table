from src.model.configs.connection import DBConnectionHandler #Conexão com o banco
from src.model.entities.inscritos import Inscritos #Entidade de eventos
from .interfaces.subscribers_repository import SubscribersRepositoryInterface
 
class SubscribersRepository(SubscribersRepositoryInterface):
  #Adicionar no Banco de Dados
  def insert(self,subscriber_infos: dict)-> None: 
    with DBConnectionHandler() as db:
      try:
        new_subscriber = Inscritos(
          nome=subscriber_infos.get("name"),
          email=subscriber_infos.get("email"),
          link=subscriber_infos.get("link"),
          evento_id=subscriber_infos.get("evento_id"),
          )
        db.session.add(new_subscriber) #Adiciona a seção um novo evento
        db.session.commit()
      except:  
        db.session.rollback() #Volta o banco para o estado anterior
        raise Exception #Levanta a exceção
  
  def select_subscriber(self,email:str, evento_id:int)-> Inscritos: 
    with DBConnectionHandler() as db:
      data = (
        db.session
        .query(Inscritos)
        .filter(Inscritos.email == email, Inscritos.evento_id == evento_id)
        .one_or_none()
      ) 
      return data
 
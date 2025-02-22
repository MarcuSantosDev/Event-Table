from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker #sessão de banco de dados

class DBConnectionHandler: # gerenciar a conexão com o banco de dados.
  def __init__(self):
    self.__connection_string= "sqlite:///schema.db"
    self.__engine = self.__create_database_engine()
    self.session = None #Começar com uma sessão vazia

  def __create_database_engine(self):
    engine = create_engine(self.__connection_string)
    return  engine
 
  def __enter__(self):
    session_make = sessionmaker(bind=self.__engine)
    self.session = session_make() #Ao entrar a sessão irá mudar
    return self #Retorna todo o contexto da classe
  
  def __exit__(self,exc_type, exc_val, exc_tb): 
    self.session.close() #Ao sair a sessão irá fechar
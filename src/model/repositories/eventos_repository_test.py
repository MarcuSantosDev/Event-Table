import pytest
from .eventos_repository import EventosRepository
#Para rodar o pytest basta digitar no terminal: pytest -s -v "caminho do directório" do arquivo
@pytest.mark.skip("Insert in DB") #Faz um marcador que pula o teste
def test_insert_eventos():
  event_name = "eventoTeste2"
  event_repo = EventosRepository()

  event_repo.insert(event_name)


@pytest.mark.skip("select in DB") 


# Teste de busca de um evento no banco de dados
def test_select_event():
  event_name = "eventoTeste2"
  event_repo = EventosRepository()

  event = event_repo.select_event(event_name)
  print(event) #memória que armazena o evento
  print(event.nome) #Nome do evento 
  print(event.id)
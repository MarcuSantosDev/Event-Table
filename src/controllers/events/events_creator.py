from src.model.repositories.interfaces.eventos_repository import EventosRepositoryInterface
from src.http_types.http_request import HttpRequest 
from src.http_types.http_response import HttpResponse
class EventsCreator:
  def __init__ (self,events_repo: EventosRepositoryInterface):
    self.__events_repo = events_repo
  
  def create(self,http_request:HttpRequest) -> HttpResponse:
    events_info = http_request.body["data"]
    event_name = events_info["name"]

    self.__check_event(event_name) #Verifica se houve um evento com o mesmo nome
    self.__insert_event(event_name) #Insere um novo evento
    return self.__format_response(event_name)

  def  __check_event(self,event_name:str) -> None:
    response = self.__events_repo.select_event(event_name) #Verifica se há um evento com um mesmo nome
    if response: raise Exception("Event Already exist !")

  
  def __insert_event(self,event_name:str) -> None:
    self.__events_repo.insert(event_name) #Insere um novo evento

  def __format_response(self,event_name:str) -> HttpResponse: #Traduz a resposta do EventsCreator para um HttpResponse

    return HttpResponse(
      body={
        "data": {
          "Type": "Event",
          "count": 1,
          "attributes": {"event_name": event_name}
        }
      },status_code= 201
    )



    
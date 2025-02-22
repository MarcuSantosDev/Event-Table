from .subscribers_repository import SubscribersRepository
import pytest

@pytest.mark.skip("Insert in DB")
def test_insert():
  subscriber_info = {
    "name": "Meu Nome",
    "email": "Meu Email", 
    "evento_id": 2,
  }
  subs_repo = SubscribersRepository()
  subs_repo.insert(subscriber_info)

def test_select_subscriber():
  email = "Meu Email"
  evento_id = 2

  subs_repo = SubscribersRepository()
  resp = subs_repo.select_subscriber(email,evento_id)
  print(resp.email)
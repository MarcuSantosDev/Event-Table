from flask import Flask
from src.main.routes.event import event_route_bp #carrega as rotas
from src.main.routes.subs import subs_route_bp

app = Flask(__name__) #Criação de um arquivo http

#Registra as rotas
app.register_blueprint(event_route_bp)
app.register_blueprint(subs_route_bp)

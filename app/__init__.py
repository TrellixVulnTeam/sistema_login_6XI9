
from bottle import Bottle
from bottle import TEMPLATE_PATH
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os, sys


Base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=True)

app = Bottle()
# create = True -> Executa o create all
# commit=True -> Comita as mudanças apos a rota ser executada
plugin = sqlalchemy.Plugin(engine, Base.metadata, keyword='db', create=True, commit=True, use_kwargs=False)

app.install(plugin)
TEMPLATE_PATH.insert(0, 'app/views')

from app.controllers import default
from app.models import tables


#TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

#aux_dirname = os.path.dirname(sys.argv[0])
#aux_dirname=os.path.abspath(os.path.join(os.path.dirname(__file__)))

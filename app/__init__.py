
from bottle import Bottle
from bottle import TEMPLATE_PATH
import os, sys


app = Bottle()

from app.controllers import default


TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))

#aux_dirname = os.path.dirname(sys.argv[0])
aux_dirname=os.path.abspath(os.path.join(os.path.dirname(__file__)))

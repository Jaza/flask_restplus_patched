__version__ = '0.1.9'

from flask_restplus import *
from .api import Api
from .model import Schema, DefaultHTTPErrorSchema
from .namespace import Namespace
from .parameters import Parameters, PostFormParameters, PatchJSONParameters
from .swagger import Swagger
from .resource import Resource

try:
    from .model import ModelSchema
except ImportError:
    pass

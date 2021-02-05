from sanic.blueprints import Blueprint
from .controllers.auth import auth
from .controllers.payment import payment
from .controllers.report import report

api = Blueprint.group(auth, payment, report, url_prefix='/api')

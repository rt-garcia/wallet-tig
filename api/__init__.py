from sanic.blueprints import Blueprint
from .controllers.user import user
from .controllers.payment import payment
from .controllers.report import report
from .controllers.wallet import wallet
from .controllers.user import user
from .controllers.commerce import commerce

api = Blueprint.group(user, payment, report, commerce, wallet, url_prefix='/api')

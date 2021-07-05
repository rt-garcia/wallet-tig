from sanic import Blueprint
from sanic.request import Request
from sanic_jwt_extended.decorators import jwt_required, jwt_optional
from ..models import report

report = Blueprint('report', '/report')


@report.route('/totalTxs', ['POST'])
@jwt_required
async def tTxs(request: Request):
    return True


@report.route('/usersRegistered', ['POST'])
@jwt_required
async def listB(request: Request):
    return True


@report.route('/blockUser', ['POST'])
@jwt_required
async def listB(request: Request):
    return True


@report.route('/unblockUser', ['POST'])
@jwt_required
async def listB(request: Request):
    return True


@report.route('/totalMoney', ['POST'])
@jwt_required
async def listB(request: Request):
    return True



from sanic import Blueprint
from views.user.get_user import GetUser

view_user = Blueprint("user", url_prefix="/user/v1")

view_user.add_route(GetUser.as_view(), "/get_all_user")
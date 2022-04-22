from sanic import Blueprint
from views.scheduler_service import Book

view_bp = Blueprint("scheduler_tasks", url_prefix="/api_scheduler/v1")

view_bp.add_route(Book.as_view(), "/test")

from app.dao.base import BaseDao
from app.users.models import Users


class UsersDAO(BaseDao):
    model = Users

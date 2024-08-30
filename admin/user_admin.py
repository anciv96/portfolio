from typing import Any

import bcrypt
from sqladmin import ModelView
from starlette.requests import Request

from models.user_model import User


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id, User.username, User.is_admin
    ]
    form_edit_rules = ['username', 'is_admin']

    async def on_model_change(
        self, data: dict, model: Any, is_created: bool, request: Request
    ) -> None:
        if not is_created:
            data.pop('hashed_password', None)
        else:
            password_hash = bcrypt.hashpw(data['hashed_password'].encode('utf-8'), bcrypt.gensalt())
            data['hashed_password'] = password_hash.decode('utf-8')

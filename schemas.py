from flask_marshmallow import Marshmallow
from marshmallow import post_load

import app
from models import User

marshmallow = Marshmallow(app)


class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'user_role', 'password')

        @post_load
        def make_user(self, data):
            return User(**data)


user_schema = UserSchema()
users_schema = UserSchema(many=True)

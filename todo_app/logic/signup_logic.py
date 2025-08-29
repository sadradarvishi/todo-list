from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from todo_app.dao.user_dao import UserDao

class SignUpLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_dao = UserDao()

    def create_user(self, data):
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        try:
            validate_password(password)
        except Exception as e:
            raise ValidationError(str(e))

        hashed_password = make_password(password)

        return self.user_dao.create_user(
            firstname=firstname,
            lastname=lastname,
            username=username,
            password=hashed_password,
            email=email
        )
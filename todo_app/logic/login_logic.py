from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

from todo_app.dao.user_dao import UserDao

class LoginLogic:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_dao = UserDao()

    def login_user(self, data, username):
        password = data.get('password')
        user = self.user_dao.get_user_by_username(username=username)

        if not user.check_password(password):
            raise ValidationError("Incorrect password")

        return self.generate_token_for_user(user)


    def generate_token_for_user(self, user):
        refresh_token = RefreshToken.for_user(user)

        return {
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token)
        }
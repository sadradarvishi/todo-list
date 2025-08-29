from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny

from todo_app.tasks import send_email
from todo_app.logic.login_logic import LoginLogic

class LoginController(APIView):
    permission_classes = [AllowAny]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login_logic = LoginLogic()

    def post(self, request):
        try:
            data = request.data
            username = data.get("username")
            token = self.login_logic.login_user(data, username)

            send_email.delay(username)

            return Response(token, HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), HTTP_400_BAD_REQUEST)
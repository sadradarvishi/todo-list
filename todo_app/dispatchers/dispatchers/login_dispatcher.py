from django.urls import path

from todo_app.controller.login_controller import LoginController

urlpatterns = [
    path('', LoginController.as_view())
]
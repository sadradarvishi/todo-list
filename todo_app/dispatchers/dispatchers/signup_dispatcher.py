from django.urls import path

from todo_app.controller.signup_controller import SignUpController

urlpatterns = [
    path('', SignUpController.as_view())
]
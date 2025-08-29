from django.urls import path, include

urlpatterns = [
    path('signup/', include('todo_app.dispatchers.dispatchers.signup_dispatcher')),
    path('login/', include('todo_app.dispatchers.dispatchers.login_dispatcher')),
    path('tasks/', include('todo_app.dispatchers.dispatchers.tasks_dispatcher')),
]
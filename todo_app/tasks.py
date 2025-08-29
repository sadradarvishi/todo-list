from celery import shared_task
from django.core.mail import send_mail

from todo_app.entity.user_entity import UserEntity

@shared_task(acks_late=True, ignore_result=True)
def send_email(username):
    user = UserEntity.objects.get(username=username)
    subject = f"hello {user.firstname}"
    message = (
        "welcome to my todo-list app \n\n"
        "hope you enjoy it!"
    )
    send_mail(
        subject=subject,
        message=message,
        from_email='sadsaddardar@gmail.com',
        recipient_list=[user.email],
        fail_silently=False
    )
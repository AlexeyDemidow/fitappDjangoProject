from django.core.mail import send_mail
from django_fit_calories_app.celery import app
from .service import send_email
from .models import CustomUser


@app.task
def send_mailing(user_name, user_email):
    send_email(user_name, user_email)


@app.task
def beat_mailing():
    for user in CustomUser.objects.all():
        send_mail(
            'MyFitApp',
            f'{user.username}, напоминаем вам внести данные по БЖУ и выпитой воды за сегодня, а так же взвеситься.',
            'django_fitapp@mail.ru',
            [user.email],
            fail_silently=False,
        )

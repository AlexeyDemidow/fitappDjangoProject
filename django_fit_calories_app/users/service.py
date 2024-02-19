from django.core.mail import send_mail


def send_email(user_name, user_email):
    send_mail(
        'Cпасибо что выбрали MyFitApp!',
        f'{user_name}, cпасибо что выбрали наш сервис для отслеживания питания и веса!\n'
        '\nС уважением, команда MYFITAPP.',
        'django_fitapp@mail.ru',
        [user_email],
        fail_silently=False,
    )

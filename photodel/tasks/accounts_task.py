from django.template.loader import render_to_string
from services.accounts_service import send_email_to_users, get_name_user
from additional_entities.models import EmailFragment
from photodel.celery import app
from django.conf import settings


@app.task
def task_send_email_to_user(email, code):
    title = f'Платформа photodel приветствует вас'
    url = f'{settings.BASE_URL}?email_token={code}'
    login_or_name, profile = get_name_user(email)
    placement_piece = EmailFragment.objects.all().first().verify_email
    html_content = render_to_string('mail_templates/mail.html', {"login": login_or_name,
                                                                 "placement_piece": placement_piece,
                                                                 "fragment": url})
    return send_email_to_users(title, [email], html_content)


@app.task
def task_send_reset_password_to_email(email, code):
    title = 'Платформа photodel.by приветствует вас'
    url = f'{settings.BASE_URL}?reset_token={code}'
    login_or_name, profile = get_name_user(email)
    placement_piece = EmailFragment.objects.all().first().reset_password
    html_content = render_to_string('mail_templates/mail.html', {"login": login_or_name,
                                                                 "placement_piece": placement_piece,
                                                                 "fragment": url})
    return send_email_to_users(title, [email], html_content)
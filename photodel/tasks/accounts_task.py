from django.template.loader import render_to_string
from services.accounts_service import send_email_to_users, get_name_user
from additional_entities.models import EmailFragment
from photodel.celery import app


@app.task
def task_send_email_to_user(email, code):
    title = f'{code}: Платформа photodel приветствует вас'
    login_or_name, profile = get_name_user(email)
    placement_piece = EmailFragment.objects.all().first().verify_email
    html_content = render_to_string('mail_templates/mail.html', {"login": login_or_name,
                                                                 "placement_piece": placement_piece,
                                                                 "fragment": code})
    return send_email_to_users(title, [email], html_content)


@app.task
def task_send_reset_password_to_email(email, code):
    title = 'Платформа photodel.by приветствует вас'
    login_or_name, profile = get_name_user(email)
    placement_piece = EmailFragment.objects.all().first().reset_password.replace('~pass', code)
    html_content = render_to_string('mail_templates/mail.html', {"login": login_or_name,
                                                                 "placement_piece": placement_piece
                                                                  })
    return send_email_to_users(title, [email], html_content)
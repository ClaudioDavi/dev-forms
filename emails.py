from flask_mail import Message
from app import app
from app import mail


def send_email(recipient, position):
    msg = Message(
        subject='Obrigado por se candidatar',
        sender=app.config['DEFAULT_FROM_MAIL'],
        recipients=[recipient,]
    )
    msg.body = "Obrigado por se candidatar, assim que tivermos uma vaga disponível " \
               "para programador %s entraremos em contato." % position
    mail.send(msg)

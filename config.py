import os

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'colocar-no-environ-depois'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_USERNAME = 'claudio.smtp.server@gmail.com'
DEFAULT_FROM_MAIL = 'claudio.smtp.server@gmail.com'
MAIL_PASSWORD = 'SmtpMailServer'
MAIL_PORT = 587
MAIL_USE_TLS = True

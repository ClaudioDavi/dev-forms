from app.models import Dev
from app.emails import send_email

def create_user(user_name, user_email):
    return Dev(user_name, user_email)

def is_front(html,css,js):
    if html >= 7 and js >=7 and css >= 7:
        return True
    else:
        return False

def is_back(python, django):
    if python >= 7 and django >= 7:
        return True
    else:
        return False

def is_mobile(ios, android):
    if ios >= 7 and android >= 7:
        return True
    else:
        return False

def handle_email(developer):
    is_generic = True
    for k,v in developer.positions.items():
        if v:
            is_generic = False
            send_email(developer.email, k)
    if is_generic:
        send_email(developer.email, '')
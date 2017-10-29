from app.models import Dev
from app.emails import send_email

def create_user(user_name, user_email):
    return Dev(user_name, user_email)

def handle_form(form):
    dev = create_user(form.name.data, form.email.data)
    front = is_allowed(form.skill_html.data,
                form.skill_css.data,
                form.skill_js.data
                )
    back = is_allowed(form.skill_python.data,
                form.skill_django.data
                )
    mobile = is_allowed(form.skill_ios.data,
                form.skill_android.data
                )
    dev.positions = {'Front End': front,
                     'Back End': back,
                     'Mobile': mobile
                     }
    handle_email(dev)


def is_allowed(*args):
    for arg in args:
        if arg < 7:
            return False
    return True

def handle_email(developer):
    is_generic = True
    for position, value in developer.positions.items():
        if value:
            is_generic = False
            send_email(developer.email, position)
    if is_generic:
        send_email(developer.email, '')
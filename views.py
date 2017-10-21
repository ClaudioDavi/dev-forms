from flask import render_template, request, redirect

from app import app
from app.forms import DevForm
import app.controllers as ctrl


@app.route("/", methods=['GET', 'POST'])
def index():

    form = DevForm()

    if request.method == 'POST' and form.is_submitted():

        dev = ctrl.create_user(form.name.data, form.email.data)

        is_front = ctrl.is_front(form.skill_html.data,
                                 form.skill_css.data,
                                 form.skill_js.data
                                 )

        is_back = ctrl.is_back(form.skill_python.data,
                               form.skill_django.data
                               )

        is_mobile = ctrl.is_mobile(form.skill_ios.data,
                                   form.skill_android.data
                                   )

        dev.positions = {'Front End': is_front,
                         'Back End': is_back,
                         'Mobile': is_mobile
                         }

        ctrl.handle_email(dev)
        return redirect('/thanks')

    return render_template('index.html',
                           title='HOME',
                           form = form,
                           )

@app.route("/thanks")
def thanks():
    return render_template('thanks.html', title='THANKS')
from flask import render_template, request, redirect

from app import app
from app.forms import DevForm
import app.controllers as form_controller


@app.route("/", methods=['GET', 'POST'])
def index():

    form = DevForm()

    if request.method == 'POST' and form.is_submitted() and form.validate_on_submit():

        form_controller.handle_form(form)

        return redirect('/thanks')

    return render_template('index.html',
                           title='Inicio',
                           form=form,
                           )


@app.route("/thanks")
def thanks():
    return render_template('thanks.html', title='Obrigado')

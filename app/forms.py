from flask_wtf import FlaskForm
from wtforms.fields.html5 import IntegerRangeField, EmailField
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class DevForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    skill_html = IntegerRangeField('skill_html')
    skill_css = IntegerRangeField('skill_css')
    skill_js = IntegerRangeField('skill_js')
    skill_python = IntegerRangeField('skill_python')
    skill_django = IntegerRangeField('skill_django')
    skill_android = IntegerRangeField('skill_android')
    skill_ios = IntegerRangeField('skill_ios')




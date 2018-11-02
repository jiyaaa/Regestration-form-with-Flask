from flask import Flask , render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
from  wtforms.fields.html5 import DateField

form1 = Flask(__name__)
form1.config['SECRET_KEY'] = 'this_is_a_secret'
form1.config['RECAPTCHA_PUBLIC_KEY'] = '6Ld_K3gUAAAAAKwV0QLkBj3IFkGnd0jB6dGkT1EG'
form1.config['RECAPTCHA_PRIVATE_KEY'] = #sorry , plz visit google recaptcha,,

class RegisterForm(FlaskForm):
    user = StringField('username')
    email = StringField('Email')
    pasw = PasswordField('Password')
    recaptcha = RecaptchaField('')
    dob = DateField('Date of Birth', format = '%Y-%m-%d')

@form1.route('/', methods=['GET', 'POST'])
def formatt():
    form = RegisterForm()
    return render_template("formatt.html", form = form )
if __name__ == '__main__':
    form1.run(debug=True)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Přezdívka", validators=[DataRequired()])
    password = PasswordField("Heslo", validators=[DataRequired()])
    remember_me = BooleanField("Pamatuj si mě")
    submit = SubmitField("Přihlásit")

class RegistrationForm(FlaskForm):
    username = StringField('Přezdívka', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Heslo', validators=[DataRequired()])
    password2 = PasswordField('Stejné heslo znovu', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zaregistrovat se')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Použij prosím jinou přezdívku.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Použij prosím jinou e-mailovou adresu.")

class EditProfileForm(FlaskForm):
    username = StringField('Přezdívka', validators=[DataRequired()])
    about_me = TextAreaField('O mně', validators=[Length(min=0, max=140)])
    submit = SubmitField('Potvrdit')

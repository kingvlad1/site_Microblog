#Wt-Forms = WTF!!
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
#WTF?

class LoginForm(FlaskForm):
    username = StringField("Ім'я", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запам'ятати мене")
    submit = SubmitField("Авторизуватися")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Register")

class Feedback(FlaskForm):
    name = StringField("Вкажіть ваше справжнє ім'я", validators=[DataRequired()])
    email = StringField("Ваш Email", validators=[DataRequired()])
    embed = StringField("Опис вашого запиту", validators=[DataRequired()])
    submit = SubmitField("Відправити запит")

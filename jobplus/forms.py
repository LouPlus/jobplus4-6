from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import Length, Email, EqualTo, Required

class BaseForm(FlaskForm):
	email = StringField('Email',validators=[Required(),Email()])
	password = PasswordField('Password',validators=[Required(),Length(1,24)])
	submit = SubmitField('Submit')

class LoginForm(BaseForm):
	remember_me = BooleanField('Remember me')

class CompanyRegisterForm(BaseForm):
	company_name = StringField('Company name',validators=[Required(),Length(1,24)])
	repeat_password = PasswordField('Repeat password',validators=[Required(),EqualTo('password')])

class EmployeeRegisterForm(BaseForm):
	username = StringField('Username',validators=[Required(),Length(1,24)])
	repeat_password = PasswordField('Repeat password',validators=[Required(),EqualTo('password')])

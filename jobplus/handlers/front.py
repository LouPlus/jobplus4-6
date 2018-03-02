from flask import Blueprint, render_template
from jobplus.forms import LoginForm, CompanyRegisterForm, EmployeeRegisterForm

front = Blueprint('front', __name__)
@front.route('/')
def index():
	return render_template('index.html')

@front.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html',form=form)

@front.route('/company_register')
def company_register():
	form = CompanyRegisterForm()
	return render_template('company_register.html',form=form)

@front.route('/employee_register')
def employee_register():
	form = EmployeeRegisterForm()
	return render_template('employee_register.html',form=form)
	
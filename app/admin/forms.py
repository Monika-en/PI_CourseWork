# app/admin/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, IntegerField
from wtforms.validators import DataRequired

class UserEditForm(FlaskForm):
    # Form for admin to edit user

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    notifications =  SelectField('Notifications', choices=[ ('0', 'Disabled'),
                        ('1', 'Enabled')], validators=[DataRequired()])
    type = SelectField('Type', choices=[ ('0', 'Basic'),
                        ('1', 'Premium')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class PasswordForm(FlaskForm):
    current_pass = PasswordField('Current Password', validators=[DataRequired()])
    new_pass = PasswordField('New Password', validators=[DataRequired()])
    new_pass_repated = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField('Change')
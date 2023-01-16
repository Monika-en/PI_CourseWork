# app/admin/views.py
from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import UserEditForm
from .. import db
from ..models import User

from datetime import datetime, timedelta, timezone
from ..auth import views as mailing

typeDict = {'long': 'Long',
            'short': 'Short',
            'buyStop': 'Buy stop',
            'sellStop': 'Sell stop',
            'buyLimit': 'Buy limit',
            'sellLimit': 'Sell limit'}

def check_admin():
    #Prevent non-admins from accessing the page
    if current_user.type != 2:
        abort(403)


@admin.route('/users')
@login_required
def list_users():
    #List all users
    check_admin()

    users = User.query.all()
    return render_template('admin/users/users.html',
                           users=users, title='Users')

@admin.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    #Edit user
    check_admin()

    user = User.query.get_or_404(id)

    # prevent admin from being assigned a department or role
    #if employee.is_admin:
    #    abort(403)

    form = UserEditForm(obj=user)
    if form.validate_on_submit():
        user.fist_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.notifications = form.notifications.data
        if user.type != 2:
            user.type = form.type.data
        db.session.add(user)
        db.session.commit()
        flash('You have successfully edited user.')

        # redirect to the roles page
        return redirect(url_for('admin.list_users'))

    return render_template('admin/users/user.html',
                            user=user,
                            form=form,
                            title='Edit User')

@admin.route('/users/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    #Delete user
    check_admin()

    #user = User.query.get_or_404(id)
    #User.query.filter_by(id=123).delete()
    User.query.filter(User.id == id).delete()
    db.session.commit()
    flash('You have successfully deleted user.', 'success')
    #users = User.query.all()
    return redirect(url_for('admin.list_users'))
    #return render_template('admin/users/users.html', users=users, title='Users')
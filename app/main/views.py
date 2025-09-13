from . import main as main
from flask import (
    render_template, redirect, url_for, flash, request
)
from flask_login import login_required

@main.route('/')
def index():
    return redirect(url_for('security.login'))

@main.route('/home')
@login_required
def home():
    return render_template('main/index.html')
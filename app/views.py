from flask import render_template, flash, redirect
from app import appl
from .forms import LoginForm

@appl.route('/')
@appl.route('/index')
def index():
    user = {'nickname': 'Daphne'}
    posts = [
    {
        'author': {'nickname':'John'},
        'body': 'Beautiful day!'
    },
    {
        'author': {'nickname': 'Susan'},
        'body': 'Cool!'
    }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@appl.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=appl.config['OPENID_PROVIDERS'])

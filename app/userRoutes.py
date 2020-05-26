from flask import session, redirect, url_for, render_template
from app.data import *
from app.config import *
from datetime import datetime as dt



@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if "e_mail" in session:
        return redirect(url_for('profile'))

    today = f'{week_days[dt.today().weekday()].capitalize()}, {dt.today().strftime("%d - %m - %Y")}'
    main_nav = [
        {'name': 'Home', 'url': 'home'},
        {'name': 'Trouver un Hopitâl à proximité', 'url': 'find_hospital'},
        {'name': 'Create an account', 'url': 'signup'},
        {'name': 'Se Connecter', 'url': 'login'},
    ]
    title = 'WEHELP | Home'
    description = 'WEHELP Home Page'
    return render_template('home.jinja2',
                           title=title,
                           description=description,
                           main_nav=main_nav,
                           today=today,
                           )
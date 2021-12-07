from db.database import Database
from flask import Flask, g, render_template, request
from flask import jsonify
from recuperation import get_db, importation_donnees_piscines, gestion_donnees_piscines
from recuperation import importation_donnees_glissades, gestion_donnees_glissades
from recuperation import importation_donnees_patinoires, gestion_donnees_patinoires
from recuperation import importation_gestion_all
from mail.mail import send_mail

import atexit
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)
app.secret_key = "toto"

app.config['SECRET_KEY'] = 'c4c287e37fd35eb88596cb2ec526b1e1'
app.config['SECURITY_PASSWORD_SALT'] = '9d3ec01441ee8fc92f7c526d89acc604'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'inf5190bertrand@gmail.com'
app.config['MAIL_PASSWORD'] = 'linfOcch0uette'

sched = BackgroundScheduler({'apscheduler.timezone': 'Canada/Eastern'}, deamon=True)
sched.add_job(importation_gestion_all, 'cron', hour=0)
sched.start()
atexit.register(lambda: sched.shutdown())

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.route('/')
def home():
    prenom = "Anna"
    # send_mail(prenom)
    return 'Hellooo'

@app.route('/doc')
def documentation():
    return render_template('documentation.html')

@app.route('/api/installations', methods=["GET"])
def get_installations():
    arrondissement = request.args.get("arrondissement")
    piscines = get_db().get_piscines_by_arrondissement(arrondissement)
    dict_piscines = [installation.asDictionary() for installation in piscines]
    glissades = get_db().get_glissades_by_arrondissement(arrondissement)
    dict_glissades = [installation.asDictionary() for installation in glissades]
    patinoires = get_db().get_patinoires_by_arrondissement(arrondissement)
    dict_patinoires = [installation.asDictionary() for installation in patinoires]
    
    return jsonify([dict_piscines+dict_glissades+dict_patinoires])


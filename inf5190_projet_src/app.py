from db.database import Database
from flask import Flask, g, render_template, request, Response
from flask import jsonify, send_file
from recuperation import importation_gestion_all
from send_email.mail import send_mail
import dicttoxml
import csv
from twitter import send_tweet

# BackGroundScheduler
import atexit
from apscheduler.schedulers.background import BackgroundScheduler


def create_app():

    app = Flask(__name__)
    app.secret_key = "toto"

    app.config['SECRET_KEY'] = 'c4c287e37fd35eb88596cb2ec526b1e1'
    app.config['SECURITY_PASSWORD_SALT'] = '9d3ec01441ee8fc92f7c526d89acc604'

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'inf5190bertrand@gmail.com'
    app.config['MAIL_PASSWORD'] = 'linfOcch0uette'

    app.config['JSON_AS_ASCII'] = False

    with app.app_context():
        importation_gestion_all()
        sched = BackgroundScheduler(
                                    {'apscheduler.timezone': 'Canada/Eastern'},
                                    deamon=True)
        sched.add_job(importation_gestion_all, 'cron', hour=0)
        # Décommentez cette ligne pour tester le Background scheduler
        # sched.add_job(importation_gestion_all, 'interval', seconds=30)
        sched.start()
        atexit.register(lambda: sched.shutdown())

    return app


app = create_app()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


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
    # importation_gestion_all()
    # prenom = "Anna"
    # send_mail(prenom)
    # send_tweet()
    noms = get_db().get_all_names()
    return render_template('home.html', noms=noms)


@app.route('/doc')
def documentation():
    return render_template('documentation.html')


@app.route('/api/installations', methods=["GET"])
def get_installations():
    arrondissement = request.args.get("arrondissement")
    piscines = get_db().get_piscines_by_arrondissement(arrondissement)
    dict_piscines = [
        installation.asDictionary() for installation in piscines]
    glissades = get_db().get_glissades_by_arrondissement(arrondissement)
    dict_glissades = [
        installation.asDictionary() for installation in glissades]
    patinoires = get_db().get_patinoires_by_arrondissement(arrondissement)
    dict_patinoires = [
        installation.asDictionary() for installation in patinoires]

    if (len(dict_piscines) == 0
            and len(dict_glissades) == 0
            and len(dict_patinoires) == 0):
        error = ("L'arrondissement saisi n'est pas renseigné")
        return render_template("404.html", error=error), 404
    return jsonify([dict_piscines+dict_glissades+dict_patinoires])


@app.route('/api/installations/2021', methods=["GET"])
def get_installations_2021():
    glissades = get_db().get_glissades_updated_in_2021()
    dict_glissades = [
        installation.asDictionary() for installation in glissades]
    patinoires = get_db().get_patinoires_updated_in_2021()
    dict_patinoires = [
        installation.asDictionary() for installation in patinoires]

    if (len(dict_glissades) == 0
            and len(dict_patinoires) == 0):
        error = ("Aucune données renseignées...")
        return render_template("404.html", error=error), 404

    return jsonify([dict_glissades+dict_patinoires])


@app.route('/api/installations/2021/xml', methods=["GET"])
def get_installations_2021_xml():
    glissades = get_db().get_glissades_updated_in_2021()
    dict_glissades = [
        installation.asDictionary() for installation in glissades]
    patinoires = get_db().get_patinoires_updated_in_2021()
    dict_patinoires = [
        installation.asDictionary() for installation in patinoires]

    if (len(dict_glissades) == 0
            and len(dict_patinoires) == 0):
        error = ("Aucune données renseignées...")
        return render_template("404.html", error=error), 404

    xml = dicttoxml.dicttoxml(dict_glissades+dict_patinoires)
    return xml


@app.route('/api/installations/2021/csv', methods=["GET"])
def get_installations_2021_csv():
    installations = get_db().get_installations_updated_in_2021()
    dict_installations = [
        installation.asDictionary() for installation in installations]

    with open('installations_2021.csv', 'w', newline='') as csvfile:
        fieldnames = ["id", "nom", "nom_arrondissement"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(dict_installations)):
            writer.writerow(dict_installations[i])
    if (len(dict_installations) == 0):
        error = ("Aucune données renseignées...")
        return render_template("404.html", error=error), 404

    csvfile.close()
    return send_file('installations_2021.csv',
                     as_attachment=True,
                     attachment_filename='installations_2021.csv')


@app.route('/api/installation', methods=["GET"])
def get_installation():
    nom = request.args.get("nom")
    installations = get_db().get_installation_by_name(nom)
    dict_installations = [
        installation.asDictionary() for installation in installations]
    if (len(dict_installations) == 0):
        error = ("Le nom saisi est incorrect...")
        return render_template("404.html", error=error), 404

    return jsonify([dict_installations])

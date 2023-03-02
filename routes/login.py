from flask import render_template, request
from database import Database
from . import login_bp

ProfileUtilisateur = {}

@login_bp.route("/login", methods=['POST'])
def login():

    courriel = '"'+request.form.get('courriel')+'"'
    passe = request.form.get('motpasse')

    database = Database()

    cmd='SELECT motpasse FROM utilisateurs WHERE courriel='+courriel+';'
    passeVrai = database.query_one(cmd)

    if (passeVrai!=None) and (passe==passeVrai[0]):

        cmd='SELECT * FROM utilisateurs WHERE courriel='+courriel+';'
        info = database.query_one(cmd)

        global ProfileUtilisateur
        ProfileUtilisateur["courriel"]=courriel
        ProfileUtilisateur["nom"]=info[2]
        ProfileUtilisateur["avatar"]=info[3]
        return render_template('bienvenu.html', profile=ProfileUtilisateur)

    return render_template('login.html', message="Informations invalides!")



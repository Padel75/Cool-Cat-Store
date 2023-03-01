from flask import render_template, request
import pymysql
from secrets import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, MYSQL_PORT
from . import login_bp

ProfileUtilisateur = {}

@login_bp.route("/login", methods=['POST'])
def login():

    courriel = '"'+request.form.get('courriel')+'"'
    passe = request.form.get('motpasse')

    conn= pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD,db=MYSQL_DB, port=MYSQL_PORT)
    cmd='SELECT motpasse FROM utilisateurs WHERE courriel='+courriel+';'
    cur=conn.cursor()
    cur.execute(cmd)
    passeVrai = cur.fetchone()

    if (passeVrai!=None) and (passe==passeVrai[0]):

        cmd='SELECT * FROM utilisateurs WHERE courriel='+courriel+';'
        cur=conn.cursor()
        cur.execute(cmd)
        info = cur.fetchone()

        global ProfileUtilisateur
        ProfileUtilisateur["courriel"]=courriel
        ProfileUtilisateur["nom"]=info[2]
        ProfileUtilisateur["avatar"]=info[3]
        return render_template('bienvenu.html', profile=ProfileUtilisateur)

    return render_template('login.html', message="Informations invalides!")



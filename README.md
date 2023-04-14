# ALL COOL STUFF
## Serveur

### Installation

Assurez-vous d'installer les librairies python à l'aide de la commande suivante :

    pip install -r requirements.txt

### Lancement

Pour lancer le serveur en **https**, il suffit d'exécuter le fichier `main.py` :

    python app.py

Vous devriez voir apparaître le message suivant :

    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on https://127.0.0.1:5000

Pour lancer le serveur en **http**, il suffit d'exécuter :

    flask run

Prendre note que l'application Vue.js utilise le url "https://127.0.0.1:5000" pour l'api.

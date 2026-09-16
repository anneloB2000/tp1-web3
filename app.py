"""
TP1 - Web3 - Pokemon
"""

from flask import Flask, render_template, request
import bd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/ajout-carte')
def ajout_carte():
    return render_template('ajout-carte.jinja')

@app.route('/collection')
def collection():
    collection_carte = []

    with bd.creer_connexion() as conn:
        with conn.get_curseur() as curseur:
            collection_carte = curseur.execute("select * from elements_collection")

    return render_template('collection.jinja', collection_carte=collection_carte)





app.run(debug=True)
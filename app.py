"""
TP1 - Web3 - Pokemon
"""

from flask import Flask, render_template, request
import bd

app = Flask(__name__)


@app.route('/')
def index():
    collection_carte = []

    with bd.creer_connexion() as conn:
        with conn.get_curseur() as curseur:
            curseur.execute("select * from elements_collection limit 5")
            collection_carte = curseur.fetchall()

    return render_template('index.jinja', collection_carte=collection_carte)

@app.route('/ajout-carte')
def ajout_carte():
    return render_template('ajout-carte.jinja')

@app.route('/collection')
def collection():
    collection_carte = []

    with bd.creer_connexion() as conn:
        with conn.get_curseur() as curseur:
            curseur.execute("select * from elements_collection")
            collection_carte = curseur.fetchall()

    return render_template('collection.jinja', collection_carte=collection_carte)




@app.route('/details-carte')
def details_carte():
    """Affiche les détails d'une carte"""
    identifiant = request.args.get('id', type=int)
    carte = {}

    with bd.creer_connexion() as conn:
        with conn.get_curseur() as curseur:
            curseur.execute(
             'SELECT * FROM carte_pokemon JOIN elements_collection ON carte_pokemon.id = elements_collection.id_carte WHERE elements_collection.id = %(id)s',
                {
                    'id': identifiant
                }
            )
            carte = curseur.fetchone()

    return render_template('detail-carte.jinja', carte=carte)

app.run(debug=True)

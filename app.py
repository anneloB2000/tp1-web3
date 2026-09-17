"""
TP1 - Web3 - Pokemon
"""

from flask import Flask, render_template, request
import bd

app = Flask(__name__)


@app.route('/')
def index():
    """Affiche la pahge d'accueil"""
    collection_carte = []

    with bd.creer_connexion() as conn:
        with conn.get_curseur() as curseur:
            curseur.execute("select * from elements_collection where statut = 1 limit 5")
            collection_carte = curseur.fetchall()

    return render_template('index.jinja', collection_carte=collection_carte)

@app.route('/ajout-carte')
def ajout_carte():
    """Affiche la page d'ajout d'une carte"""

    return render_template('ajout-carte.jinja')

@app.route('/collection')
def collection():
    """Affiche la"""
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

@app.route('/illustrateurs')
def illustrateurs():
    """Affiche la page listant tous les illustrateurs"""
    liste_illustrateurs = []

    with bd.creer_connexion() as conn:
        with conn.get_curseur() as curseur:
            curseur.execute("select * from carte_pokemon group by illustrateur order by illustrateur desc limit 20")
            liste_illustrateurs = curseur.fetchall()

    return render_template('illustrateurs.jinja',illustrateurs=liste_illustrateurs)

@app.route('/creations')
def creations():
    """Affiche toutes les créations d'un illustrateur"""
    illustrateur = request.args.get('illustrateur', type=str)
    cartes = {}

    with bd.creer_connexion() as conn:
        with conn.get_curseur() as curseur:
            curseur.execute(
             'SELECT * FROM carte_pokemon WHERE illustrateur=%(illu)s LIMIT 30',
                {
                    'illu': illustrateur
                }
            )
            cartes = curseur.fetchall()

    return render_template('creations.jinja', cartes=cartes)

if __name__ == "__main__":
    app.run(debug=True) 
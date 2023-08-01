# Importer les modules nécessaires
from flask import Flask, request, jsonify, send_from_directory  # Flask pour le serveur web, jsonify pour créer des réponses JSON
from flask_cors import CORS  # CORS pour gérer les requêtes cross-origin
import subprocess  # subprocess pour exécuter des commandes du système d'exploitation
import os  # os pour interagir avec le système d'exploitation

# Initialiser une instance de Flask
app = Flask(__name__)
# Appliquer CORS à notre application pour accepter les requêtes de toutes les origines
CORS(app)

# Définir le chemin d'accès au répertoire ".well-known" dans le répertoire racine de l'application
well_known_dir = os.path.join(app.root_path, '.well-known')

# Créer une route pour servir des fichiers du répertoire ".well-known"
@app.route('/.well-known/<path:filename>')
def well_known(filename):
    # Utiliser send_from_directory pour envoyer le fichier demandé
    return send_from_directory(well_known_dir, filename)

# Créer une route pour exécuter des commandes POST
@app.route('/run', methods=['POST'])
def run_command():
    # Extraire les données JSON de la requête
    data = request.get_json()
    # Extraire la liste des commandes du JSON
    commands = data.get('commands')

    # Si aucune commande n'est fournie, retourner une erreur
    if not commands:
        return jsonify({'error': 'No commands provided'}), 400

    # Un dictionnaire pour stocker les résultats de l'exécution des commandes
    output = {}
    for i, command in enumerate(commands):
        try:
            # Essayer d'exécuter la commande et de récupérer la sortie
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            output_lines = result.decode('utf-8').splitlines()
            # Enregistrer la sortie sous la clé "command_i"
            output[f"command_{i}"] = {'output': output_lines}
        except subprocess.CalledProcessError as e:
            # Si une erreur se produit lors de l'exécution de la commande, enregistrer l'erreur
            error_lines = e.output.decode('utf-8').splitlines()
            output[f"command_{i}"] = {'error': error_lines}

    # Retourner la sortie de toutes les commandes sous forme de JSON
    return jsonify(output)

# Si ce script est le point d'entrée, exécuter l'application
if __name__ == '__main__':
    app.run(host='localhost', port=3333)

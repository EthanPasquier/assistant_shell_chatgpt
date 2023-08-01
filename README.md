# Plugin Commande Shell - Assistant Shell

## Présentation

L'Assistant Shell est un plugin basé sur Flask permettant d'exécuter des commandes shell et de recevoir les résultats en format JSON. Ce plugin fonctionne avec le système de plugins d'OpenAI ChatGPT. L'API écoute sur `localhost:3333` et offre un endpoint `/run` pour l'exécution des commandes shell.

**Note :** Le logiciel est actuellement en phase ALPHA. Son utilisation est à vos propres risques.

## Mise en garde de sécurité ⚠️

Ce plugin a pour objectif d'être utilisé uniquement dans un contexte éducatif. Il est déconseillé de l'utiliser en environnement de production sans avoir mis en place des mesures de sécurité adéquates. L'exécution de commandes shell arbitraires via une API peut représenter un risque de sécurité conséquent. Veillez à soigneusement valider et assainir toute entrée qui pourrait être utilisée pour exécuter des commandes shell.

## Comment débuter

### Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3
- Flask
- Flask-CORS

### Procédure d'installation

1. Cloner le dépôt :
   
   ```bash
   git clone https://github.com/EthanPasquier/assistant_shell.git
   ```

2. Accéder au répertoire du projet :
   
   ```bash
   cd assistant_shell
   ```

3. Installer les dépendances :
   
   ```bash
   pip install -r requirements.txt
   ```

## Comment lancer le Plugin

1. Démarrer le serveur Flask :
   
   ```bash
   python main.py
   ```

2. Testez l'API en utilisant `curl` ou tout autre outil similaire :
   
   ```bash
   curl "http://localhost:3333/run?command=ls"
   ```

## Configuration du plugin dans ChatGPT

Dans ChatGPT, allez dans la boutique de plugins et choisissez d'ajouter un plugin. Sélectionnez l'option pour développer votre propre plugin et renseignez l'URL de votre script de plugin local. Si le test précédent a fonctionné, vous devriez pouvoir entrer `http://localhost:3333`.

## Licence

Ce projet est distribué sous licence MIT. Veuillez consulter le fichier LICENSE pour plus de détails.

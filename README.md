# Création d'une Api d'Intelligence Artificielle

## Starbucks Calories

### Introduction :

Nos données: Dataset Kaggle Starbucks https://www.kaggle.com/starbucks/starbucks-menu

Notre modèle : Régression Linéaire

Notre Api : L'Api Starbucks Calories permet de prédire le nombre de calories en fonction de la quantité de lipides, glucides, fibres et protéines.
Lien vers l'Api : http://starbucksfood.azurewebsites.net

### FastApi :

Pour créer et communiquer avec l'API

Importer FastApi
Créer une instance app : Exemple app = FastAPI()
Définir les requêtes (GET, POST, DELETE...)
Définir le chemin de la requête ex : (@app.get("/root/"))
Lancer le serveur de développement

Ressources : https://fastapi.tiangolo.com/tutorial/first-steps/

### Uvicorn :

Pour visualiser l'Api grâce au serveur uvicorn : uvicorn main:app --reload

   * main: le fichier main.py (le "module" Python).
   * app: l'objet crée dans le fichier main.py avec app = FastAPI().
   * --reload: permet au server de rédemarrer aprés chaques modifications


### Docker:

Méthode de cloisonnement: Faire tourner des environnements isolés les uns des autres dans des conteneurs, partageant le même noyau. Contrainement aux machines virtuelles, il n'inclut pas d'OS et s'appuie sur les fonctionnalités de l'OS hôte.
Le conteneur virtualise l'environnement d'éxécution, ce qui le rend plus facile a télécharger, migrer ou sauvegarder.

docker build -t <nom_image> . / docker run <nom_image>


### Azure:

Pour déployer notre modèle en ligne :

1) Créer un compte sur le portail Azure
2) Créer un registre de conteneur
3) Se connecter au registre grâce à Azure CLI
4) Envoyer l’image au registre avec docker pull et docker push
5) Exécuter l’image à partir du registre avec docker run
6) Se connecter à Azure via Vscode et App service Azure
7) Créer et générer une image grâce au Dockerfile
8) Déployer dans le registre de conteneurs
9) Enfin déployer sur App Service (http://<app-name>.azurewebsites.net)

Ressources : https://docs.microsoft.com/fr-fr/azure/app-service/quickstart-custom-container?tabs=python&pivots=container-linux

# :uk: EN :uk:
A python scrypt to generate random faces from https://thispersondoesnotexist.com (~5min / 1k faces)
## Features
- Generate random faces
- Save faces
- (INCOMING) Option to add filters (gender, age, etc.)
## Dependencies
- Python 3.10
- Requests ```pip install requests```
## How to use
Use the main.py to generate faces or use FaceGenerator.py as a module
main.py :
- Just ask for the number of faces you want to generate and then save them in faces/

## Config parameters:
- `url`: The URL to retrieve the face images from.
- `path_to_save`: The path where the face images will be saved.
- `prefix`: The prefix for the saved image filenames.
- `timing`: The wait time between each request (in seconds). Note: Setting this value below 0.3 seconds might lead to receiving duplicate images.


# :fr: FR :fr:
Un script python pour générer des visages aléatoires à partir de https://thispersondoesnotexist.com (~5min / 1k visages)
## Fonctionnalités
- Générer des visages aléatoires
- Sauvegarder les visages
- (À VENIR) Option pour ajouter des filtres (sexe, âge, etc.)
## Dépendances
- Python 3.10
- Requests ```pip install requests```
## Comment utiliser
Utilisez main.py pour générer des visages ou utilisez FaceGenerator.py comme module
main.py :
- Demande simplement le nombre de visages que vous souhaitez générer, puis les enregistre dans faces/

## Paramètres de configuration:
- `url`: L'URL pour récupérer les images de visage.
- `path_to_save`: Le chemin où les images de visage seront enregistrées.
- `prefix`: Le préfixe pour les noms de fichiers d'image qui seront enregistrés.
- `timing`: Le temps d'attente entre chaque requête (en secondes). Remarque : En dessous de 0,3 seconde peut conduire à recevoir des images en double.

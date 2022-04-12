# But du projet

Réaliser un code fonctionnel d'une application Web (un site).

Les objectifs suivants ont été atteints :

- Implémenter des requêtes GET/POST.
- Utiliser les patrons HTML Jinja, page de base.
- Implémenter PUT et DELETE.

# Rendu

Nous proposons un site internet qui recense des recettes de coktails. Il est possible de consulter simplement les recettes mais aussi d'en ajouter de nouvelles. Une recherche de recette par mots-clés est disponible.

# Exécution

## Configurer l'environnement

Pour configurer l'environnement sous linux ou sous macOS, suivez les commandes suivantes que vous pouvez retrouver https://flask.palletsprojects.com/en/2.1.x/installation/#virtual-environments.

Créer l'environnement : 
    $ python3 -m venv venv
Activer l'environnement :
    $ . venv/bin/activate
Installer Flask (dans l'environnement) :
    $ pip install -U pip flask
Lancer le serveur en mode débuggage :
    $ FLASK_ENV=development flask run

Une fois le serveur local lancé, vous aurez alors l'indication de l'adresse à suivre dans un navigateur internet afin d'ouvrir la page d'accueil du site :

http://127.0.0.1:5000/

## Fonctionnalités :

Vous retrouverez sur la barre de navigation en haut à gauche trois pages accessibles :

- La page d'accueil, avec le titre du site, et le top 3 des meilleurs coktails.
- Coktails qui permet d'accéder à la page présentant l'ensemble des recettes de coktails : http://127.0.0.1:5000/cocktails
- Contact qui permet d'accéder à la page de contact avec les différents moyens de contacter les gestionnaires du site : http://127.0.0.1:5000/contact

En plus de ces trois onglets, un outil recherche est implémenté. Il est possible d'écrire dans le champ une partie du nom d'un coktail, ou bien un ingrédient. L'icone "Search" à côté permet de lancer la recherche. Si cette dernière n'aboutit à aucun résultat, une page affichera "Aucune recette trouvée".

Vous pouvez cliquer sur une recette de votre choix, que ce soit sur la page d'accueil, de l'ensemble des recettes ou après une recherche fructueuse. Une fois le coktail sélectionné, vous accéderez à la page associée indiquant le coût, la difficulter de réalisation, les ingrédients nécessaires, les quantités associées et les étapes de préparation. Exemple de page : http://127.0.0.1:5000/cocktail/1

Il est possible d'ajouter un coktail à la base de donnée, à l'aide du bouton correspondant. Il vous sera demandé de remplir les détails précédemment mentionnés, propres à chaque coktail.
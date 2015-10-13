# Documentation

This project lets you access the users, their badges and 3d models via a REST API, and shows and implementation of automatic badge management.

The API is based on [Django REST Framework](http://www.django-rest-framework.org/). You will need to get it to run this demo.

    pip3 install djangorestframework markdown django-filter

## Browse the API

Just run the django development server:

    python3 manage.py runserver

Go to `localhost:8000`. That's it.


## About the demo

- The demo is not meant to be a production-ready API covering all cases, but rather focuses on showing the design and patterns used.
- You can then see users, models and badges using the corresponding endpoints. A user's achievments (badges) can be seen in the API user endpoint.
- Achievement checks and badge assignements are managed by the `BadgeManager` class.
  - The class is written so that each badge obtention condition can be checked independently.
  - Badges are given to users using Django signals (see `signals.py` for an arbitrary example of systematic check and update).
  - Currently, the demo checks all conditions on every User save(), but could be extended to perform specific checks on specific events.


# Original Instructions

- Partir d'une structure Django vierge
- Rajouter les users + un model Model3d() qui représente un modèle 3d
- Implémenter une fonctionnalité de 'badges'
  - Il existe plusieurs types de badge, chacun étant décerné pour une action ou série d'action effectuée par l'utilisateur sur le site
  - La liste des badges qu'un user a obtenu doit être accessible via l'api
  - Le backend doit "décerner" les badges aux users (ie: détecter quand une action a été réalisée et donner le badge au user)
    - Badges a implémenter (liste non limitative):
      - Star: le modèle d'un user a plus de 1k views
      - Collector: un user a uploadé plus de 5 modèles
      - Pionneer: le user est inscrit depuis plus de 1 an sur le site


Il n'y a pas de contrainte de temps mais, idéalement, n'y passe pas plus d'une journée. Les instructions sont volontairement assez vagues, pour te laisser faire tes propres choix. Quelques conseils généraux:

- Mettre l'accent sur la structure et la lisibilité
- Faire l'exercice en imaginant que ce code pourrait être mis en production demain
- Ne pas hésiter à laisser des commentaires pour expliquer les choix techniques (eg: expliquer les bénéfices / contraintes de telle ou telle solution)
- Ne pas hésiter à s'appuyer sur des libs externes (snippets, libraires, fonctions, modules django, etc), mais mettre un lien vers la resource dans le code
- Ne pas hésiter à s'appuyer les fonctionnalités de Django quand nécessaires: CBV, signals, forms, etc
- Le cadre de l'exercice n'est pas limitatif: tout bonus sera apprécié :)
- Ne pas hésiter à nous poser des questions si besoin

Merci d'envoyer le code dans un zip, ou mieux, sur un repo github.

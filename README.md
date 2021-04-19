# Synchronisation des Startups avec Airtable


## Mettre à jour les dépendances
```
pip3 install pipreqs
pipreqs . --force
```

## Configurer le script

Créer un fichier `.env`
```
AIRTABLE_BASE_ID={identifiant de la base, trouvable dans help > API Documentation}
AIRTABLE_API_KEY={clé, trouvable dans account : personnal api key}
AIRTABLE_TABLE={nom de la table}
```

Par exemple : 
```
AIRTABLE_BASE_ID=appXXXXXXXX
AIRTABLE_API_KEY=keyXXXXXXXX
AIRTABLE_TABLE=Startups
```

## Lancer le programme

```
# Voir la liste des SE qui ont changé
python3 startup.py

# Mettre à jour les SE
python3 startup.py -w

```

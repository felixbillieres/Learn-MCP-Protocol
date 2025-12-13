# Instructions - Projet 03

## Ta mission

Créer un modèle Pydantic et l'utiliser dans un outil MCP.

## Étapes à suivre

1. **Crée un modèle Pydantic `Message`** dans `solution.py` :
   - Hérite de `BaseModel`
   - Champs :
     - `expediteur` : str (obligatoire, description "Nom de l'expéditeur")
     - `destinataire` : str (obligatoire, description "Nom du destinataire")
     - `contenu` : str (obligatoire, description "Contenu du message")
     - `priorite` : str (optionnel, par défaut "normale", description "Priorité du message")
   - Utilise `Field()` pour les descriptions

2. **Crée un modèle Pydantic `MessageResponse`** :
   - `message_id` : int (description "ID unique du message")
   - `expediteur` : str
   - `destinataire` : str
   - `contenu` : str
   - `priorite` : str
   - `date_envoi` : str (description "Date d'envoi du message")

3. **Crée un outil `envoyer_message`** :
   - Prend un paramètre `message` de type `Message`
   - Retourne un `MessageResponse`
   - Génère un `message_id` aléatoire (ou utilise un compteur)
   - Crée la date d'envoi (format string simple : "2024-01-15 10:30:00")
   - Retourne les informations formatées

## Indices

- Importe `BaseModel` et `Field` depuis `pydantic`
- Les modèles Pydantic héritent de `BaseModel`
- `Field()` permet d'ajouter des descriptions et des contraintes
- Pour générer un ID, tu peux utiliser `import random; random.randint(1, 10000)`
- Pour la date, tu peux utiliser `from datetime import datetime; datetime.now().strftime("%Y-%m-%d %H:%M:%S")`

## Test

Utilise `python test.py` pour vérifier que :
- Les modèles sont bien définis
- La validation fonctionne
- L'outil fonctionne correctement

## Résultat attendu

Quand tu appelles `envoyer_message` avec un message, tu devrais recevoir un `MessageResponse` avec toutes les informations complétées (ID, date, etc.).
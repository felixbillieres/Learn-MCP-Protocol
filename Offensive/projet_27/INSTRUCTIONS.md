# Instructions - Projet 27 (Gestionnaire de Payloads)

## Ta mission

Créer un gestionnaire de payloads avec CRUD, validation et sélection intelligente.

## Étapes à suivre

1. **Crée les modèles Pydantic** :
   - `Payload` :
     - `id` : int
     - `nom` : str
     - `type` : str (enum: "exploit", "shell", "shellcode")
     - `os` : str (enum: "linux", "windows", "macos")
     - `architecture` : str (enum: "x86", "x64", "arm")
     - `description` : str | None
     - `code` : str (le payload lui-même)
     - `tags` : List[str]

2. **Crée les outils CRUD** :
   - `creer_payload` : Ajoute un nouveau payload
   - `lister_payloads` : Liste avec filtres (type, os, architecture)
   - `obtenir_payload` : Récupère un payload par ID
   - `supprimer_payload` : Supprime un payload

3. **Crée l'outil `selectionner_payload`** avec elicitation :
   - Demande le contexte (os, architecture, type)
   - Utilise elicitation pour confirmer le choix
   - Retourne le payload le plus adapté

4. **Crée la resource `payload://list`** :
   - Expose tous les payloads disponibles

5. **Valide les données** :
   - Vérifie que os/architecture sont compatibles
   - Valide le format du code

## Test

Utilise `python test.py` pour vérifier le CRUD et la sélection.


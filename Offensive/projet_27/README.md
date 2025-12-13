# Projet 27 : Gestionnaire de Payloads

## Objectif

Créer un serveur MCP pour gérer des payloads d'exploitation (exploits, shells, shellcodes) avec validation et sélection intelligente.

## Concepts à apprendre

### Payloads en sécurité offensive

Un payload est le code malveillant exécuté après l'exploitation d'une vulnérabilité :
- **Exploits** : Code qui exploite une vulnérabilité spécifique
- **Shells** : Interfaces de ligne de commande (reverse shell, bind shell)
- **Shellcodes** : Code machine pour exécution directe

### Architecture MCP

- **Tools** : CRUD pour payloads
- **Resources** : Exposer les payloads disponibles
- **Elicitation** : Sélectionner le payload adapté selon le contexte
- **Validation** : Vérifier la compatibilité OS/architecture

## Cas d'usage

- Stocker et organiser des payloads
- Sélectionner automatiquement le bon payload
- Valider la compatibilité avant utilisation
- Générer des payloads personnalisés


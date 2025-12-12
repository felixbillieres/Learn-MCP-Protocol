# Projet 09 : Resources avec templates URI

## Objectif

Apprendre à créer des resources avec des templates URI qui permettent des ressources paramétrées dynamiquement.

## Concepts à apprendre

### Qu'est-ce qu'un template URI ?

Un **template URI** est un modèle d'URI qui accepte des paramètres. Cela permet de créer des ressources dynamiques sans avoir à les déclarer toutes individuellement.

**Exemple** :
- Template : `file:///{path}`
- URI résolue : `file:///home/user/document.txt` (avec `path=/home/user/document.txt`)

### Templates vs Resources statiques

- **Resources statiques** : URI fixes, connues à l'avance (projet 08)
- **Resources avec templates** : URI dynamiques, générées à partir de paramètres

### Avantages des templates

- Moins de code répétitif
- Support de nombreuses ressources sans toutes les déclarer
- Flexibilité accrue

## Documentation MCP

Les templates utilisent le format [RFC 6570 URI Templates](https://datatracker.ietf.org/doc/html/rfc6570).

Exemple de template :
```
file:///{path}
config://{section}/{key}
```

## Ce que tu vas créer

Dans ce projet, tu vas créer un serveur qui expose des templates de ressources pour accéder à des fichiers de configuration dynamiques.

## Prochaines étapes

Lis `INSTRUCTIONS.md` pour voir ce que tu dois faire exactement !
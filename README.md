# RPG-textuel-au-tour-par-tour — Python

Application Python en ligne de commande simulant un RPG textuel dans un univers de ninjas, avec combats au tour par tour, techniques basées sur des mudras, inventaire, progression et plusieurs modes de jeu.

Projet réalisé dans un cadre universitaire.

---

## 1. Présentation générale

Le programme propose :

- Des combats au tour par tour entre ninjas  
- Des techniques reposant sur des affinités élémentaires (Feu, Eau, Terre, Vent, Tonnerre)  
- Un système de mudras (séquences à saisir) pour activer des techniques  
- Un mode Arène avec progression, loot et adversaires générés  
- Un mode Histoire structuré en chapitres avec dialogues et récompenses  
- Un didacticiel interactif pour découvrir les mécaniques du jeu  
- Une IA capable de s’adapter au contexte du combat  
- Une gestion des statistiques, objets, techniques et équipements  

---

## 2. Cahier des charges

### 2.1 Objectif général

Créer un RPG textuel complet comprenant :

- Un système de combat stratégique  
- Plusieurs modes de jeu (Arène, Histoire, Didacticiel)  
- Une progression du personnage  
- Un ensemble cohérent de techniques, objets, affinités et mécaniques internes  
- Une IA réactive selon la situation  
- Une architecture orientée objet  

### 2.2 Fonctionnalités prévues

#### a) Modes de jeu

**Mode Arène :**

- Combats successifs contre des ennemis générés procéduralement  
- Gain d’XP, nouveaux objets et nouvelles techniques  
- Deux difficultés : normal et difficile  

**Mode Histoire :**

- Succession de chapitres structurés  
- Dialogues introductifs  
- Ennemis prédéfinis  
- Récompenses scénarisées  

**Didacticiel :**

- Présentation guidée des mécaniques du jeu  
- Combats scriptés et explications  

#### b) Système de combat & ressources

- Fonctionnement au tour par tour  
- 1 action offensive maximale par tour  
- Jusqu’à 2 actions défensives  
- Attaques physiques (Taijutsu) ou utilisant le chakra (Ninjutsu, Genjutsu)  

**Ressources principales :**

- PV  
- Chakra  
- Endurance  
- Spiritualité  

**Affinités élémentaires (impact sur les dégâts) :**

Feu > Vent > Tonnerre > Terre > Eau > Feu  

#### c) Mécaniques spéciales

- Mudras : séquences à saisir pour activer des techniques  
- Inventaire : kunai, shuriken, pilules, parchemins…  
- Objets consommables ou équipements  
- Tentative de fuite : limitée et risquée  

IA capable de :

- Fuir  
- Se défendre  
- Utiliser des techniques adaptées  
- Adopter un comportement plus agressif en mode difficile  

#### d) Progression

- Gain d’XP en Arène  
- Amélioration progressive des statistiques  
- Déblocage de techniques plus puissantes  
- Récompenses fixes en mode Histoire  

#### e) Sauvegarde

- Une fonctionnalité de sauvegarde avait été étudiée mais n’a pas été intégrée, le chargement n’étant pas suffisamment fiable dans la version testée.

---

## 3. Architecture du projet

Architecture orientée objet comprenant les classes suivantes :

| Classe             | Rôle                                                                                           |
|--------------------|------------------------------------------------------------------------------------------------|
| `Ninja`            | Personnage jouable / ennemi (stats, affinité, inventaire, techniques, états, etc.)            |
| `Technique`        | Attaques et actions nécessitant mudras et chakra (coût, dégâts, affinités…)                  |
| `Objet`            | Consommables et équipements (effets, rareté, utilisation)                                     |
| `GestionnaireMudras` | Vérification et validation des séquences de mudras saisies par le joueur                    |
| `Combat`           | Gestion complète d’un affrontement (tours, IA, fin de combat, affichage)                      |
| `Arène`            | Génération d’ennemis, gestion de l’XP, des récompenses et de la difficulté                    |
| `Histoire`         | Chapitres, dialogues, liste d’ennemis associés, récompenses et progression de l’aventure      |

---

## 4. Difficultés rencontrées

### 4.1 Adaptation de la POO au Python

- Passage depuis une logique Java vers Python (`__init__`, `isinstance`, `getattr`, etc.)  
- Réécriture des classes `Ninja`, `Technique`, `Objet` dans un style plus idiomatique Python  

### 4.2 Timer du mode difficile

- Timer fonctionnel mais affichage temps réel peu lisible dans la console  
- Le choix a été fait de ne pas conserver cette mécanique dans la version actuelle  

### 4.3 Sauvegarde / chargement

- Tests instables sur la lecture/écriture structurée (pertes de données, format fragile)  
- Fonction retirée de la version finale  

---

## 5. Exemple d’un chapitre du mode Histoire

```python
chapitres[1] = {
    'titre': "L'Examen Genin",
    'description': "...",
    'dialogueIntro': [...],
    'ennemis': [
        {'nom': 'Shikamaru Nara', 'niveau': 1, 'affinite': 'Vent'},
        {'nom': 'Shoji Akimichi', 'niveau': 1, 'affinite': 'Terre'},
        {'nom': 'Sasuke Uchiha', 'niveau': 2, 'affinite': 'Feu'}
    ],
    'dialogueFin': [...],
    'recompenses': {
        'xp': 100,
        'technique': 'Kage Bunshin no Jutsu',
        'objet': 'Bandeau de Konoha'
    }
}

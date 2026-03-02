Voici une version **entièrement prête à copier-coller** dans ton `README.md` :

---

# 🎮 Mar&Maj – Jeu de Labyrinthe en Terminal (Python + Curses)

Projet de jeu développé en Python utilisant la bibliothèque **curses** pour créer une interface interactive directement dans le terminal.

---

# 🚀 Installation Rapide

## 📦 Prérequis

* Python 3.10+
* Terminal compatible curses

### Sous Windows

Installez le module nécessaire :

```powershell
pip install windows-curses
```

### Sous Linux / macOS

La bibliothèque `curses` est généralement incluse par défaut.

---

# ▶️ Lancer le Jeu

Depuis le dossier du projet :

```bash
python JeuCurses.py
```

---

# 🎯 Objectif du Jeu

Le joueur doit :

* Se déplacer dans un labyrinthe
* Collecter des objets
* Atteindre la sortie
* Gérer un nombre limité de déplacements (dans les niveaux avancés)
* Optimiser ses mouvements pour éviter la défaite

---

# 🎮 Contrôles

* ⬆️⬇️⬅️➡️ Flèches directionnelles : déplacement
* Une touche quelconque : continuer après un message

---

# 🧩 Niveaux Disponibles

## 🟢 Niveau 1

* Introduction au jeu
* Déplacement libre
* Collecte d’objets
* Atteindre la sortie

---

## 🔵 Niveau 2

* Nouveau labyrinthe
* Réinitialisation de la position
* Collecte d’objets obligatoire

---

## 🟡 Niveau 3

* Nombre de déplacements limité
* Défaite si les mouvements atteignent 0
* Redémarrage automatique en cas d’échec

---

## 🔴 Niveau 4

* Déplacements limités

* Introduction d’objets spéciaux :

  * ⭐ Objet bonus → +3 mouvements
  * ❌ Objet malus → -3 mouvements

* Gestion dynamique des mouvements restants

* Messages informatifs lors de la collecte

---

# 🧠 Architecture du Projet

## 🎨 Affichage

* `draw_maze_with_char_and_items()`
* `draw_maze_with_char_and_itemsniv4()`

Ces fonctions affichent :

* Le labyrinthe
* Les objets
* Le joueur

---

## 🚶 Déplacement

* `update_p()`

Met à jour la position du joueur selon la touche pressée.

---

## ⭐ Gestion des Objets

* `collect_items()`
* `collect_itemsniv4()`

Permet :

* De supprimer un objet collecté
* De modifier le nombre de mouvements restants (niveau 4)

---

# 📁 Structure du Projet

```
MarMaj/
├── JeuCurses.py
└── README.md
```

---

# 🧠 Concepts Programmatiques Utilisés

* Programmation modulaire
* Gestion d’état (mouvements restants)
* Manipulation de listes
* Suppression sécurisée d’éléments lors d’itérations
* Gestion des erreurs (`IndexError`)
* Interface interactive avec curses
* Conditions de victoire / défaite

---

# ⚠️ Difficultés Rencontrées

* Gestion des coordonnées hors limites
* Débogage avec curses (les `print` ne s’affichent pas normalement)
* Mise à jour correcte des variables entre fonctions
* Gestion dynamique des objets bonus/malus

---

# 🔮 Améliorations Possibles

* Génération aléatoire de labyrinthes
* Système de score global
* Ajout d’un chronomètre
* Menu principal interactif
* Système de sauvegarde
* Version graphique (Tkinter / Pygame)
* Ajout d’ennemis



# Cas Technique - Analytics Engineer - Équipe Data Dougs

## 🗓️ Introduction

Cher candidat(e),

Dans quelques jours, tu rencontreras l’**équipe Data de Dougs**. Une partie de l’entretien sera consacrée à la **restitution du cas technique** présenté ici.

Nous t'invitons à lire attentivement les instructions ci-dessous et à préparer le cas en autonomie. S’il te manque des informations, tu es libre de prendre des hypothèses que tu devras expliciter lors de l'entretien.

Néanmoins, si tu rencontres des difficultés ou que tu as des questions, n’hésite pas à contacter **marie.lefevre@dougs.fr** en amont.

**Bonne préparation !**

---

## 🧐 Mise en Contexte

Tu viens d’arriver chez Dougs en tant qu’**Analytics Engineer**. Félicitations !

Dans ce projet git, tu trouveras :
* Le code d’un **DAG Airflow**
* **4 fichiers CSV** qui sont nos sources de données brutes
* Les **codes SQL** utilisés dans notre outil **dbt**

Ta **première mission** est de comprendre l’**architecture data existante** et de proposer des **améliorations** sur ce qui est en place actuellement.

Pour cela, crée une branche de travail à partir de ce *repository*. Tu feras les *commits* que tu souhaites implémenter dans cette **branche distincte**.


---

## 📦 Livrable Attendu

Avant le jour de l’entretien, envoie-nous par mail :

### 1. Présentation (1 à 3 pages ou slides)
Une présentation (document ou slides) de :
* Ta vision de l’**architecture data** présentée ici
* Ce qui, selon toi, **ne convient pas**
* Ce que tu **suggères d’améliorer** et **pourquoi**

### 2. Code
Le **zip de ton code** avec ta **branche prête pour être *mergée*** dans `main`.

---

## ⏱️ Estimation de Temps et Entretien

* Ce travail devrait te prendre **entre 4 et 6 heures**.
* Le jour de l’entretien, nous échangerons sur ton livrable et ferons quelques manipulations ensemble.

---

## 💡 Conseils Techniques

* Le DAG présenté ici a été créé spécifiquement pour ce test : il prend des données CSV pour les exporter vers un *dataset* **BigQuery** (de façon factice).
* Nous attendons de toi que tu **améliores le code** mais **pas que tu réussisses à faire tourner le DAG**. L'objectif est l'**analyse** et la **proposition d'amélioration** de l'architecture.
# **Extraction Automatique d'Offres d'Emploi et Analyse des Tendances du Marché**

Ce projet consiste à automatiser l'extraction d'offres d'emploi à partir d'un site web en utilisant Python et BeautifulSoup,
et à analyser ces données pour identifier les tendances du marché du travail dans une région spécifique grâce à Power BI.

---

## **1. Objectif du Projet**

- Automatiser la collecte d'offres d'emploi publiées en ligne.
- Analyser les tendances du marché du travail (titres populaires, lieux géographiques, évolution des offres dans le temps).
- Faciliter la prise de décision pour les chercheurs d'emploi ou les responsables RH.

---

## **2. Fonctionnalités**

### **A. Extraction Automatique des Données**
- Récupération des offres d'emploi depuis un site web (ex. https://emploi.afrikinterim.com).
- Nettoyage des données pour éliminer les erreurs d'encodage ou les incohérences.
- Sauvegarde des données dans un fichier CSV structuré.

### **B. Analyse des Tendances avec Power BI**
- Visualisations dynamiques incluant :
  - Répartition géographique des offres.
  - Évolution temporelle des offres.
---

## **3. Technologies Utilisées**

### **Backend : Extraction Automatique**
- **Langage** : Python
- **Bibliothèques principales** :
  - `requests` : pour accéder au site web.
  - `BeautifulSoup` : pour le parsing HTML.
  - `re` : pour le nettoyage des données.
  - `pandas` : pour manipuler les données et créer des fichiers CSV.

### **Frontend : Analyse des Données**
- **Outil de visualisation** : Power BI
- **Fichier source** : fichier CSV contenant les données extraites.

---

## **4. Architecture du Projet**

### **Étape 1 : Extraction Automatique**
1. Collecte des données sur plusieurs pages web.
2. Parsing des éléments HTML pour extraire :
   - Titre de l'offre.
   - Date de publication.
   - Localisation de l'emploi.
3. Nettoyage des données et gestion des encodages.
4. Enregistrement dans un fichier CSV.

### **Étape 2 : Analyse avec Power BI**
1. Importation des données depuis le fichier CSV.
2. Création de tableaux de bord interactifs pour visualiser :
   - Les titres de postes les plus populaires.
   - Les régions avec le plus d'offres.
   - Les tendances temporelles.

---

## **5. Résultats Attendus**
- Des visualisations dynamiques pour explorer les tendances du marché.
- Des insights exploitables pour mieux comprendre les opportunités d'emploi dans une région donnée.

---

## **6. Exemple d'Exécution**

### **Extrait de Données CSV**

| Titre               | Date        | Lieu                             |
|---------------------|-------------|-----------------------------------|
| Chef Mécanicien     | 27/01/2025  | Katanga, République démocratique du Congo |
| Ingénieur Logiciel  | 25/01/2025  | Kinshasa, République démocratique du Congo |
| Analyste Financier  | 20/01/2025  | Lubumbashi, République démocratique du Congo |

### **Exemple de Tableau de Bord Power BI**

- Répartition géographique :
 ![powerBI](https://github.com/user-attachments/assets/cefa8a86-58f3-492c-9475-ff948369437d)
---

## **7. Comment Utiliser ce Projet**

### **Étape 1 : Extraction Automatique**
1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   ```
2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```
3. Exécutez le script Python pour extraire les données :
   ```bash
   python job_extractor.py
   ```
4. Consultez le fichier `jobfair_cleaned.csv` généré dans le répertoire du projet.

### **Étape 2 : Analyse des Tendances**
1. Ouvrez Power BI Desktop.
2. Chargez le fichier `jobfair_cleaned.csv`.
3. Explorez et personnalisez le tableau de bord selon vos besoins.

---

## **8. Améliorations Futures**
- Ajouter des fonctionnalités de scraping pour d'autres sites d'emploi.
- Développer un modèle prédictif pour anticiper les évolutions du marché.
- Automatiser la mise à jour des données pour un suivi en temps réel.

---

## **9. Conclusion**
Ce projet combine l'extraction de données web et l'analyse visuelle pour fournir des insights exploitables sur les tendances du marché du travail.
Il s'agit d'un outil pratique pour quiconque souhaite suivre et analyser les opportunités d'emploi dans une région spécifique.

---

## **10. Auteur**
- **Nom** : [ISSA Fiti]
- **Contact** : [Issafiti02@gmail.com]
---

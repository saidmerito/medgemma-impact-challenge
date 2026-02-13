# ✅ Checklist de Déploiement Streamlit Cloud

## 📋 Avant de déployer

### 1. Fichiers requis à la racine du repository GitHub

- [ ] `app.py` - Application principale
- [ ] `requirements.txt` - Dépendances Python
- [ ] `packages.txt` - Dépendances système (optionnel)
- [ ] `src/` - Dossier avec les modules Python
- [ ] `README.md` - Documentation

### 2. Contenu de requirements.txt

Vérifiez que votre `requirements.txt` contient au minimum:

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
Pillow>=10.0.0
openpyxl>=3.1.0
python-dotenv>=1.0.0
```

### 3. Structure du projet

```
votre-repo/
├── app.py                 ✅ REQUIS
├── requirements.txt       ✅ REQUIS
├── packages.txt          ⚪ Optionnel
├── README.md             ✅ RECOMMANDÉ
├── .streamlit/
│   └── config.toml       ⚪ Optionnel
└── src/
    ├── __init__.py       ✅ REQUIS
    ├── medgemma_processor.py  ✅ REQUIS
    └── utils.py          ✅ REQUIS
```

### 4. Fichiers à NE PAS commiter

Ajoutez ceci dans `.gitignore`:

```
venv/
.env
__pycache__/
*.pyc
.DS_Store
*.log
```

## 🚀 Étapes de Déploiement sur Streamlit Cloud

### Étape 1: Préparer GitHub

```bash
# 1. Initialiser git (si pas déjà fait)
git init

# 2. Ajouter .gitignore
cat > .gitignore << EOF
venv/
.env
__pycache__/
*.pyc
.DS_Store
*.log
data/
test_data/
EOF

# 3. Ajouter tous les fichiers
git add .

# 4. Commit
git commit -m "Initial commit - Project Sentinel"

# 5. Créer un repo sur GitHub
# Allez sur github.com et créez un nouveau repository

# 6. Lier et pousser
git remote add origin https://github.com/VOTRE_USERNAME/project-sentinel.git
git branch -M main
git push -u origin main
```

### Étape 2: Déployer sur Streamlit Cloud

1. **Allez sur [share.streamlit.io](https://share.streamlit.io)**

2. **Connectez-vous avec GitHub**

3. **Cliquez sur "New app"**

4. **Remplissez le formulaire:**
   - Repository: `VOTRE_USERNAME/project-sentinel`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL: `project-sentinel` (ou nom personnalisé)

5. **Cliquez sur "Deploy!"**

6. **Attendez le déploiement** (2-3 minutes)

### Étape 3: Configuration des Secrets (si nécessaire)

Si vous utilisez des variables d'environnement:

1. **Dans Streamlit Cloud, allez dans "Settings"**

2. **Cliquez sur "Secrets"**

3. **Ajoutez vos secrets au format TOML:**

```toml
HF_TOKEN = "votre_token_huggingface"
MODEL_NAME = "google/medgemma-1.5-4b-it"

[password]
password = "votre_mot_de_passe"
```

4. **Sauvegardez**

## 🔍 Vérification Post-Déploiement

### Tests à effectuer:

- [ ] L'application se charge sans erreurs
- [ ] Les 3 pages sont accessibles (Upload, Statistiques, À Propos)
- [ ] L'upload de fichier fonctionne
- [ ] Le bouton "Analyser" fonctionne
- [ ] Les graphiques s'affichent correctement
- [ ] L'export Excel/CSV/JSON fonctionne
- [ ] Le design est correct (couleurs, mise en page)

### Si l'application crash:

1. **Vérifier les logs:**
   - Cliquez sur "Manage app"
   - Regardez les logs en temps réel
   - Identifiez l'erreur

2. **Erreurs communes:**

   **a) ModuleNotFoundError:**
   ```
   Solution: Vérifier requirements.txt
   ```

   **b) File not found:**
   ```
   Solution: Vérifier que tous les fichiers sont sur GitHub
   ```

   **c) Import error:**
   ```
   Solution: Vérifier la structure des dossiers (src/__init__.py)
   ```

3. **Corriger et redéployer:**
   ```bash
   # Corriger le problème localement
   git add .
   git commit -m "Fix: correction du bug XYZ"
   git push
   
   # Streamlit Cloud redéploiera automatiquement
   ```

## 📝 Template requirements.txt Minimaliste

Si vous avez des problèmes, utilisez cette version ultra-minimaliste:

```
streamlit==1.28.0
pandas==2.0.0
plotly==5.17.0
Pillow==10.0.0
openpyxl==3.1.0
```

## 🎯 URLs Utiles

Une fois déployé, votre application sera accessible à:

```
https://VOTRE_USERNAME-project-sentinel-app-XXXXX.streamlit.app
```

Ou avec URL personnalisée:

```
https://project-sentinel.streamlit.app
```

## 🔄 Mises à Jour

Pour mettre à jour l'application déployée:

```bash
# 1. Faire vos modifications localement

# 2. Tester localement
streamlit run app.py

# 3. Commiter et pousser
git add .
git commit -m "Update: description des changements"
git push

# Streamlit Cloud redéploie automatiquement!
```

## 🆘 Dépannage Rapide

### L'app ne démarre pas

```bash
# Vérifier que requirements.txt est à jour
cat requirements.txt

# Tester en local d'abord
streamlit run app.py

# Si ça marche en local, le problème vient du déploiement
```

### Erreur de build

```
# Souvent dû à des versions incompatibles
# Utiliser des versions exactes dans requirements.txt:
streamlit==1.28.0
pandas==2.0.0
```

### L'app est lente

```
# Optimiser les imports
# Utiliser st.cache_data pour les fonctions coûteuses
# Réduire la taille des images
```

## 📞 Ressources

- **Documentation Streamlit Cloud:** https://docs.streamlit.io/streamlit-community-cloud
- **Forum Streamlit:** https://discuss.streamlit.io
- **Status Streamlit:** https://streamlit.status.io

## ✨ Conseils Pro

1. **Testez toujours en local avant de pousser**
2. **Utilisez des versions exactes dans requirements.txt pour la production**
3. **Activez les analytics dans Streamlit Cloud pour suivre l'usage**
4. **Utilisez des secrets pour les données sensibles**
5. **Documentez bien votre README pour les visiteurs**

---

**Bon déploiement ! 🚀**

Une fois déployé, n'oubliez pas de:
- ✅ Tester toutes les fonctionnalités
- ✅ Partager l'URL
- ✅ Créer votre vidéo de démo
- ✅ Soumettre au MedGemma Impact Challenge

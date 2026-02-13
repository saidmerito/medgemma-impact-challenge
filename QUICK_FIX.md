# 🔧 FIX RAPIDE - Erreur ModuleNotFoundError

## ❌ Erreur actuelle:
```
ModuleNotFoundError: No module named 'plotly'
```

## ✅ SOLUTION IMMÉDIATE

### Si vous êtes sur Streamlit Cloud:

1. **Vérifiez que `requirements.txt` existe à la racine de votre repo GitHub**

2. **Le contenu EXACT de `requirements.txt` doit être:**

```txt
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
Pillow>=10.0.0
openpyxl>=3.1.0
python-dotenv>=1.0.0
```

3. **Commit et push:**

```bash
git add requirements.txt
git commit -m "Fix: update requirements.txt"
git push
```

4. **Redémarrez l'app dans Streamlit Cloud:**
   - Allez dans "Manage app"
   - Cliquez sur "Reboot app"

### Si vous êtes en local:

```bash
# 1. Allez dans le dossier du projet
cd project-sentinel

# 2. Activez l'environnement virtuel
source venv/bin/activate  # Linux/Mac
# OU
venv\Scripts\activate  # Windows

# 3. Installez les dépendances
pip install streamlit pandas numpy plotly Pillow openpyxl python-dotenv

# 4. Vérifiez l'installation
pip list | grep plotly

# 5. Lancez l'app
streamlit run app.py
```

## 📋 Checklist de vérification:

- [ ] Le fichier `requirements.txt` est à la **racine** du projet (pas dans un sous-dossier)
- [ ] Le fichier `requirements.txt` contient bien les 7 packages listés ci-dessus
- [ ] Vous avez fait `git add requirements.txt` puis `git push`
- [ ] Vous avez redémarré l'application

## 🆘 Si ça ne marche toujours pas:

### Vérifiez la structure de votre projet GitHub:

```
votre-repo/
├── app.py              ✅ DOIT être ici
├── requirements.txt    ✅ DOIT être ici
├── src/
│   ├── __init__.py
│   ├── medgemma_processor.py
│   └── utils.py
└── .streamlit/
    └── config.toml
```

### Créez requirements.txt manuellement:

```bash
# Dans votre repo GitHub, créez un fichier requirements.txt avec:

cat > requirements.txt << 'EOF'
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
Pillow>=10.0.0
openpyxl>=3.1.0
python-dotenv>=1.0.0
EOF

git add requirements.txt
git commit -m "Add requirements.txt"
git push
```

## 💡 Installation Alternative (Version Minimale)

Si vous voulez juste faire marcher l'app rapidement:

**requirements.txt version ultra-simple:**

```
streamlit
pandas
plotly
Pillow
openpyxl
```

Cette version installe les dernières versions de chaque package.

## ✅ Test Rapide

Pour vérifier que tout fonctionne:

```bash
# Testez chaque import
python -c "import streamlit; print('✅ streamlit OK')"
python -c "import pandas; print('✅ pandas OK')"
python -c "import plotly; print('✅ plotly OK')"
python -c "import PIL; print('✅ Pillow OK')"
python -c "import openpyxl; print('✅ openpyxl OK')"
```

Si tous affichent "✅ ... OK", alors l'app devrait fonctionner!

---

**Cette erreur est 99% du temps due à un `requirements.txt` manquant ou mal placé. Vérifiez qu'il est bien à la racine de votre repository GitHub !**

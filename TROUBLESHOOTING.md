# 🔧 Guide de Dépannage - Project Sentinel

## ❌ Erreur: ModuleNotFoundError

### Symptôme
```
ModuleNotFoundError: No module named 'plotly'
```
ou
```
ModuleNotFoundError: No module named 'pandas'
```

### Solution

#### Sur Streamlit Cloud:

1. **Vérifiez requirements.txt**
   - Le fichier doit être à la racine du projet
   - Doit contenir toutes les dépendances

2. **Contenu minimal de requirements.txt:**
   ```
   streamlit>=1.28.0
   pandas>=2.0.0
   numpy>=1.24.0
   plotly>=5.17.0
   Pillow>=10.0.0
   openpyxl>=3.1.0
   python-dotenv>=1.0.0
   ```

3. **Redéployer l'application:**
   - Allez dans "Manage app"
   - Cliquez sur "Reboot app"
   - Ou faites un nouveau commit sur GitHub

#### En local:

```bash
# 1. Activer l'environnement virtuel
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Vérifier l'installation
pip list | grep -E "streamlit|plotly|pandas"

# 4. Si ça ne marche toujours pas, réinstaller
pip install --upgrade --force-reinstall streamlit plotly pandas numpy pillow openpyxl
```

## ❌ Erreur: Port déjà utilisé

### Symptôme
```
OSError: [Errno 98] Address already in use
```

### Solution

```bash
# Trouver le processus
lsof -i :8501

# Tuer le processus
kill -9 [PID]

# Ou utiliser un autre port
streamlit run app.py --server.port 8502
```

## ❌ Erreur: Python version

### Symptôme
```
Python 3.7 or higher is required
```

### Solution

```bash
# Vérifier la version
python --version

# Installer Python 3.9+
# Ubuntu/Debian:
sudo apt update
sudo apt install python3.9

# Mac:
brew install python@3.9

# Windows: Télécharger depuis python.org
```

## ❌ Erreur: Permission denied (run.sh)

### Symptôme
```
bash: ./run.sh: Permission denied
```

### Solution

```bash
# Donner les permissions d'exécution
chmod +x run.sh

# Puis lancer
./run.sh
```

## ❌ Erreur: No module named 'src'

### Symptôme
```
ModuleNotFoundError: No module named 'src'
```

### Solution

```bash
# Vérifier que vous êtes dans le bon répertoire
pwd  # Devrait afficher .../project-sentinel

# Vérifier la structure
ls -la src/

# Si src/ n'existe pas, vous êtes au mauvais endroit
cd project-sentinel
```

## ❌ L'application ne s'ouvre pas automatiquement

### Solution

```bash
# Ouvrir manuellement dans le navigateur
# L'URL sera affichée dans le terminal, généralement:
http://localhost:8501

# Ou forcer l'ouverture
streamlit run app.py --server.headless false
```

## ❌ Erreur: Streamlit Cloud - App crashed

### Sur Streamlit Cloud:

1. **Vérifier les logs**
   - Cliquez sur "Manage app"
   - Regardez les logs en temps réel

2. **Problèmes courants:**

   **a) requirements.txt manquant**
   ```
   Solution: Créer requirements.txt à la racine
   ```

   **b) Fichiers manquants**
   ```
   Solution: Vérifier que src/, app.py sont sur GitHub
   ```

   **c) Secrets non configurés**
   ```
   Solution: Ajouter les secrets dans les paramètres Streamlit Cloud
   ```

## ❌ Erreur: Import error avec MedGemma

### Symptôme
```
ImportError: cannot import name 'AutoModelForVision2Seq'
```

### Solution

Le code actuel est en **mode démo** et n'utilise PAS le vrai MedGemma.

Pour utiliser le vrai modèle:

1. **Installer PyTorch et Transformers:**
   ```bash
   pip install torch transformers accelerate
   ```

2. **Décommenter dans `src/medgemma_processor.py`:**
   ```python
   # Ligne ~30-40, décommenter:
   from transformers import AutoModelForVision2Seq, AutoProcessor
   self.processor = AutoProcessor.from_pretrained(self.model_name)
   self.model = AutoModelForVision2Seq.from_pretrained(...)
   ```

3. **Ajouter votre token HuggingFace:**
   ```bash
   # Dans .env
   HF_TOKEN=votre_token_ici
   ```

## 🔍 Diagnostic Complet

Si vous avez toujours des problèmes, lancez ce script de diagnostic:

```bash
#!/bin/bash
echo "=== Diagnostic Project Sentinel ==="
echo ""
echo "Python version:"
python --version
echo ""
echo "Pip version:"
pip --version
echo ""
echo "Répertoire actuel:"
pwd
echo ""
echo "Structure du projet:"
ls -la
echo ""
echo "Contenu de src/:"
ls -la src/ 2>/dev/null || echo "Dossier src/ non trouvé!"
echo ""
echo "Packages installés:"
pip list | grep -E "streamlit|plotly|pandas|numpy|pillow"
echo ""
echo "Environnement virtuel:"
which python
echo ""
```

Sauvegardez ce script comme `diagnostic.sh`, rendez-le exécutable (`chmod +x diagnostic.sh`) et lancez-le (`./diagnostic.sh`).

## 📝 Checklist de Vérification

Avant de lancer l'application:

- [ ] Python 3.9+ installé
- [ ] Dans le dossier `project-sentinel/`
- [ ] Environnement virtuel activé
- [ ] `requirements.txt` présent
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Dossier `src/` présent avec les fichiers Python
- [ ] Fichier `app.py` présent
- [ ] Port 8501 disponible

## 🆘 Besoin d'aide supplémentaire?

### Installation minimale qui fonctionne à coup sûr:

```bash
# 1. Créer un nouveau dossier
mkdir test-sentinel
cd test-sentinel

# 2. Créer requirements.txt
cat > requirements.txt << EOF
streamlit==1.28.0
pandas==2.0.0
plotly==5.17.0
Pillow==10.0.0
openpyxl==3.1.0
EOF

# 3. Installer
pip install -r requirements.txt

# 4. Copier app.py depuis le projet
cp ../project-sentinel/app.py .
cp -r ../project-sentinel/src .

# 5. Lancer
streamlit run app.py
```

## 💡 Astuces

### Pour Streamlit Cloud:

1. **Toujours avoir ces fichiers à la racine:**
   - `app.py`
   - `requirements.txt`
   - `.streamlit/config.toml` (optionnel)

2. **Structure minimale:**
   ```
   votre-repo/
   ├── app.py
   ├── requirements.txt
   └── src/
       ├── __init__.py
       ├── medgemma_processor.py
       └── utils.py
   ```

3. **Ne PAS inclure:**
   - `venv/`
   - `.env`
   - `__pycache__/`
   - Fichiers de données sensibles

### Pour développement local:

1. **Toujours utiliser un environnement virtuel**
2. **Mettre à jour pip régulièrement:** `pip install --upgrade pip`
3. **Nettoyer le cache si problème:** `pip cache purge`

## 📞 Support

Si rien ne fonctionne, partagez:

1. Votre système d'exploitation
2. Version de Python (`python --version`)
3. Message d'erreur complet
4. Sortie de `pip list`
5. Contenu de `requirements.txt`

---

**La plupart des problèmes viennent de dépendances manquantes. Assurez-vous que `requirements.txt` est correct et que toutes les dépendances sont installées !**

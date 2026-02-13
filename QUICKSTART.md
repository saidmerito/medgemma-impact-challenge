# 🚀 Quick Start Guide - Project Sentinel

## Installation Rapide (5 minutes)

### Option 1: Linux/Mac

```bash
# 1. Télécharger et extraire le projet
unzip project-sentinel.zip
cd project-sentinel

# 2. Lancer le script d'installation
chmod +x run.sh
./run.sh
```

### Option 2: Windows

```batch
# 1. Extraire le projet
# 2. Double-cliquer sur run.bat
```

## Première Utilisation

1. **L'application s'ouvre automatiquement** dans votre navigateur à `http://localhost:8501`

2. **Téléverser une image de registre**
   - Cliquez sur "Browse files"
   - Sélectionnez une photo de votre registre médical

3. **Analyser**
   - Cliquez sur "🚀 Analyser le registre"
   - Attendez 10-15 secondes

4. **Vérifier et Exporter**
   - Vérifiez les données extraites
   - Exportez en Excel, CSV ou JSON

## Exemples de Registres à Tester

Des images de test sont disponibles dans `test_data/`:
- `test_data/sample_register_1.jpg` - Registre de consultation
- `test_data/sample_register_2.jpg` - Registre de vaccination
- `test_data/sample_register_3.jpg` - Registre de morbidité

## Résolution de Problèmes

### L'application ne démarre pas

```bash
# Vérifier Python
python3 --version

# Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall
```

### Port déjà utilisé

```bash
# Utiliser un autre port
streamlit run app.py --server.port 8502
```

### Erreur d'importation

```bash
# Activer l'environnement virtuel
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Réinstaller
pip install -r requirements.txt
```

## Configuration Avancée

### Utiliser avec un GPU (optionnel)

```bash
# Éditer .env
DEVICE=cuda

# Installer PyTorch avec CUDA
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### Changer la langue

Dans l'interface, utilisez la barre latérale pour choisir:
- Français
- English
- Wolof (bientôt disponible)

## Support

- 📧 Email: support@projectsentinel.org
- 📖 Documentation complète: README.md
- 🐛 Signaler un bug: GitHub Issues

---

**Bon usage ! 🎉**

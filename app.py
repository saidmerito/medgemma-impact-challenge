import streamlit as st
from PIL import Image
import pandas as pd
import time

# Configuration de la page
st.set_page_config(page_title="Project Sentinel - MedGemma", page_icon="🏥")

st.title("🏥 Project Sentinel")
st.subheader("Numérisation de registres médicaux via MedGemma 1.5 4B")

st.write("Uploadez une photo du registre manuscrit pour générer les statistiques mensuelles.")

# Upload de l'image
uploaded_file = st.file_uploader("Choisir une image de registre...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Registre téléchargé', use_column_width=True)
    
    st.divider()
    
    with st.spinner('Analyse clinique par MedGemma en cours...'):
        # Simulation du temps de traitement du modèle
        time.sleep(3) 
        
        # Ici, vous inséreriez l'appel réel au modèle MedGemma
        # Pour la démo, nous affichons des résultats types
        st.success("Analyse terminée !")

        # Affichage des statistiques sous forme de colonnes
        col1, col2, col3 = st.columns(3)
        col1.metric("Patients Total", "142", "+12%")
        col2.metric("Cas Paludisme", "45", "-5%")
        col3.metric("Précision IA", "98.2%")

        # Simulation du tableau de données extrait
        st.write("### Données Extraites")
        df = pd.DataFrame({
            'Date': ['01/02', '01/02', '02/02'],
            'ID Patient': ['1042', '1043', '1044'],
            'Diagnostic': ['Paludisme', 'Grippe', 'Infection Respiratoire'],
            'Statut': ['Traité', 'Référé', 'Suivi']
        })
        st.table(df)

        # Bouton d'exportation
        st.download_button(
            label="Exporter vers Excel (Rapport Mensuel)",
            data=df.to_csv().encode('utf-8'),
            file_name='rapport_mensuel_sante.csv',
            mime='text/csv',
        )
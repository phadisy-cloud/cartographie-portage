import streamlit as st
from PIL import Image
import os

# 1. Configure the web page
st.set_page_config(layout="wide", page_title="Cartographie Portage à Domicile")
st.title("Cartographie des communes - Portage à domicile")

# 2. Define the regions and their respective image files
regions = {
    "Ambert": "ambert.png",
    "Thiers": "thiers.png",
    "Beaumont": "beaumont.png",
    "Billom": "billom.png",
    "Ceyrat": "ceyrat.png",
    "Etap-auvergne": "etap-auvergne.png",
    "Mond'Arverne ": "mondarverne.png"
}

# 3. Create a split layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Carte des territoires")
    
    # Using your exact updated PNG filename!
    main_map_path = "cartographie des communes et enquetes portage à domicile.png"
    
    if os.path.exists(main_map_path):
        main_map = Image.open(main_map_path)
        st.image(main_map, use_container_width=True)
    else:
        st.warning(f"⚠️ Image de la carte introuvable. Vérifiez que le nom '{main_map_path}' est exact dans votre dossier.")

    # Create a dropdown menu to select the region
    st.markdown("### 🔍 Sélectionnez une région :")
    selected_region = st.selectbox(
        "Choisissez un territoire pour voir son resulta :", 
        list(regions.keys())
    )

with col2:
    st.subheader(f"Infographie : {selected_region}")
    
    # 4. Display the infographic for the chosen region
    image_path = regions[selected_region]
    
    if os.path.exists(image_path):
        img = Image.open(image_path)
        st.image(img, use_container_width=True)
    else:
        st.error(f"⚠️ Image introuvable : '{image_path}'. Vérifiez le nom du fichier dans votre dossier 'maportage'.")
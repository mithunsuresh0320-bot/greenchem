import streamlit as st
import joblib
import pubchempy as pcp

# Load model & vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Convert name → SMILES
def name_to_smiles(name):
    try:
        compounds = pcp.get_compounds(name, 'name')
        if compounds:
            return compounds[0].canonical_smiles
    except:
        return None
    return None

# Get molecule image from PubChem
def get_image_url(smiles):
    return f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{smiles}/PNG"

# UI
st.set_page_config(page_title="Green Chemistry AI", page_icon="🌱")

st.title("🌱 Green Chemistry AI")
st.markdown("### Predict Eco-Friendly Chemicals 🌍")

user_input = st.text_input("Enter Chemical Name or SMILES")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter something")
    else:
        smiles = name_to_smiles(user_input)

        if smiles:
            st.info(f"🔬 SMILES: {smiles}")
        else:
            smiles = user_input

        # Predict
        X = vectorizer.transform([smiles])
        prediction = model.predict(X)[0]
        prob = model.predict_proba(X)[0]

        green_score = round(prob[1] * 100, 2)

        if prediction == 1:
            st.success(f"✅ Eco-Friendly ({green_score}%)")
        else:
            st.error(f"❌ Harmful ({100 - green_score}%)")

        # Show molecule image (NO RDKit)
        image_url = get_image_url(smiles)
        st.image(image_url, caption="🧬 Molecule Structure")
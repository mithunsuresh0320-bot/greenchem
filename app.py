import streamlit as st
import joblib
import pubchempy as pcp

# -------------------------------
# PAGE SETTINGS
# -------------------------------
st.set_page_config(page_title="Green Chemistry AI", page_icon="🌱")

st.title("🌱 Green Chemistry AI")
st.write("Predict whether a chemical is eco-friendly")

# -------------------------------
# LOAD MODEL
# -------------------------------
try:
    model = joblib.load("model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# -------------------------------
# NAME → SMILES
# -------------------------------
def name_to_smiles(name):
    try:
        compounds = pcp.get_compounds(name, 'name')
        if compounds:
            return compounds[0].canonical_smiles
    except:
        pass
    return None

# -------------------------------
# INPUT
# -------------------------------
user_input = st.text_input("Enter Chemical Name or SMILES:")

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a chemical")
    else:
        smiles = name_to_smiles(user_input)

        if smiles:
            st.info(f"🔬 SMILES: {smiles}")
        else:
            smiles = user_input

        try:
            X = vectorizer.transform([smiles])

            # 🔥 GET PROBABILITIES
            prob = model.predict_proba(X)[0]

            eco_prob = prob[0] * 100
            harm_prob = prob[1] * 100

            # 🔥 75% RULE
            if eco_prob >= 75:
                st.success(f"✅ Eco-Friendly ({eco_prob:.2f}%)")
            else:
                st.error(f"❌ Harmful ({harm_prob:.2f}%)")

        except Exception as e:
            st.error(f"❌ Prediction error: {e}")

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
# LOAD MODEL (SAFE)
# -------------------------------
try:
    model = joblib.load("model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()  # stop app if model not loaded

# -------------------------------
# FUNCTION: NAME → SMILES
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
# INPUT UI
# -------------------------------
user_input = st.text_input("Enter Chemical Name or SMILES:")

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a chemical")
    else:
        # Convert name → SMILES
        smiles = name_to_smiles(user_input)

        if smiles:
            st.info(f"🔬 SMILES: {smiles}")
        else:
            smiles = user_input

        try:
            # ML Prediction
            X = vectorizer.transform([smiles])
            pred = model.predict(X)[0]
            prob = model.predict_proba(X)[0]

            score = round(prob[1] * 100, 2)

            # Result
            if pred == 1:
                st.success(f"✅ Eco-Friendly ({score}%)")
            else:
                st.error(f"❌ Harmful ({100 - score}%)")

        except Exception as e:
            st.error(f"❌ Prediction error: {e}")
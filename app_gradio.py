import joblib
import pubchempy as pcp
import gradio as gr

# Load model
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

# Prediction function
def predict(input_text):
    smiles = name_to_smiles(input_text)

    if smiles is None:
        smiles = input_text

    X = vectorizer.transform([smiles])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0]

    score = round(prob[1] * 100, 2)

    if pred == 1:
        return f"✅ Eco-Friendly ({score}%)\nSMILES: {smiles}"
    else:
        return f"❌ Harmful ({100-score}%)\nSMILES: {smiles}"

# UI
app = gr.Interface(
    fn=predict,
    inputs="text",
    outputs="text",
    title="🌱 Green Chemistry AI",
    description="Enter Chemical Name or SMILES"
)

app.launch()
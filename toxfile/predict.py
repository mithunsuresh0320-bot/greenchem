import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Take input
smiles = input("Enter SMILES: ")

# Convert input to features
X = vectorizer.transform([smiles])

# Predict
prediction = model.predict(X)[0]

# Output result
if prediction == 1:
    print("✅ Eco-Friendly")
else:
    print("❌ Harmful")
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
data = pd.read_csv("cleaned_data.csv")

# Convert SMILES to text features
vectorizer = CountVectorizer(analyzer='char')
X = vectorizer.fit_transform(data["smiles"])

y = data["green_score"]

print("✅ Features created:", X.shape)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

print("✅ Model trained!")

# Save model + vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model saved!")
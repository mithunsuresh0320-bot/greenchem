# 🌱 Green Chemistry AI

A machine learning application that predicts whether chemical compounds are eco-friendly based on their toxicity profiles.

## Features

- **Chemical Name Input**: Enter a chemical name and automatically convert to SMILES notation
- **SMILES Support**: Direct SMILES string input for advanced users
- **Eco-Friendly Prediction**: Get predictions with confidence scores
- **Molecular Visualization**: Display 2D structure images from PubChem

## Project Structure

```
greenchem/
├── app.py                 # Main Streamlit application
├── train_model.py         # Model training script
├── prepare_data.py        # Data preprocessing script
├── predict.py             # Prediction utilities
├── requirements.txt       # Python dependencies
├── cleaned_data.csv       # Processed training data
├── model.pkl              # Trained ML model
├── vectorizer.pkl         # Text vectorizer for SMILES
└── toxfile/
    ├── dataset.py         # Dataset utilities
    └── tox21.csv          # Raw toxicity dataset
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/greenchem.git
cd greenchem
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## Model Details

- **Algorithm**: Random Forest Classifier
- **Features**: Character-level SMILES vectorization
- **Training Data**: Tox21 toxicity dataset
- **Output**: Binary classification (Eco-friendly / Not eco-friendly)

## Dependencies

- **streamlit**: Web app framework
- **pandas**: Data manipulation
- **scikit-learn**: Machine learning
- **joblib**: Model serialization
- **pubchempy**: Chemical data retrieval

## License

MIT License

## Author

Created for Green Chemistry AI project

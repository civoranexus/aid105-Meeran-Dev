from pathlib import Path
import pickle
from ai.feature_extractor import extract_features

BASE_DIR = Path(__file__).resolve().parent.parent
AI_DIR = BASE_DIR / "ai"

with open(AI_DIR / "eligibility_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_eligibility(user, scheme):
    features = extract_features(user, scheme)
    
    X = [list(features.values())]

    probability = model.predict_proba(X)[0][1]
    
    if probability >= 0.65:
        category = "Highly Eligible"
    elif probability >= 0.35:
        category = "Potentially Eligible"
    else:
        category = "Not Eligible"
    
    return round(probability, 2), category, features
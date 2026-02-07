import pickle
from sklearn.linear_model import LogisticRegression
from data_generator import generate_training_data
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
AI_DIR = BASE_DIR / "ai"

with open(DATA_DIR / "sample_users.json", "r") as f:
    users = json.load(f)

with open(DATA_DIR / "schemes.json", "r") as f:
    schemes = json.load(f)

x, y = generate_training_data(users, schemes)

model = LogisticRegression()
model.fit(x, y)

with open(AI_DIR / "eligibility_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved.")

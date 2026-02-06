from flask import Blueprint, request, jsonify
from ai.predict import predict_eligibility
import json
from pathlib import Path

recommend_bp = Blueprint("recommend", __name__)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

@recommend_bp.route("/recommend", methods=["POST"])
def recommend_schemes():
    user = request.json

    with open(DATA_DIR / "schemes.json", "r") as f:
        schemes = json.load(f)
        
    results = []

    for scheme in schemes:
        prob, category, reasons = predict_eligibility(user, scheme)

        results.append({
            "scheme_id": scheme["scheme_id"],
            "name": scheme["name"],
            "category": category,
            "eligibility_score": round(prob * 100, 2),
            "reasons": reasons,
            "benefits": scheme["benefits"],
            "deadline": scheme["deadline"]
        })

    # Rank by eligibility score
    results.sort(key=lambda x: x["eligibility_score"], reverse=True)

    return jsonify(results)

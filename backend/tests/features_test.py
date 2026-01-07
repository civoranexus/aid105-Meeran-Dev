from ai.feature_extractor import extract_features

user = {
    "age": 18,
    "income": 100000,
    "state": "Maharashtra",
    "categories": ["Student", "OBC", "Women"]
}

scheme = {
    "min_income": 0,
    "max_income": 200000,
    "min_age": 18,
    "max_age": 30,
    "state": "Maharashtra",
    "target_groups": ["Student", "OBC"],
    "level": "State"
}

print(extract_features(user, scheme))

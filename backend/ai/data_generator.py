from feature_extractor import extract_features

def generate_label(features):
    score = (
        features["income_in_range"] * 0.35 +
        features["age_in_range"] * 0.25 +
        features["state_match"] * 0.20 +
        features["target_group_overlap"] * 0.20
    )

    return 1 if score >= 0.65 else 0


def generate_training_data(users, schemes):
    x = []
    y = []

    for user in users.values():
        for scheme in schemes.values():
            features = extract_features(user, scheme)
            x.append(list(features.values()))
            y.append(generate_label(features))

    return x, y

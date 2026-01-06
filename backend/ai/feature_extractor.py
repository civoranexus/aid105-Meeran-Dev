def extract_features(user, scheme):
    features = {}

    # Income
    features["income_in_range"] = int(
        scheme["min_income"] <= user["income"] <= scheme["max_income"]
    )

    income_range = scheme["max_income"] - scheme["min_income"]
    if income_range > 0:
        features["income_distance"] = round(
            1 - abs(user["income"] - scheme["max_income"]) / income_range, 2
        )
    else:
        features["income_distance"] = 0

    # Age
    features["age_in_range"] = int(
        scheme["min_age"] <= user["age"] <= scheme["max_age"]
    )

    # State
    features["state_match"] = int(
        scheme["state"] == "All" or scheme["state"] == user["state"]
    )

    # Target group overlap
    overlap = set(user["categories"]).intersection(set(scheme["target_groups"]))
    features["target_group_overlap"] = round(
        len(overlap) / len(scheme["target_groups"]), 2
    )

    return features

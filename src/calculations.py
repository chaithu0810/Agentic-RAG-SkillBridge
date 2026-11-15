from datetime import datetime


REFERENCE_DATE = datetime(2025, 1, 15)


def calculate_attendance(
    present_days: int,
    total_days: int
):

    if total_days <= 0:
        raise ValueError("Total days must be positive")

    if present_days < 0 or present_days > total_days:
        raise ValueError("Invalid attendance values")

    percentage = (
        present_days / total_days
    ) * 100

    return round(percentage, 2)


def calculate_weighted_score(
    scores: list,
    weights: list
):

    if len(scores) != len(weights):
        raise ValueError("Scores and weights must match")

    if not weights or any(w < 0 for w in weights):
        raise ValueError("Invalid weights")

    if sum(weights) <= 0:
        raise ValueError("Total weight must be positive")

    score = sum(
        s * w
        for s, w in zip(scores, weights)
    )

    return round(score / sum(weights), 2)


def calculate_days_remaining(target_date: str):

    target = datetime.strptime(
        target_date,
        "%Y-%m-%d"
    )

    return (target - REFERENCE_DATE).days
from src.calculations import (
    calculate_attendance,
    calculate_weighted_score,
    calculate_days_remaining
)


print("Attendance:")

print(calculate_attendance(80, 100))


print("\nWeighted Score:")

print(
    calculate_weighted_score(
        [80, 90, 70],
        [0.3, 0.4, 0.3]
    )
)


print("\nDays Remaining:")

print(
    calculate_days_remaining("2025-01-30")
)
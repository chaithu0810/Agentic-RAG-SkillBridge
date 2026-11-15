
from src.data_tools import (
    search_student,
    search_course,
    search_assessment,
    search_attendance,
    search_mentor
)

from src.policy_search import search_policy

from src.calculations import (
    calculate_attendance,
    calculate_weighted_score
)

from src.agent import run_agent


print("\n========== CSV TESTING ==========")

print("Student:", search_student("S101"))

print("Course:", search_course("C101"))

print("Assessment:", search_assessment("S101"))

print("Attendance:", search_attendance("S101"))

print("Mentor:", search_mentor("M101"))


print("\n========== POLICY TESTING ==========")

print(
    search_policy(
        "What are the attendance requirements?"
    )
)


print("\n========== CALCULATION TESTING ==========")

print(calculate_attendance(80, 100))

print(
    calculate_weighted_score(
        [80, 90, 70],
        [0.3, 0.4, 0.3]
    )
)


print("\n========== AGENT TESTING ==========")

result = run_agent(
    "Explain the attendance policy."
)

print(result["answer"])

print(result["tool_trace"])

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
    calculate_weighted_score,
    calculate_days_remaining
)


TOOLS = [

    search_student,

    search_course,

    search_assessment,

    search_attendance,

    search_mentor,

    search_policy,

    calculate_attendance,

    calculate_weighted_score,

    calculate_days_remaining

]


TOOL_FUNCTIONS = {

    "search_student": search_student,

    "search_course": search_course,

    "search_assessment": search_assessment,

    "search_attendance": search_attendance,

    "search_mentor": search_mentor,

    "search_policy": search_policy,

    "calculate_attendance": calculate_attendance,

    "calculate_weighted_score": calculate_weighted_score,

    "calculate_days_remaining": calculate_days_remaining

}
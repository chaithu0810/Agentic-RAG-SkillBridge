from src.data_tools import (
    search_student,
    search_course,
    search_assessment,
    search_attendance,
    search_mentor
)

print("\nSTUDENT LOOKUP")
print(search_student("STU0001"))

print("\nCOURSE LOOKUP")
print(search_course("CRS013"))

print("\nASSESSMENT LOOKUP")
print(search_assessment("STU0001"))

print("\nATTENDANCE LOOKUP")
print(search_attendance("STU0001"))

print("\nMENTOR LOOKUP")
print(search_mentor("MNT004"))
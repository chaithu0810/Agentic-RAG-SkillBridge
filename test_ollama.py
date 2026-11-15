from ollama import chat

def get_attendance(student_id: str):
    return f"Attendance records for {student_id}"

response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": "Find attendance for student S101"
        }
    ],
    tools=[
        get_attendance
    ]
)

print(response.message)
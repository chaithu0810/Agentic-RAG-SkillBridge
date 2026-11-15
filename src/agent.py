
import json
import ollama

from src.schemas import TOOLS, TOOL_FUNCTIONS

MODEL = "qwen2.5:7b"

SYSTEM_PROMPT = """
You are SkillBridge Student Academics Agent.

You answer questions about:
- Students
- Courses
- Assessments
- Attendance
- Mentors
- Academic policies

Rules:
1. Use tools to retrieve actual information.
2. Use search_policy for policy questions.
3. Use Python functions for calculations.
4. Never invent records or policies.
5. If information is unavailable, say so.
6. Use 15 January 2025 as the reference date.
"""


def run_agent(question):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    tool_trace = []

    try:

        for iteration in range(8):

            response = ollama.chat(
                model=MODEL,
                messages=messages,
                tools=TOOLS,
                stream=False
            )

            assistant_message = response.message

            messages.append(assistant_message)

            tool_calls = assistant_message.tool_calls or []

            # Return final answer when no more tools are needed

            if not tool_calls:

                return {
                    "answer": assistant_message.content or
                              "No answer generated.",
                    "tool_trace": tool_trace
                }

            for tool_call in tool_calls:

                tool_name = tool_call.function.name

                arguments = tool_call.function.arguments

                # Normalize arguments if SDK returns JSON text

                if isinstance(arguments, str):
                    arguments = json.loads(arguments)

                print("\nTOOL:", tool_name)
                print("ARGUMENTS:", arguments)

                function = TOOL_FUNCTIONS.get(tool_name)

                if function is None:
                    result = {
                        "error": f"Unknown tool: {tool_name}"
                    }
                else:
                    try:
                        result = function(**arguments)
                    except Exception as error:
                        result = {"error": str(error)}

                tool_trace.append({
                    "tool": tool_name,
                    "arguments": arguments,
                    "result": result
                })

                messages.append({
                    "role": "tool",
                    "name": tool_name,
                    "content": json.dumps(
                        result,
                        default=str
                    )
                })

        return {
            "answer": "Maximum agent iterations reached.",
            "tool_trace": tool_trace
        }

    except Exception as error:

        print("AGENT ERROR:", error)

        return {
            "answer": f"Agent failed: {error}",
            "tool_trace": tool_trace
        }

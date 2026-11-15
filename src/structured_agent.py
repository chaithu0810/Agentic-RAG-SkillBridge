
import json
import ollama

from src.agent import run_agent
from src.output_schema import AgentOutput


MODEL = "qwen2.5:7b"


def get_structured_answer(question):

    # Run the main Agentic RAG system
    result = run_agent(question)

    answer_text = result["answer"]

    # Convert agent response into structured output
    prompt = f"""
    Convert the following academic answer into JSON.

    Question:
    {question}

    Agent answer:
    {answer_text}

    Return these four fields:

    {{
        "answerable": 1,
        "lookup_value": null,
        "rule_value": null,
        "final_answer": null
    }}

    Rules:
    - answerable must be 0 or 1.
    - Never invent information.
    - Use null for unavailable values.
    - Return valid JSON only.
    """

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format=AgentOutput.model_json_schema()
    )

    raw_output = response.message.content

    try:

        data = json.loads(raw_output)

        validated = AgentOutput.model_validate(data)

        return validated.model_dump()

    except Exception as error:

        raise ValueError(
            f"Could not generate structured output: {error}"
        )

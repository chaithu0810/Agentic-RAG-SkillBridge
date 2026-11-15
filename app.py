
import streamlit as st

from src.agent import run_agent


st.set_page_config(
    page_title="SkillBridge Academics Agent",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 SkillBridge Student Academics Agent")

st.write(
    "Your AI-powered academic assistant. "
    "Ask questions about students, courses, "
    "attendance, assessments and academic policies."
)


if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat history

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Receive question

question = st.chat_input(
    "Ask your academic question..."
)


if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)


    with st.chat_message("assistant"):

        with st.spinner("AI Agent is working..."):

            result = run_agent(question)

            # Handle both dictionary and string responses

            if isinstance(result, dict):

                answer = result.get(
                    "answer",
                    "No answer generated."
                )

                tool_trace = result.get(
                    "tool_trace",
                    []
                )

            else:

                answer = str(result)

                tool_trace = []

            st.markdown(answer)

            if tool_trace:

                with st.expander(
                    "View Agent Tool Execution"
                ):

                    for trace in tool_trace:

                        st.write(
                            "Tool:",
                            trace.get("tool")
                        )

                        st.json(trace)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })


import streamlit as st
import asyncio

from agent import callAgent

# Page Configuration
st.set_page_config(
    page_title="Movie Automation System",
    page_icon="🎬",
    layout="centered"
)

# Application Title
st.title("🎬 Movie Automation System")

st.write("Ask me anything about Movies, Multiplex and Hall details.")

# Store Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# User Chat Input
user_input = st.chat_input("Ask about movies...")

if user_input:

    # Display User Message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Get AI Response
    with st.chat_message("assistant"):

        with st.spinner("Agent is searching movie details..."):

            try:

                result = asyncio.run(callAgent(user_input))

                st.write(result)

                # Save Assistant Response
                st.session_state.messages.append(
                    {"role": "assistant", "content": result}
                )

            except Exception as e:

                st.error(f"Error: {e}")

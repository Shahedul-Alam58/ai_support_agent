import streamlit as st
from controller import route_request

st.set_page_config(page_title="SRBN Store AI Support Agent")
st.title("🛒 SRBN Store AI Support Agent")

# Initialize chat history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Type your message here:")

if st.button("Send") and user_input.strip():
    # Send input to controller
    response = route_request(user_input)

    # Save to chat history
    st.session_state.history.append({"user": user_input, "bot": response})

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")
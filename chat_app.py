import streamlit as st
import requests

st.set_page_config(page_title="Bangla RAG Chatbot", layout="centered")
st.title("🗣️ Bangla Literature Chatbot")
st.write("Ask questions in Bangla or English based on your uploaded textbook.")

# Set up session history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("❓ Ask a question:")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    # Call FastAPI endpoint
    try:
        response = requests.post("http://localhost:8000/ask", json={"question": user_input})
        data = response.json()
        st.session_state.chat_history.append(("🧑 You", user_input))
        st.session_state.chat_history.append(("🤖 Bot", data["answer"]))
    except Exception as e:
        st.error(f"❌ Could not connect to API: {e}")

# Display chat
for speaker, message in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {message}")

# Show the similarity graph
st.divider()
st.markdown("#### 🔍 Retrieved Chunk Similarity Scores")
try:
    st.image("retrieval_scores.png", use_column_width=True)
except:
    st.warning("No similarity graph found yet.")

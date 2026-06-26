import streamlit as st
from ollama import Client

# Create client instance (Very Important)
client = Client(host="http://localhost:11434")

st.set_page_config(
    page_title="Custom LLM Model By Omraje Ambure - Ollama",
    layout="centered",
    page_icon="💀"
)

st.title("Custom Local LLM Model");

prompt = st.text_area("Enter Your Prompt",height=200,max_chars=2000,placeholder="Enter Your Prompt",label_visibility="hidden")


if st.button("Generate Response",icon='🔥'):
    if prompt.strip() == "qwen2.5-coder:7b":
        st.warning("Please Enter A Prompt")
    else:
        with st.spinner("Thinking..."):
            response = client.chat(
                model="qwen2.5-coder:7b",
                messages=[
                    {"role":"user","content":prompt}
                ]
            )
            st.success("Response Generated! ")
            st.write(response["message"]["content"])
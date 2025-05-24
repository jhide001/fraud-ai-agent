
import streamlit as st
import os
import openai

st.set_page_config(page_title="Fraud Detection AI Agent")

st.title("🔍 Fraud Detection AI Agent")
st.markdown("Enter a **link or message** and I’ll scan it for potential fraud.")

openai.api_key = os.getenv("OPENAI_API_KEY")

user_input = st.text_area("Paste the suspicious text or link here:")

if st.button("Scan for Fraud"):
    if not openai.api_key:
        st.warning("Missing OpenAI API key. Please set it in your environment.")
    elif user_input.strip() == "":
        st.error("Please enter some text or a link to scan.")
    else:
        with st.spinner("Analyzing..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a cybersecurity agent trained to detect fraud, phishing, and scams."},
                    {"role": "user", "content": f"Check this for fraud: {user_input}"}
                ],
                temperature=0.2
            )
            result = response['choices'][0]['message']['content']
            st.success("Scan Complete:")
            st.write(result)

import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. SETUP - PASTE YOUR KEY CAREFULLY HERE
genai.configure(api_key="API key")
model = genai.GenerativeModel('gemini-2.5-flash')

st.title("SnapFix Debugger")

uploaded_file = st.file_uploader("Upload Code Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, use_container_width=True)
    
    if st.button("Analyze & Fix"):
        st.write("🔄 Connecting to Google AI...") # This tells you the button worked
        try:
            response = model.generate_content(["Identify the error in this code and provide a fix:", img])
            st.subheader("The Solution:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
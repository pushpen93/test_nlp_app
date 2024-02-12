import streamlit as st

def main():
    st.title("Resume Information Extractor")
    
    uploaded_file = st.file_uploader("Upload a resume", type=["pdf", "docx"])
    if uploaded_file:
        st.write("File uploaded successfully!")
        # Process the uploaded file and extract information
        
        # Display extracted information
        st.write("Extracted Information:")
        # Display extracted information here

if __name__ == "__main__":
    main()


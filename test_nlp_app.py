import streamlit as st

def main():
    # Set up the layout
    st.title("Resume Information Extractor")

    # Upload resume in the sidebar
    uploaded_file = st.sidebar.file_uploader("Upload a resume", type=["pdf", "docx"])
    
    if uploaded_file:
        # Display uploaded resume over the entire screen
        st.title("Uploaded Resume")
        st.write("File uploaded successfully!")
        # Display extracted information
        st.title("Extracted Information:")
        # Process the uploaded file and extract information
        # Display extracted information here

if __name__ == "__main__":
    main()

import streamlit as st

def main():
    # Set up the layout
    st.title("Resume Information Extractor")
    col1, col2 = st.columns([1, 3])  # Adjust the width ratio as needed
    
    # Left column for title
    with col1:
        pass  # Nothing to display here, just keeping the space
    
    # Right column for file upload and review
    with col2:
        uploaded_file = st.file_uploader("Upload a resume", type=["pdf", "docx"])
        if uploaded_file:
            st.write("File uploaded successfully!")
            # Process the uploaded file and extract information
            
            # Display extracted information
            st.write("Extracted Information:")
            # Display extracted information here

if __name__ == "__main__":
    main()


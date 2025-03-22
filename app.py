import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with PDFs", page_icon=":books:")
    
    st.header("Chat with PDFs :books:")
    st.text_input("Ask me anything about your documents:")
    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docx = st.file_uploader("Upload your PDFs and click on 'Process'",accept_multiple_files=True)
        if st.button("Process"): # This button will trigger the processing of the uploaded files if clicked
            with st.spinner("Processing..."): # This will display a loading message while the files are being processed
                # get the text from the uploaded files
        
if __name__ == "__main__":
    main()
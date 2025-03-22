import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def get_text_from_pdf(pdf_file):
    text = "" # This will store the text from the PDFs
    for pdf in pdf_file: # Loop through the uploaded PDFs
        pdf_reader = PdfReader(pdf) # Read the current PDF
        for page in pdf_reader.pages: # Loop through the pages of the current PDF
            text += page.extract_text() # Extract the text from the current page and add it to the text variable
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(separator='\n',chunk_size=1000,chunk_overlap=200,length_function=len) # Create a text splitter object , length_function=len is used to get the length of the text
    text_chunks = text_splitter.split(text) # Split the text into chunks
    return text_chunks

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
                raw_text = get_text_from_pdf(pdf_docx)
                
                # split the text into chunks
                text_chunks = get_text_chunks(raw_text)
        
if __name__ == "__main__":
    main()
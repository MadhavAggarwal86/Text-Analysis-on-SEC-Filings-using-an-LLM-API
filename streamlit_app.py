import streamlit as st 
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.chains.summarize import load_summarize_chain
from transformers import T5Tokenizer, T5ForConditionalGeneration
from langchain_text_splitters import RecursiveCharacterTextSplitter
from transformers import pipeline
import aspose.words as aw
import nlp
import torch
import base64
import requests
from sec_edgar_downloader import Downloader
import os
from bs4 import BeautifulSoup
import re






#from ticker to downloading data
headers = {"User-Agent": "madhavaggarwal86@gmail.com"}

def data_finding (ticker2):
    dl = Downloader("user-agent", "madhavaggarwal86@gmail.com")
    dl.get("10-K", ticker2)
    
    placeholder = st.empty()
    for i in range(5, 0, -1):
        placeholder.text(f"Running in {i} seconds...")
        time.sleep(1)
    run_after_5_seconds()
    

def ticker_finding (ticker, headers = headers):
    ticker = ticker.upper().replace(".", "-")
    ticker_json = requests.get("https://www.sec.gov/files/company_tickers.json", headers = headers).json()
    
    return data_finding(ticker)
    raise ValueError(f"Ticker {Ticker} not found in SEC Database")



#to clean data for preprocessing
def clean_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Remove content after "&lt;div style="font-family:Tim"
    clean_text = re.sub(r'&lt;div style="', '', html_content, flags=re.DOTALL)

    # Remove HTML tags
    clean_text = re.sub(r'<.*?>', '', clean_text)

    # Remove extra newlines and whitespace
    clean_text = "\n".join(line.strip() for line in clean_text.splitlines() if line.strip())

    # Write clean text to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(clean_text)


input_folder = "sec-edgar-filings"
output_folder = "Output"

def run_after_5_seconds(): 
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".txt"):
                input_file = os.path.join(root, file)
                output_subfolder = os.path.relpath(root, input_folder)
                output_subfolder_path = os.path.join(output_folder, output_subfolder)
                if not os.path.exists(output_subfolder_path):
                    os.makedirs(output_subfolder_path)
                output_file = os.path.join(output_subfolder_path, f"cleaned_{file[:-4]}.txt")

                with open(input_file, 'r', encoding='utf-8') as f:
                    text_content = f.read()
                
                # Check if the file contains HTML or XBRL data
                if "<html" in text_content.lower():
                    clean_html(input_file, output_file)
                else:
                    # Clean XBRL data by removing XML-like tags and extra newlines/whitespace
                    clean_text = re.sub(r'<.*?>', '', text_content)
                    clean_text = "\n".join(line.strip() for line in clean_text.splitlines() if line.strip())
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(clean_text)
                    
    placeholder2 = st.empty()
    for i in range(5, 0, -1):
        placeholder2.text(f"Running in {i} seconds...")
        time.sleep(1)
    
    st.subheader("Your Summarization as below: ")
    merge_txt_files("Output", "output.txt")
    txt_to_pdf("output.txt", "output.pdf")
    summary = llm_pipeline(directory_path)
    st.text("Summarization Complete")
    st.text(summary)
    





#model and tokenizer loading
checkpoint = "LaMini-Flan-T5-248M"
tokenizer = T5Tokenizer.from_pretrained(checkpoint)
base_model = T5ForConditionalGeneration.from_pretrained(checkpoint, device_map='auto', torch_dtype=torch.float32)







#file loader and preprocessing
def file_preprocessing(file):
    loader =  PyPDFLoader(file)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    texts = text_splitter.split_documents(pages)
    final_texts = ""
    for text in texts:
        print(text)
        final_texts = final_texts + text.page_content
    return final_texts



# merge txt files into one 
def merge_txt_files(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write('\n')

# Example usage:




# convert .txt file to pdf file
def txt_to_pdf(input_file, output_file):
    doc = aw.Document(input_file)
    doc.save(output_file)













directory_path = "/Users/madhavaggarwal/Desktop/FINAL BLOW/output.pdf"









#LLM pipeline
def llm_pipeline(filepath):
    pipe_sum = pipeline(
        'summarization',
        model = base_model,
        tokenizer = tokenizer,
        max_length = 500, 
        min_length = 50)
    input_text = file_preprocessing(filepath)
    result = pipe_sum(input_text)
    result = result[0]['summary_text']
    return result
@st.cache_data(experimental_allow_widgets=True)


#streamlit code 

def main():
    st.title("Document Summarization App using Language Model")

    user_input = st.text_input("Enter something:")
    ticker_finding (user_input, headers = headers)
    




    
    
    

if __name__ == "__main__":
    main()
    
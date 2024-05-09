# 📄 Text Analysis on SEC Filings using an LLM API

## 📝 Overview

This project aims to perform text analysis on SEC 10-K filings using an LLM (Language Model) API. The process involves fetching SEC filings using the EDGAR API, cleaning the data using BeautifulSoup, and then utilizing the LLM API to extract insights from the filings.

## 🛠️ Tech Stack

- **Python Libraries**:
  - SEC_EDGAR_downloader
  - Aspose
  - BeautifulSoup
- **LANGCHAIN**
- **STREAMLIT**
- **LLM API** - LaMini-Flam-T5-248M

## 📁 Main Code

The main code is implemented in the file `streamlit_app.py`.

## 🔄 Workflow

1. **📊 Data Collection**: 
   - Use the EDGAR API to fetch SEC 10-K filings by entering the Company Ticker in the input area.

2. **🧹 Data Cleaning**:
   - Clean the fetched data, which is in HTML or XBRL format, present in .txt files using BeautifulSoup.

3. **🔨 Data Processing**:
   - Merge all .txt files into one file, which is then converted into a PDF file. Using PDF files simplifies the process and can lead to better summarization results.

4. **🔍 Text Analysis**:
   - Utilize the LaMini LLM API to extract insights from the consolidated dataset. I have chosen this specific LLM API because it is mini-version of Llama API and I thought it could possibly run on my local host on my laptop. 

## ⚠️ Limitations

Due to limitations related to the macOS system, the web app cannot be run locally to display outputs. However, the code is error-free.

## 🚀 How to Run

To run the code, follow these steps:

1. **Download the LLM API**:
   - First of all, download the LLM API from this link (https://drive.google.com/drive/folders/1IcIh94_nsooWbl5RHGZapWBVHf1KJWEn?usp=drive_link) and put it in the same folder where you are going to run the code.

2. **Install Required Libraries**:
   - All the required Python libraries are listed in the `requirements.txt` file. Run the following command in the terminal or Command Prompt:
     ```
     pip install -r requirements.txt
     ```

3. **Run the Streamlit App**:
   - Go to the main code, which is `streamlit_app.py`, and run the following command in the terminal:
     ```
     streamlit run streamlit_app.py
     ```
   Your program will run on your localhost.

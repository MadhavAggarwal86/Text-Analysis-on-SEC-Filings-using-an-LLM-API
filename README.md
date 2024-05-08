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
   - Utilize the LaMini LLM API to extract insights from the consolidated dataset.

## ⚠️ Limitations

Due to limitations related to the macOS system, the web app cannot be run locally to display outputs. However, the code is error-free.

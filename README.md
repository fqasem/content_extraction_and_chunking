# content_extraction_and_chunking
This exercise shows content extraction and chunking from various types of files - pdf, image etc.

# 1. Pdf content extraction:

The provided code demonstrates a powerful Python script for efficiently extracting and processing content from PDF documents. It employs various libraries such as pdfplumber, fitz, and reportlab to extract text, identify specific font sizes, segment content into meaningful chunks, and generate new PDFs based on those chunks. This code can be incredibly useful for tasks like analyzing PDF reports, extracting specific sections, and reorganizing content for further analysis or presentation.

Source: https://medium.com/@mahedi154/automated-pdf-content-extraction-and-chunking-with-python-d8f8012defda

Note: Use pymupdf instead of fitz module

From terminal:

 C:\Users\farra\Projects\git_projects\content_extraction_and_chunking\.venv\Scripts> .\python.exe -m pip install -r ..\..\requirements.txt

 OR (The following resulted in ModuleNotFound error. Better use the above one)

pip install pymupdf pdfplumber reportlab pytesseract pillow

# 2. Text extraction from image:

## Using Tesseract

Source : https://www.nutrient.io/blog/how-to-use-tesseract-ocr-in-python/

Optical character recognition (OCR) is essential for converting images of text into machine-encoded text, and Python provides powerful tools to streamline this process. In this tutorial, you’ll learn how to use Python with Tesseract OCR, a powerful open source OCR engine, using the pytesseract library. This guide walks you through installing Tesseract, setting up Python bindings, and running image-to-text extraction effectively. 


### How to resolve Tesseract Not Found isuue:

For Windows Only
1 - You need to have Tesseract OCR installed on your computer.

get it from here. https://github.com/UB-Mannheim/tesseract/wiki

Download the suitable version.

2 - Add Tesseract path to your System Environment. i.e. Edit system variables.

3 - Run pip install pytesseract and pip install tesseract

4 - Add this line to your python script every time

pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'  # your path may be different
5 - Run the code.

## Using EasyOCR

EasyOCR is a popular open-source optical character recognition (OCR) library designed to extract text from images and convert it into machine-readable formats. With its user-friendly interface and straightforward integration, EasyOCR makes it simple for developers to implement OCR capabilities into their applications. The library supports multiple languages, making it versatile for a wide range of international use cases. By leveraging advanced deep learning techniques, EasyOCR achieves high accuracy in text extraction, enabling efficient data extraction and analysis from various sources, such as scanned documents, photographs, and screenshots.

### Description:

The EasyOCR Text Extraction project is an application that utilizes the EasyOCR library to extract text from images in both English and Hindi languages. The project aims to provide a simple and efficient solution for developers who require OCR capabilities in their applications for extracting textual information from images.

### Features:

Text extraction from images: The application uses the EasyOCR library to extract text from images containing English and Hindi characters. Language support: Supports both English and Hindi languages for text extraction. High accuracy: The EasyOCR library utilizes advanced deep learning techniques to achieve high accuracy in text extraction, ensuring reliable results. Easy integration: The project provides a user-friendly interface and straightforward integration, making it easy for developers to incorporate OCR capabilities into their applications. Versatile usage: The application can extract text from various sources, including scanned documents, photographs, and screenshots.

### Installation:

Clone the repository: git clone https://github.com/Priyansu-Bhandari/EasyOCR_Project.git

Install the required dependencies: pip install -r requirements.txt

Usage: Upload Image: Select an image file (in JPG, PNG, or TIFF format) containing English or Hindi text that you want to extract.

Extract Text: Click the "Extract Text" button to initiate the text extraction process.

View Results: The extracted text will be displayed on the screen, separated by language.

### Dependencies:

Python (3.6+)

EasyOCR library

OpenCV (for image processing)

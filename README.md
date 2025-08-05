# content_extraction_and_chunking
This exercise shows content extraction and chunking from various types of files - pdf, image etc.

1. Pdf content extraction:

The provided code demonstrates a powerful Python script for efficiently extracting and processing content from PDF documents. It employs various libraries such as pdfplumber, fitz, and reportlab to extract text, identify specific font sizes, segment content into meaningful chunks, and generate new PDFs based on those chunks. This code can be incredibly useful for tasks like analyzing PDF reports, extracting specific sections, and reorganizing content for further analysis or presentation.

Source: https://medium.com/@mahedi154/automated-pdf-content-extraction-and-chunking-with-python-d8f8012defda

Note: Use pymupdf instead of fitz module

From terminal:

 C:\Users\farra\Projects\git_projects\content_extraction_and_chunking\.venv\Scripts> .\python.exe -m pip install -r ..\..\requirements.txt

 OR (The following resulted in ModuleNotFound error. Better use the above one)

pip install pymupdf pdfplumber reportlab pytesseract pillow

2. Image extraction:

Source : https://www.nutrient.io/blog/how-to-use-tesseract-ocr-in-python/


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

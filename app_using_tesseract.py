import streamlit as st
import pytesseract
from PIL import Image
import io

# Set the path to the Tesseract-OCR executable
# Download Tesseract-OCR from https://digi.bib.uni-mannheim.de/tesseract/
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust this path as necessary

def extract_text_from_image(image):
    """
    Extracts text from a PIL image using Tesseract OCR.
    :param image: PIL Image object.
    :return: Extracted text as a string.
    """
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return str(e)

st.title("Handwriting/Image to Editable Text")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.write("Extracting text...")
    extracted_text = extract_text_from_image(image)
    st.subheader("Extracted Text:")
    st.text_area("Text", extracted_text, height=200)
    st.download_button(
        label="Download Text",
        data=extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
else:
    st.info("Please upload an image file to extract text.")
# Note: Ensure that Tesseract-OCR is installed and the path to the executable is correctly set.

# 🖼️ Image to Text Converter App

Convert images (even handwritten ones!) into editable text using **Python**, **Streamlit**, and **Tesseract OCR**.  
Run the app locally and access it on any device (mobile or desktop) on the same network — no deployment required!

---

## 📌 Features

✅ Upload image files (`.jpg`, `.jpeg`, `.png`)  
✅ Extract text using `pytesseract` (OCR engine)  
✅ View and edit extracted text  
✅ Download as `.txt` file  
✅ Access app on your mobile via local IP  
✅ Built with **just a few lines of Python code**

---

## 🚀 Screenshot

![image](https://github.com/user-attachments/assets/8a32d1ed-cfa1-4f81-9266-731d42ebec30)


> Access the app in your mobile browser by visiting your computer's IP and port (e.g., `http://192.168.0.105:8501`)

---

## 📦 Installation

1. **Clone this repository:**

```bash
git clone https://github.com/Manav1918/image2text-streamlit.git
cd image-to-text-converter
```

2. **Install dependencies:**

```bash
pip install streamlit pytesseract pillow
```

3. **Install Tesseract OCR Engine:**

- Download from [Official Website](https://digi.bib.uni-mannheim.de/tesseract/)
- After installing, update the path in the script:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
```

---

## ▶️ Run the App

```bash
streamlit run app_using_tesseract.py
```

You can now open it in your browser (usually `http://localhost:8501`)  
To access it on your mobile device, find your computer's IP and use:

```
http://<your-local-ip>:8501
```

---

## 📁 File Structure

```
📦 image-to-text-converter
├── app_using_tesseract.py
├── requirements.txt
├── README.md
```

---

## ✨ Upcoming Feature

If you're interested in a **handwriting-to-text converter like Google Lens**, using the **Google Vision API**, leave a comment or ⭐ the repo — tutorial coming soon!

---

## 🙏 Support & Contribution

Feel free to fork, star ⭐, and contribute via pull requests!

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📢 Connect

Subscribe to [**CID – An Education Hub**](https://youtube.com/@CID_Official)  
Slogan: _Keep Coding! Keep Learning!_

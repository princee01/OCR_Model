# 🧠 Handwritten Answer OCR with Smart Evaluation

## 📖 Overview

This project is an Optical Character Recognition (OCR) tool that extracts handwritten English text from images using EasyOCR and OpenCV. The extracted text is formatted to preserve numbered answers and paragraphs, making it suitable for academic evaluations.

It is currently being enhanced to integrate OpenAI’s ChatGPT for automated answer correctness checking and will include support for file uploads and answer history storage using a database.

---

## 🚀 Features

- ✅ **Handwritten Text Extraction**: Uses EasyOCR to recognize handwritten text from answer sheets or paper.
- ✅ **Smart Formatting**: Automatically formats numbered points for cleaner output.
- ⚙️ **Work in Progress**:
  - Paragraph handling improvements.
  - ChatGPT integration to validate answer correctness.
  - File upload support (PDF/Image).
  - Answer storage in a database for record-keeping.
- 🔮 **Future Scope**:
  - Evaluate answers using OpenAI API (ChatGPT).
  - Provide API-based access for frontend apps.
  - Improved UI for uploading and viewing results.
  - Support extracting answers from PDFs, images, or scanned sheets.
  - Historical data view & analytics for users/students.

---

## 🧰 Requirements

Make sure Python 3.x is installed, then install required libraries:

```bash
pip install easyocr opencv-python

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

🧪 Usage Instructions
Save your handwritten answer as an image (.png, .jpg, etc.).

Replace the image_path variable with your image file name:

python
Copy
Edit
image_path = "your_image_name.png"
Run the script:

bash
Copy
Edit
python ocr_extractor.py
Output will show extracted and formatted text from the image.

🛠️ Ongoing Changes
Improve text recognition from real paper paragraphs and longer answers.

Integrate ChatGPT to validate answer correctness using OpenAI's API.

Enhance the script to accept file uploads (PDF/image) instead of hardcoded image paths.

Store previous extraction results and evaluated answers in a database.

🔮 Future Scope
✍️ Answer Evaluation Using ChatGPT: Extracted answers will be evaluated using OpenAI's API for correctness and completeness.

🖼️ Support File Uploads: Users will be able to upload files (images, PDFs) through a frontend UI.

💬 API Integration: A REST API will be developed to expose the OCR and answer evaluation as a service.

🧾 Database Integration: Store extracted answers, evaluations, and scores for future reference.

🌐 Improved UI: User-friendly frontend to upload images, view results, and track performance.

📊 Analytics & Dashboard: Show evaluation scores, strengths/weaknesses, and progress over time.

🧠 Example Output
pgsql
Copy
Edit
Formatted Extracted Text:
1. Python is an interpreted language.
It supports object-oriented and procedural programming.
2. Machine Learning is a part of Artificial Intelligence.
🤝 Contributing
Want to help? Feel free to fork this repository, make enhancements, and submit a pull request.

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

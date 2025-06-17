# 🧠 OCR with Smart Evaluation

## 📖 Overview
This project is an Optical Character Recognition (OCR) tool designed to extract questions and their respective handwritten answers from images using EasyOCR and OpenCV. After extracting the content, it leverages an AI-powered answer evaluation system via API integration to automatically check the correctness and quality of answers.

Based on the AI evaluation, the system assigns grades or scores to each answer, enabling an automated and efficient academic assessment workflow. The project also supports storing answer history and evaluation results for future reference.

## 🚀 Features
✅ Handwritten Text Extraction: Uses EasyOCR to recognize handwritten text from answer sheets or paper.

✅ Smart Formatting: Automatically formats numbered points for cleaner output.

✅ Smart Evaluation & Answer Validation: Automatically evaluates and validates answers for correctness and completeness using the integrated AI system.

✅ File Upload Support: Accepts images and PDFs for processing.

✅ Answer Storage: Stores extracted answers and evaluations in a database for record-keeping.


## 🧰 Requirements

Make sure Python 3.x is installed, then install required libraries:

```bash
pip install easyocr opencv-python
```

## 🧪 Usage Instructions

1. Place your handwritten answer image in the project folder.
2. Open the script file.
3. Update the `image_path` variable with your image file name. Example:
   ```python
   image_path = "your_image_name.png"
   ```
4. Run the script:
   ```bash
   python ocr_extractor.py
   ```
5. The script will:
   - Extract handwritten text using EasyOCR.
   - Format the text for easier reading (especially numbered points).
   - Print the formatted extracted text to the console.

## 🛠️ Ongoing Changes

1. Improve text recognition from real paper paragraphs and longer answers.
2. Enhance the script to accept file uploads (PDF/image) instead of hardcoded image paths.
3. Store previous extraction results and evaluated answers in a database.

## 🔮 Future Scope
🖼️ Support File Uploads: Users will be able to upload files (images, PDFs) through a frontend UI.

🧾 Database Integration: Store extracted answers, evaluations, and scores for future reference.

🌐 Improved UI: User-friendly frontend to upload images, view results, and track performance.

📊 Analytics & Dashboard: Show evaluation scores, strengths/weaknesses, and progress over time.



## 📥 Example Output

![Screenshot 2025-06-17 165846](https://github.com/user-attachments/assets/51f5fbf9-f497-4cf0-8ff5-b7d5415c9a57)
![Screenshot 2025-06-17 165911](https://github.com/user-attachments/assets/b01bfd5a-ff5b-4b04-9921-df871fdcf994)
![Screenshot 2025-06-17 165934](https://github.com/user-attachments/assets/358ad589-1f8f-401b-800d-bcddf2c8fd31)


## 🤝 Contributing

Want to help? Feel free to fork this repository, make enhancements, and submit a pull request.

## 📄 License

This project is licensed under the **MIT License** – see the LICENSE file for details.

## 👨‍💻 Author

**Prince**  
B.Tech CSE | Developer | AI & Software Enthusiast  
[GitHub](http://github.com/princee01) | [LinkedIn](https://www.linkedin.com/in/prince-kumar99107/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

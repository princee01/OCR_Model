
# #-----------------------------------------------------------------old code only for extracting text from image--------------------
# import easyocr
# import cv2
# import re

# def extract_handwritten_text(image_path):
#     reader = easyocr.Reader(['en'])  # Language = English
#     result = reader.readtext(image_path)

#     formatted_text = ""
#     for detection in result:
#         text = detection[1]
#         # If text starts with a number (like "1", "2", etc.)
#         if re.match(r"^\d", text):
#             formatted_text += f"\n{text}\n"
#         else:
#             formatted_text += text + " "

#     return formatted_text.strip()

# if __name__ == "__main__":
#     image_path = "Screenshot 2025-05-20 225502.png"
#     text = extract_handwritten_text(image_path)
#     print("Formatted Extracted Text:\n1.", text)
##-------------------------------------------------------------code with API integration and answer evaluation-------------------
import easyocr
import re
import requests

def extract_handwritten_text(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    raw_text = ""
    for detection in result:
        text = detection[1]
        raw_text += text + " "

    raw_text = re.sub(r'\s*(Q[:\-])', r'\n\1', raw_text)
    raw_text = re.sub(r'\s*(A[:\-])', r'\n\1', raw_text)

    return raw_text.strip()

def extract_qa_pairs(text):
    lines = text.splitlines()
    qa_pairs = []
    question, answer = "", ""

    for line in lines:
        if line.startswith("Q:") or line.startswith("Q-"):
            if question and answer:
                qa_pairs.append((question.strip(), answer.strip()))
                question, answer = "", ""
            question = line[2:].strip()
        elif line.startswith("A:") or line.startswith("A-"):
            answer = line[2:].strip()

    if question and answer:
        qa_pairs.append((question.strip(), answer.strip()))

    return qa_pairs


def evaluate_with_huggingface(question, answer):
    import requests

    HF_TOKEN = "write your huggingace API key"     #point to be noted
    API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a strict examiner. Evaluate the student's answer and respond ONLY in the format below. Do NOT answer any other questions or continue the conversation.

FORMAT:
Score: X/10  
Explanation: ...  
Suggestions: ...

Question: {question}
Answer: {answer}
"""

    payload = {
        "inputs": prompt.strip(),
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.5,
            "return_full_text": False,
            "stop": ["Question:", "Student's Answer:"]
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
                return result[0]["generated_text"].strip()
            else:
                return "⚠️ Unexpected response format: " + str(result)
        else:
            return f"⚠️ API Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"⚠️ Request failed: {e}"




if __name__ == "__main__":
    image_path = "Screenshot 2025-05-22 125223.png"  # Change as needed
    raw_text = extract_handwritten_text(image_path)

    print("\n📄 Cleaned OCR Text:\n" + "="*40)
    print(raw_text)

    qa_pairs = extract_qa_pairs(raw_text)

    if not qa_pairs:
        print("\n❌ No Q&A pairs detected. Please check OCR formatting.")
    else:
        for i, (q, a) in enumerate(qa_pairs, 1):
            print(f"\n--- 📝 Evaluating Question {i} ---")
            print(f"Q: {q}")
            print(f"A: {a}")
            feedback = evaluate_with_huggingface(q, a)
            print("✅ Feedback:\n", feedback)




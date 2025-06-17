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

    # Handle formats like '1 . Q:' or '1\t. Q:'
    raw_text = re.sub(r'\s*\d+\s*[\.\-]\s*(Q[:\-])', r'\n\1', raw_text, flags=re.IGNORECASE)
    raw_text = re.sub(r'\s*\d+\s*[\.\-]\s*(A[:\-])', r'\n\1', raw_text, flags=re.IGNORECASE)

    # Also match regular Q:/A: without leading numbers
    raw_text = re.sub(r'\s*(Q[:\-])', r'\n\1', raw_text, flags=re.IGNORECASE)
    raw_text = re.sub(r'\s*(A[:\-])', r'\n\1', raw_text, flags=re.IGNORECASE)

    # Optional cleanup
    raw_text = re.sub(r'\n+', '\n', raw_text)
    raw_text = re.sub(r'\s{2,}', ' ', raw_text)

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
    HF_TOKEN = "write your own hugging face API here....."
    API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a strict computer science examiner. Your job is to grade answers for accuracy.

Evaluate whether the student's answer is factually correct.

Scoring rules:
- If the answer is wrong or unrelated: Score 0–3
- If partially correct or vague: Score 4–6
- If fully correct but missing detail: Score 7–9
- If fully correct and well explained: Score 10

Respond **strictly** in the format below — no extra text.

FORMAT:
Score: X/10  
Explanation: [Briefly explain why it's correct or incorrect]  
Suggestions: [Correct the answer or explain what is missing]

Question: {question}
Answer: {answer}
"""

    

    payload = {
        "inputs": prompt.strip(),
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.3,
            "return_full_text": False,
            "stop": ["Question:", "Answer:", "Student:"]
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
                feedback_text = result[0]["generated_text"].strip()

                # Extract only the required parts using regex
                score_match = re.search(r'Score:\s*(\d+)/10', feedback_text)
                explanation_match = re.search(r'Explanation:\s*(.*?)Suggestions:', feedback_text, re.DOTALL)
                suggestions_match = re.search(r'Suggestions:\s*(.*)', feedback_text, re.DOTALL)

                score = score_match.group(1).strip() if score_match else "?"
                explanation = explanation_match.group(1).strip() if explanation_match else "N/A"
                suggestions = suggestions_match.group(1).strip() if suggestions_match else "N/A"

                return f"Score: {score}/10\nExplanation: {explanation}\nSuggestions: {suggestions}"
            else:
                return "⚠️ Unexpected response format: " + str(result)
        else:
            return f"⚠️ API Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"⚠️ Request failed: {e}"


if __name__ == "__main__":
    image_path = "Screenshot 2025-06-09 181712.png"  # Change as needed
    raw_text = extract_handwritten_text(image_path)

    print("\n📄 Cleaned OCR Text:\n" + "=" * 40)
    print(raw_text)

    qa_pairs = extract_qa_pairs(raw_text)

    if not qa_pairs:
        print("\n❌ No Q&A pairs detected. Please check OCR formatting.")
    else:
        print(f"\n✅ {len(qa_pairs)} Q&A pairs extracted from image.\n")
        for i, (q, a) in enumerate(qa_pairs, 1):
            print(f"\n--- 📝 Evaluating Question {i} ---")
            print(f"Q: {q}")
            print(f"A: {a}")
            feedback = evaluate_with_huggingface(q, a)
            print("📊 Evaluation Result:")
            print(feedback)

# app.py
import streamlit as st
from newproject import extract_handwritten_text, extract_qa_pairs, evaluate_with_huggingface
import tempfile
import os

st.set_page_config(page_title="OCR Answer Grader", layout="centered")

st.title("🧠 OCR Answer Evaluator")
st.markdown("Upload a handwritten answer sheet image to extract and evaluate answers automatically.")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    st.image(temp_path, caption="Uploaded Image", use_column_width=True)

    if st.button("🧪 Extract and Evaluate"):
        with st.spinner("Running OCR and Evaluation..."):
            raw_text = extract_handwritten_text(temp_path)
            qa_pairs = extract_qa_pairs(raw_text)

            if not qa_pairs:
                st.warning("⚠️ No Q&A pairs found in the image.")
            else:
                st.subheader("📄 Extracted Questions & Evaluations")
                for idx, (q, a) in enumerate(qa_pairs, 1):
                    st.markdown(f"### Q{idx}: {q}")
                    st.markdown(f"**Answer:** {a}")
                    feedback = evaluate_with_huggingface(q, a)
                    st.code(feedback)

    os.remove(temp_path)

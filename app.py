import streamlit as st
from ocr_extract import ocr_image, verify_id_card

st.title("OCR Fake ID / Document Detection")
st.write("Upload an ID or Document to check if it's Real or Fake.")

uploaded_file = st.file_uploader("Upload an ID or Document", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # OCR extraction
    extracted_text = ocr_image(uploaded_file)
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Verification
    status, reason = verify_id_card(extracted_text)
    st.subheader("Verification Result:")
    if status == "Real":
        st.success(f"✅ Real ID - {reason}")
    else:
        st.error(f"❌ Fake ID - {reason}")



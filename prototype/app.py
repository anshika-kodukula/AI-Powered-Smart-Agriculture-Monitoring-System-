import streamlit as st
from disease_detection import predict_disease
from pest_detection import detect_pests
from yield_prediction import predict_yield

st.title("AI-Powered Smart Agriculture Monitoring System")

uploaded_file = st.file_uploader(
    "Upload Drone Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(uploaded_file, caption="Drone Image")

    disease, confidence = predict_disease()
    pests = detect_pests()
    predicted_yield = predict_yield()

    st.subheader("Analysis Results")

    st.write(f"Disease Detected: {disease}")
    st.write(f"Confidence: {confidence}%")
    st.write(f"Pests Detected: {pests}")
    st.write(f"Predicted Yield: {predicted_yield}")

    st.subheader("Recommendation")
    st.success(
        "Apply fungicide and monitor irrigation schedule."
    )
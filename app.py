import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

from makesyntaxtree import parse_c_file
from cloadfiles import pareser_to_vector
from ml_data_visualization import FEATURE_LIST

# ----------------------------
# PAGE SETUP
# ----------------------------
st.set_page_config(page_title="C/C++ Malware Detector", layout="wide")
st.title("🛡️ C/C++ Malware Detection using Logistic Regression")

# ----------------------------
# LOAD MODEL
# ----------------------------
MODEL_PATH = "logistic_model_v1.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("⚠️ Model file not found! Please train and save it first.")
    st.stop()

model = joblib.load(MODEL_PATH)

# ----------------------------
# FILE UPLOAD SECTION
# ----------------------------
st.subheader("📂 Upload a C or C++ Source File")

uploaded_file = st.file_uploader(
    "Drag and drop or select a file", type=["c", "cpp"]
)

if uploaded_file is not None:
    # Read the uploaded file
    code = uploaded_file.read().decode("utf-8")

    # Save temporarily to disk for Clang parser (if required)
    temp_path = "temp_upload.c"
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(code)

    # Display uploaded code
    with st.expander("📄 View Uploaded Code"):
        st.code(code, language="c")

    # ----------------------------
    # FEATURE EXTRACTION
    # ----------------------------
    st.subheader("🔍 Feature Extraction in Progress...")
    try:
        node_kinds = parse_c_file(temp_path)
        xvec = pareser_to_vector(node_kinds, FEATURE_LIST).reshape(1, -1)

        # Convert to DataFrame for nice display
        feature_df = pd.DataFrame(xvec, columns=FEATURE_LIST)

        with st.expander("🧩 Extracted Feature Vector"):
            st.dataframe(feature_df.T)

        # ----------------------------
        # PREDICTION
        # ----------------------------
        st.subheader("🧠 Model Prediction")
        pred = model.predict(xvec)[0]

        if pred == 0:
            st.success("✅ This file appears **Benign**.")
        elif pred == 1:
            st.error("⚠️ This file appears **Malicious**.")

    except Exception as e:
        st.error(f"Error during parsing or prediction: {e}")

    # Clean up temporary file
    if os.path.exists(temp_path):
        os.remove(temp_path)

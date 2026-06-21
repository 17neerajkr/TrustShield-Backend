import streamlit as st
from predict import predict_scam
from modules.rules import analyze_rules
from modules.risk_calculator import calculate_final_risk
import easyocr
from PIL import Image
import numpy as np

# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="JobShield AI",
    page_icon="🛡️",
    layout="wide"
)

# ============================================
# OCR Loader
# ============================================

@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en'])

reader = load_ocr()

# ============================================
# Header
# ============================================

st.title("🛡️ JobShield AI")
st.subheader("AI-Powered Job Scam Detection System")

st.markdown(
    "Analyze job messages using Machine Learning + Rule Engine"
)

# ============================================
# Input Selection
# ============================================

input_method = st.radio(
    "Choose Input Method:",
    ["Text Message", "Screenshot Upload"]
)

user_text = ""

# ============================================
# Text Input
# ============================================

if input_method == "Text Message":

    user_text = st.text_area(
        "Paste the job message here:",
        height=200
    )

# ============================================
# Screenshot Upload
# ============================================

else:

    uploaded_file = st.file_uploader(
        "Upload WhatsApp, Telegram, Email, or LinkedIn screenshot",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Screenshot",
            use_container_width=True
        )

        with st.spinner("Extracting text using OCR..."):

            result = reader.readtext(
                np.array(image),
                detail=0
            )

            user_text = " ".join(result)

        st.success("Text Extracted Successfully!")

        st.text_area(
            "Extracted Text",
            user_text,
            height=150
        )

# ============================================
# Analyze Button
# ============================================

if st.button("🔍 Analyze"):

    if not user_text.strip():

        st.error(
            "Please enter a message or upload an image."
        )

    else:

        # =====================================
        # ML Analysis
        # =====================================

        ml_result = predict_scam(user_text)

        # =====================================
        # Rule Engine Analysis
        # =====================================

        rule_result = analyze_rules(user_text)

        # =====================================
        # Final Risk Analysis
        # =====================================

        final_result = calculate_final_risk(
            ml_result["scam_probability"],
            rule_result["rule_score"]
        )

        # =====================================
        # ML Results
        # =====================================

        st.divider()

        st.header("🤖 Machine Learning Analysis")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Verdict",
                ml_result["verdict"]
            )

            st.metric(
                "Signal",
                ml_result["signal"]
            )

        with col2:

            st.metric(
                "Scam Probability",
                f"{ml_result['scam_probability']}%"
            )

            st.metric(
                "Legitimate Probability",
                f"{ml_result['legitimate_probability']}%"
            )

        st.info(
            ml_result["recommendation"]
        )

        # =====================================
        # Rule Engine Results
        # =====================================

        st.divider()

        st.header("📋 Rule Engine Analysis")

        col3, col4 = st.columns(2)

        with col3:

            st.metric(
                "Risk Level",
                rule_result["risk_level"]
            )

        with col4:

            st.metric(
                "Rule Score",
                f"{rule_result['rule_score']}/100"
            )

        st.subheader("Reasons")

        if rule_result["reasons"]:

            for reason in rule_result["reasons"]:

                st.write(f"• {reason}")

        else:

            st.success(
                "No suspicious indicators detected."
            )

        # =====================================
        # Final Report
        # =====================================

        st.divider()

        st.header("🛡️ Final Report")

        col5, col6, col7 = st.columns(3)

        with col5:

            st.metric(
                "Signal",
                final_result["signal"]
            )

        with col6:

            st.metric(
                "Risk Level",
                final_result["risk_level"]
            )

        with col7:

            st.metric(
                "Trust Score",
                f"{final_result['trust_score']}/100"
            )

        st.progress(
            final_result["final_score"] / 100
        )

        st.write(
            f"Final Risk Score: "
            f"{final_result['final_score']}/100"
        )

        st.warning(
            "Recommendation:\n\n"
            + final_result["recommendation"]
        )

        st.info(
            "Suggested Action:\n\n"
            + final_result["suggested_action"]
        )

        st.success(
            "Safety Tip:\n\n"
            + final_result["safety_tip"]
        )

        # =====================================
        # Final Verdict
        # =====================================

        st.divider()

        st.header("🚨 Scam Detection Verdict")

        if final_result["final_score"] >= 70:

            st.error(
                "⚠️ POTENTIAL JOB SCAM DETECTED"
            )

        elif final_result["final_score"] >= 40:

            st.warning(
                "⚠️ SUSPICIOUS JOB OPPORTUNITY"
            )

        else:

            st.success(
                "✅ LIKELY GENUINE JOB OPPORTUNITY"
            )

        col8, col9 = st.columns(2)

        with col8:

            st.metric(
                "Risk Score",
                f"{final_result['final_score']}/100"
            )

        with col9:

            st.metric(
                "Trust Score",
                f"{final_result['trust_score']}/100"
            )

# from flask import Flask, request, jsonify
# from flask_cors import CORS
#
# from predict import predict_scam
# from modules.rules import analyze_rules
# from modules.risk_calculator import calculate_final_risk
# import easyocr
# import numpy as np
# from PIL import Image
# import io
#
# app = Flask(__name__)
#
# # Allow React frontend to access Flask API
# CORS(app)
# reader = easyocr.Reader(['en'], gpu=False)
#
# @app.route("/analyze-image", methods=["POST"])
# def analyze_image():
#
#     try:
#
#         if "image" not in request.files:
#
#             return jsonify({
#                 "error": "No image uploaded."
#             }), 400
#
#         file = request.files["image"]
#
#         image = Image.open(file.stream)
#
#         extracted_text = reader.readtext(
#             np.array(image),
#             detail=0
#         )
#
#         user_text = " ".join(
#             extracted_text
#         ).strip()
#
#         if not user_text:
#
#             return jsonify({
#                 "error":
#                 "No readable text found in image."
#             }), 400
#
#         ml_result = predict_scam(
#             user_text
#         )
#
#         rule_result = analyze_rules(
#             user_text
#         )
#
#         final_result = calculate_final_risk(
#             ml_result["scam_probability"],
#             rule_result["rule_score"]
#         )
#
#         return jsonify({
#
#             "success": True,
#
#             "extracted_text":
#             user_text,
#
#             "ml_analysis":
#             ml_result,
#
#             "rule_analysis":
#             rule_result,
#
#             "final_analysis":
#             final_result
#
#         })
#
#     except Exception as e:
#
#         return jsonify({
#
#             "success": False,
#
#             "error": str(e)
#
#         }), 500
#
# @app.route("/")
# def home():
#
#     return jsonify({
#         "message": "JobShield AI API is running",
#         "status": "success"
#     })
#
#
#
# @app.route("/analyze", methods=["POST"])
# def analyze():
#
#     try:
#
#         data = request.get_json()
#
#         if not data:
#
#             return jsonify({
#                 "error": "No JSON data received"
#             }), 400
#
#         user_text = data.get(
#             "message",
#             ""
#         ).strip()
#
#         if not user_text:
#
#             return jsonify({
#                 "error": "Message cannot be empty"
#             }), 400
#
#         # ==============================
#         # Machine Learning Analysis
#         # ==============================
#
#         ml_result = predict_scam(
#             user_text
#         )
#
#         if ml_result.get("status") == "Error":
#
#             return jsonify({
#                 "error": ml_result["message"]
#             }), 400
#
#         # ==============================
#         # Rule Engine Analysis
#         # ==============================
#
#         rule_result = analyze_rules(
#             user_text
#         )
#
#         # ==============================
#         # Final Risk Analysis
#         # ==============================
#
#         final_result = calculate_final_risk(
#             ml_result["scam_probability"],
#             rule_result["rule_score"]
#         )
#
#         return jsonify({
#
#             "success": True,
#
#             "input_message": user_text,
#
#             "ml_analysis": ml_result,
#
#             "rule_analysis": rule_result,
#
#             "final_analysis": final_result
#         })
#
#     except Exception as e:
#
#         return jsonify({
#
#             "success": False,
#
#             "error": str(e)
#
#         }), 500
#
#
# if __name__ == "__main__":
#
#     app.run(
#         host="0.0.0.0",
#         port=8080,
#         debug=True
#     )
#
import joblib

# ============================================
# Load Model and Vectorizer
# ============================================

print("Loading JobShield AI...")

# model = joblib.load("models/model.pkl")
# vectorizer = joblib.load("models/vectorizer.pkl")
import os

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "vectorizer.pkl"
)

model = joblib.load(MODEL_PATH)

vectorizer = joblib.load(
    VECTORIZER_PATH
)
print("JobShield AI is ready!\n")


# ============================================
# Prediction Function
# ============================================

def predict_scam(text):

    if not text.strip():
        return {
            "status": "Error",
            "message": "Input text cannot be empty."
        }

    transformed_text = vectorizer.transform([text])

    prediction = model.predict(transformed_text)[0]

    probabilities = model.predict_proba(transformed_text)[0]

    scam_probability = probabilities[1] * 100
    legitimate_probability = probabilities[0] * 100

    # Verdict System
    if scam_probability >= 70:
        verdict = "Scam"
        signal = "🔴"
        recommendation = (
            "Do NOT share personal information or make payments. "
            "Verify the source before proceeding."
        )

    elif scam_probability >= 40:
        verdict = "Suspicious"
        signal = "🟡"
        recommendation = (
            "Proceed with caution. Verify company details, "
            "email domains, and communication channels."
        )

    else:
        verdict = "Legitimate"
        signal = "🟢"
        recommendation = (
            "No major scam indicators detected. "
            "However, always remain vigilant."
        )

    return {
        "signal": signal,
        "verdict": verdict,
        "scam_probability": round(scam_probability, 2),
        "legitimate_probability": round(legitimate_probability, 2),
        "recommendation": recommendation
    }


# ============================================
# Main Program
# ============================================

if __name__ == "__main__":

    print("=" * 60)
    print("🛡️         WELCOME TO JOBSHIELD AI")
    print("=" * 60)

    user_text = input("\nEnter text to analyze:\n\n")

    result = predict_scam(user_text)

    if result.get("status") == "Error":
        print("\n❌", result["message"])

    else:
        print("\n" + "=" * 60)
        print("🔍 ANALYSIS RESULT")
        print("=" * 60)

        print(
            f"\nSignal: {result['signal']}"
        )

        print(
            f"Verdict: {result['verdict']}"
        )

        print(
            f"Scam Probability: "
            f"{result['scam_probability']}%"
        )

        print(
            f"Legitimate Probability: "
            f"{result['legitimate_probability']}%"
        )

        print(
            f"\nRecommendation:\n"
            f"{result['recommendation']}"
        )

        print("\n" + "=" * 60)


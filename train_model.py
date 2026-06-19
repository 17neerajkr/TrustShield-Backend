# import pandas as pd
# import joblib

# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import (
#     accuracy_score,
#     classification_report,
#     confusion_matrix
# )

# # ============================================
# # Load Cleaned Dataset
# # ============================================

# print("Loading dataset...")

# df = pd.read_csv(
#     "datasets/final_jobshield_dataset_cleaned.csv"
# )

# print("\nDataset Loaded Successfully!")
# print("Dataset Shape:", df.shape)

# # ============================================
# # Check Missing Values
# # ============================================

# print("\nChecking Missing Values...")

# print(df[
#     [
#         "combined_text",
#         "fraudulent"
#     ]
# ].isnull().sum())

# # ============================================
# # Features and Labels
# # ============================================

# X = df["combined_text"]

# y = df["fraudulent"]

# print("\nFraudulent Distribution:")

# print(y.value_counts())

# # ============================================
# # Split Dataset
# # ============================================

# print("\nSplitting Dataset...")

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.20,
#     random_state=42,
#     stratify=y
# )

# print("\nTraining Samples:", len(X_train))

# print("Testing Samples:", len(X_test))

# # ============================================
# # TF-IDF Vectorization
# # ============================================

# print("\nApplying TF-IDF Vectorization...")

# vectorizer = TfidfVectorizer(
#     stop_words="english",
#     max_features=10000,
#     ngram_range=(1, 2)
# )

# X_train_vectorized = vectorizer.fit_transform(
#     X_train
# )

# X_test_vectorized = vectorizer.transform(
#     X_test
# )

# print("\nVectorization Completed!")

# print(
#     "Training Matrix Shape:",
#     X_train_vectorized.shape
# )

# # ============================================
# # Train Model
# # ============================================

# print("\nTraining Logistic Regression Model...")

# model = LogisticRegression(
#     max_iter=1000,
#     random_state=42
# )

# model.fit(
#     X_train_vectorized,
#     y_train
# )

# print("\nModel Training Completed!")

# # ============================================
# # Predictions
# # ============================================

# y_pred = model.predict(
#     X_test_vectorized
# )

# # ============================================
# # Evaluation
# # ============================================

# accuracy = accuracy_score(
#     y_test,
#     y_pred
# )

# print(
#     "\nModel Accuracy:",
#     round(accuracy * 100, 2),
#     "%"
# )

# print("\nClassification Report:\n")

# print(
#     classification_report(
#         y_test,
#         y_pred
#     )
# )

# print("\nConfusion Matrix:\n")

# print(
#     confusion_matrix(
#         y_test,
#         y_pred
#     )
# )

# # ============================================
# # Save Model
# # ============================================

# joblib.dump(
#     model,
#     "models/model.pkl"
# )

# joblib.dump(
#     vectorizer,
#     "models/vectorizer.pkl"
# )

# print("\nModel saved successfully!")

# print("Vectorizer saved successfully!")

# print("\nFiles Created:")

# print("models/model.pkl")

# print("models/vectorizer.pkl")

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ============================================
# Load Cleaned Dataset
# ============================================

print("Loading dataset...")

df = pd.read_csv(
    "datasets/final_jobshield_dataset_cleaned.csv"
)

print("\nDataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# ============================================
# Check Missing Values
# ============================================

print("\nChecking Missing Values...")

print(
    df[
        [
            "combined_text",
            "fraudulent"
        ]
    ].isnull().sum()
)

# ============================================
# Features and Labels
# ============================================

X = df["combined_text"]
y = df["fraudulent"]

print("\nFraudulent Distribution:")
print(y.value_counts())

# ============================================
# Split Dataset
# ============================================

print("\nSplitting Dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# ============================================
# TF-IDF Vectorization
# ============================================

print("\nApplying TF-IDF Vectorization...")

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=10000,
    ngram_range=(1, 2)
)

X_train_vectorized = vectorizer.fit_transform(
    X_train
)

X_test_vectorized = vectorizer.transform(
    X_test
)

print("\nVectorization Completed!")

print(
    "Training Matrix Shape:",
    X_train_vectorized.shape
)

# ============================================
# Train Model
# ============================================

print("\nTraining Logistic Regression Model...")

model = LogisticRegression(
    max_iter=1000,
    random_state=42,
    multi_class='auto',
    solver='lbfgs'
)

model.fit(
    X_train_vectorized,
    y_train
)

print("\nModel Training Completed!")

# ============================================
# Predictions
# ============================================

y_pred = model.predict(
    X_test_vectorized
)

# ============================================
# Evaluation
# ============================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(
    "\nModel Accuracy:",
    round(accuracy * 100, 2),
    "%"
)

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred
    )
)

print("\nConfusion Matrix:\n")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

# ============================================
# Save Model
# ============================================

joblib.dump(
    model,
    "models/model.pkl"
)

joblib.dump(
    vectorizer,
    "models/vectorizer.pkl"
)

print("\nModel saved successfully!")
print("Vectorizer saved successfully!")

print("\nFiles Created:")
print("models/model.pkl")
print("models/vectorizer.pkl")


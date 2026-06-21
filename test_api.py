import requests

API_URL = "https://trustshield-backend-production.up.railway.app/"

# API_URL = "http://127.0.0.1:5000"
response = requests.post(
    f"{API_URL}/analyze",
    json={
        "message": (
            "Congratulations! You have been selected. "
            "No interview is required. "
            "Pay ₹2500 registration fee "
            "and send Aadhaar Card via WhatsApp."
        )
    }
)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())
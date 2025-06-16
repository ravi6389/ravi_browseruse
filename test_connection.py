import requests

GROQ_API_KEY = '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'  # <-- use your actual key



response = requests.get(
    "https://api.groq.com/openai/v1/models",
    headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
    verify=False
)
print(response.status_code)
print(response.json())

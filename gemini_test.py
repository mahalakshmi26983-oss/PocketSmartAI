from google import genai
from dotenv import load_dotenv
import os

load_dotenv("D:/PocketSmartAI/.env")

api_key = os.getenv("GOOGLE_API_KEY")

print("API key loaded:", bool(api_key))

if not api_key:
    print("ERROR: GOOGLE_API_KEY not found in .env")
    exit()

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello! Give me a one-line greeting."
)

print(response.text)
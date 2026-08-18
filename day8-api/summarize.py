import os
import sys
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in .env")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Usage: python summarize.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, "r", encoding="utf-8") as file:
        document = file.read()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

genai.configure(api_key=api_key)
for m in genai.list_models():
    print(m.name)

model = genai.GenerativeModel("gemini-3.6-flash")

prompt = f"""
Summarize the document below.

Return ONLY valid JSON in this format:

{{
  "summary": "string",
  "key_points": ["point1", "point2", "point3"],
  "word_count": number
}}

Document:
{document}
"""

try:
    response = model.generate_content(prompt)

    clean_text = response.text.strip()

    if clean_text.startswith("```json"):
        clean_text = clean_text.replace("```json", "").replace("```", "").strip()

    result = json.loads(clean_text)
    
    print("\nSUMMARY:")
    print(result["summary"])

    print("\nKEY POINTS:")
    for point in result["key_points"]:
        print("-", point)

    print("\nWORD COUNT:")
    print(result["word_count"])

except Exception as e:
    print("Request failed:", e)
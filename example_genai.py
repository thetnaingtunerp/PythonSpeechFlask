from google import genai
# pip install google-genai
# pip install -q -U google-genai

client = genai.Client(api_key="AIzaSyBvTIhZ0ZfUn8-gIAddFchtyx-tvB5YkGY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)
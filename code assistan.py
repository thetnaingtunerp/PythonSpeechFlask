from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyBvTIhZ0ZfUn8-gIAddFchtyx-tvB5YkGY")

response = client.models.generate_content(
      model="gemini-2.5-flash",
      contents="python Flask app တစ်ခု တည်ဆောက်ပြပေးပါ။",
      config=types.GenerateContentConfig(
          tools=[types.Tool(code_execution=types.ToolCodeExecution)]
      ),
  )

for part in response.candidates[0].content.parts:
      if part.text is not None:
          print(part.text)
      if part.executable_code is not None:
          print(part.executable_code.code)
      if part.code_execution_result is not None:
          print(part.code_execution_result.output)

print('Done')  
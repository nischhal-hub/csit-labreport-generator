from google import genai
from google.genai import types

# set GEMINI_API_KEY environment variable with api key.
client = genai.Client()

json_schema = types.Schema(
    type="OBJECT",
    properties={
        "topic": types.Schema(type="STRING"),
        "objective": types.Schema(
            type="ARRAY",
            items=types.Schema(type="STRING")
        ),
        "theory": types.Schema(type="STRING"),
        "implementation": types.Schema(type="STRING"),
        "conclusion": types.Schema(type="STRING")
    }
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=" Write a program to find the largest and smallest element in an array using foreach loop.",
    config=types.GenerateContentConfig(
        responseMimeType="application/json",
        responseSchema=json_schema,
        temperature=0.2,
    )
    
)


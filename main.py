from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="give me a latin quote and its translation"
)
print(interaction.output_text)
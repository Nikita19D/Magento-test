import os
from dotenv import load_dotenv
from fastapi import FastAPI
from google import genai

load_dotenv()

app=FastAPI()

items=[]


@app.get ("/")
def root():
    return{"Hello":"World"}

@app.post("/items")
def create_item(item:str):
    items.append(item)
    return item


"""client = genai.Client(api_key=os.getenv("API_KEY"))

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="write a latin quote and a english traslation of it"
    #input="Create a simple html magento sample"
)
print(interaction.output_text)"""
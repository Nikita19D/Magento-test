import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

load_dotenv()

app=FastAPI()

class Item(BaseModel):
    text:str=None
    is_done:bool = False

items=[]


@app.get ("/")
def root():
    return{"Hello":"World"}

@app.post("/items") 
def create_item(item:Item):
    items.append(item)
    return items

@app.get("/items", response_model=list[Item]) 
def list_items(limit:int=10):
    return items[0:limit]


@app.get ("/items/{item_id}", response_model=Item)
def get__item(item_id:int) -> Item:
    if item_id<len(items):
        item =items[item_id]
        return item
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")



"""client = genai.Client(api_key=os.getenv("API_KEY"))

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="write a latin quote and a english traslation of it"
    #input="Create a simple html magento sample"
)
print(interaction.output_text)"""
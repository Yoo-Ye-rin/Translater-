from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from datetime import datetime
import uvicorn
import json
import base64
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI()

client = OpenAI(
    api_key="sk-XXXX")

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    message: str

    #번역 함수


def gpt_response(message: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates text into Korean."},
            {"role": "user", "content": message}
        ]
    )

    return completion.choices[0].message.content


#REST API: POST / translate
@app.post("/translate", response_model=Message)
def translate(msg: Message):
    #try:
    print(msg)
    result = gpt_response(msg.message)
    print(result)

    return Message(message=result)


#except Exception as e:
#    raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)

# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # atau ganti ke ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str  # "user" atau "assistant"
    text: str

class ChatRequest(BaseModel):
    messages: List[Message]

class ChatResponse(BaseModel):
    reply: str

# Config: ubah model_name jika mau model lain (flan-t5-small/medium/large)
MODEL_NAME = os.environ.get("MODEL_NAME", "Aqilfikri/aqil-ai")
MAX_INPUT_LENGTH = 512  # token limit (bahu2 sesuai model)
MAX_OUTPUT_LENGTH = 512

# Load model & tokenizer (single global)
print("Loading model:", {MODEL_NAME})
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()
print("Model loaded on", device)

def build_prompt(messages: List[Dict[str, Any]]) -> str:
    user_messages = [m["text"] for m in messages if m["role"] == "user"]
    last_input = user_messages[-1] if user_messages else ""

    return f"Buatkan cerita berdasarkan kata kunci: {last_input}"

@app.options("/chat")
def chat_options():
    return JSONResponse(status_code=200, content={"message": "OK"})

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    messages = [m.dict() for m in req.messages]
    prompt = build_prompt(messages)

    # Tokenisasi input
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=MAX_INPUT_LENGTH).to(device)

    # Generate output
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=256,
            min_length=50,
            temperature=0.9,
            top_p=0.95,
            repetition_penalty=1.2,
            do_sample=True,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id,
        )

    reply = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Bersihkan hasil agar tidak mengulang prompt
    if reply.startswith(prompt):
        reply = reply[len(prompt):].strip()
    if not reply:
        reply = "Maaf, saya tidak dapat menghasilkan cerita saat ini."

    return ChatResponse(reply=reply)
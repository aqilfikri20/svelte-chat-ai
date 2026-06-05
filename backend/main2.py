# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Schema
# =========================
class Message(BaseModel):
    role: str
    text: str

class ChatRequest(BaseModel):
    messages: List[Message]

class ChatResponse(BaseModel):
    reply: str

# =========================
# Config
# =========================
MODEL_NAME = "model_cerita7"
MAX_INPUT_LENGTH = 512

print("Loading model:", MODEL_NAME)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()

print("Model loaded on", device)


# =========================
# Cleaning output
# =========================
def clean_text(text):
    replacements = {
        "yang yang": "yang",
        "tidak tidak": "tidak",
        "yap": "",
        "yung": "",
        "dan dan": "dan"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text.strip()

# =========================
# Generate 1 paragraf
# =========================
def generate_story(tema: str):

    prompt = f"""{tema}
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=128
    ).to(device)

    with torch.no_grad():
        bad_words_ids = [
            tokenizer.encode(f"<extra_id_{i}>", add_special_tokens=False)
            for i in range(100)
        ]

        outputs = model.generate(
            **inputs,
            max_new_tokens=4096,
            min_new_tokens=2056,   # 🔥 cukup untuk 10 paragraf
            temperature=0.55,
            top_p=0.7,
            repetition_penalty=1.7,
            no_repeat_ngram_size=5,
            do_sample=True,
            bad_words_ids=bad_words_ids
        )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    result = clean_text(result)

    return result

@app.options("/chat")
def chat_options():
    return JSONResponse(status_code=200, content={"message": "OK"})


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

    messages = [m.dict() for m in req.messages]
    user_messages = [m["text"] for m in messages if m["role"] == "user"]

    if not user_messages:
        return ChatResponse(reply="Silakan masukkan tema cerita.")

    tema = user_messages[-1].strip()

    if not tema:
        return ChatResponse(reply="Tema tidak boleh kosong.")

    try:
        story = generate_story(tema)
        return ChatResponse(reply=story)

    except Exception as e:
        print("ERROR:", str(e))
        return ChatResponse(reply="Terjadi kesalahan saat membuat cerita.")

# =========================
# Debug
# =========================
@app.get("/debug")
def debug_model():

    text = "Di sebuah kota kecil, seorang pemuda hidup sederhana."

    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.encode(text)
    decoded_text = tokenizer.decode(token_ids, skip_special_tokens=True)

    prompt = """
Buat 1 paragraf cerita panjang.

Tema: keadilan
Bagian: orientasi 1
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=120,
            temperature=0.8,
            top_p=0.95,
            repetition_penalty=1.2,
            no_repeat_ngram_size=4,
            do_sample=True
        )

    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {
        "original_text": text,
        "tokens": tokens,
        "token_ids": token_ids,
        "decoded_text": decoded_text,
        "generated_output": generated
    }

# =========================
# Run
# =========================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
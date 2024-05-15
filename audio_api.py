from fastapi import FastAPI, UploadFile
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/audio-fon")
async def audio_fon(audio: UploadFile):
  """
   Transcrire un audio en Fon
  """
  API_URL = "https://api-inference.huggingface.co/models/speechbrain/asr-wav2vec2-dvoice-fongbe"
 
  headers = {"Authorization": "Bearer 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"}
  
  data = await audio.read()

  response = requests.post(API_URL, headers=headers, data=data)

  return response.json()

@app.get("/")
async def welcome():
  return {"message":"Welcome to the GBETCHE transcriber API. You can transcript Fon."}


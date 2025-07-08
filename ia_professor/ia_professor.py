from fastapi import FastAPI, Request
import requests

app = FastAPI()

OLLAMA_URL = "http://llama_professor:11434/api/generate"
OLLAMA_MODEL = "phi"

@app.post("/professor")
async def professor(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")

        print("Prompt recebido pelo professor:")
        print(prompt)

        response = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })

        texto_gerado = response.json().get("response", "").strip()
        return texto_gerado

    except Exception as e:
        print(f"Erro na IA do professor: {e}")
        return f"Erro: {str(e)}"

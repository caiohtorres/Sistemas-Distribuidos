from fastapi import FastAPI, Request
import requests

app = FastAPI()

OLLAMA_URL = "http://llama_aluno:11434/api/generate"
OLLAMA_MODEL = "phi"

@app.post("/aluno")
async def aluno(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")

        print("Recebido prompt do aluno:")
        print(prompt)

        res = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })

        texto_gerado = res.json().get("response", "").strip()
        return texto_gerado

    except Exception as e:
        print(f"Erro ao processar prompt do aluno: {e}")
        return f"Erro: {str(e)}"

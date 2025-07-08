
from fastapi import FastAPI
from modelos import NotasAluno, MatrizConhecimento
from memoria import matriz_materia, feedbacks_alunos
from ia_aluno_client import chamar_ia_aluno
from ia_professor_client import chamar_ia_professor

app = FastAPI()

@app.post("/cadastrar-matriz")
def cadastrar_matriz(matriz: MatrizConhecimento):
    matriz_materia.clear()
    matriz_materia.extend(matriz.topicos)
    return {"msg": "Matriz cadastrada com sucesso."}

@app.post("/notas")
async def receber_notas(aluno: NotasAluno):
    print("input aluno")
    print(aluno)

    resultado = chamar_ia_aluno(aluno.nome, aluno.notas)
    feedback = {"aluno": aluno.nome, "defasagem": resultado.get("defasagem", [])}
    feedbacks_alunos.append(feedback)
    result = {
        "aluno": aluno.nome,
        "recomendacoes": resultado.get("recomendacoes", ""),
        "analise_professor": resultado.get("analise_professor", "")
    }
    print("result")
    print(result)
    return result

@app.get("/status-turma")
def status_turma():
    return chamar_ia_professor(feedbacks_alunos)

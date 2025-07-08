import requests

def chamar_ia_professor(feedbacks: list):
    prompt_base = "Com base nas defasagens dos alunos abaixo:\n"
    for f in feedbacks:
        prompt_base += f"- Aluno: {f['aluno']}, Defasagens: {f['defasagem']}\n"

    prompt_topicos = (
        prompt_base +
        "\nListe os tópicos mais recorrentes entre os alunos com defasagem. "
        "Responda apenas com os nomes dos tópicos, separados por vírgula, em português."
    )

    prompt_resumo = (
        prompt_base +
        "\nGere um resumo geral da situação da turma, com foco nas dificuldades principais. "
        "Responda em português pt-br, com um texto direto e curto."
    )

    try:
        print("tentando - prof")

        response_topicos = requests.post("http://ia_professor:8002/professor", json={"prompt": prompt_topicos})
        topicos_criticos = response_topicos.text.strip()

        response_resumo = requests.post("http://ia_professor:8002/professor", json={"prompt": prompt_resumo})
        resumo_geral = response_resumo.text.strip()

        return {
            "topicos_criticos": topicos_criticos,
            "resumo_geral": resumo_geral
        }

    except Exception as e:
        print(f"Erro ao chamar IA do professor: {e}")
        return {
            "topicos_criticos": "",
            "resumo_geral": "Erro ao obter análise"
        }

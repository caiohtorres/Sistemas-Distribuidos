import requests
from memoria import matriz_materia

def chamar_ia_aluno(nome: str, notas: list):
    prompt_base = f"O aluno {nome} obteve as seguintes notas por tópico da disciplina:\n"
    for i in range(min(len(notas), len(matriz_materia))):
        prompt_base += f"- {matriz_materia[i]}- nota:{notas[i]}\n"

    prompt_defasagem = prompt_base + (
        "\nIdentifique dentre esses acima exclusivamente, sem precisar de outras infos responda em uma linha apenas, quais tópicos estão com nota abaixo de 6 (defasagens) caso existam, se nao retorne que nao há nenhuma. "
        "Responda sempre em português pt-br, em texto simples responda em uma linha apenas."
    )

    prompt_recomendacoes = prompt_base + (
        "\nGere recomendações específicas para cada um deles de forma muito simples, baseado nas infos acima. "
        "Responda sempre em português pt-br, em texto simples responda em uma linha apenas."
    )

    try:
        print(f"nome: {nome} notas: {notas} matriz: {matriz_materia}")
        print("Enviando - defasagem")
        defasagem = requests.post("http://ia_aluno:8001/aluno", json={"prompt": prompt_defasagem}).text.strip()
        print(f"defasagem {defasagem}")

        print("Enviando - recomendações")
        recomendacoes = requests.post("http://ia_aluno:8001/aluno", json={"prompt": prompt_recomendacoes}).text.strip()
        print(f"recomendacoes {recomendacoes}")

        prompt_professor = (
            prompt_base
            + f"\n\nO aluno apresenta as seguintes defasagens:\n{defasagem}\n\n"
            "Diga de forma muito simples como ele está se saindo na disciplina. "
            "Responda sempre em português pt-br."
        )

        print("Enviando - análise para professor")
        analise_professor = requests.post("http://ia_professor:8002/professor", json={"prompt": prompt_professor}).text.strip()

        return {
            "defasagem": defasagem,
            "recomendacoes": recomendacoes,
            "analise_professor": analise_professor
        }

    except Exception as e:
        print(f"Erro ao chamar IA do aluno: {e}")
        return {
            "defasagem": "",
            "recomendacoes": "",
            "analise_professor": ""
        }


# Sistema de IA Educacional com FastAPI + A2A

> Esse é um sistema distribuido que utiliza agentes de IA para dar suporte a professores com relação a identificar dificuldades dos alunos e com isso melhorar a qualidade do conhecimento que é passado para o aluno.

> O sistema utiliza o modelo de IA Llama para dois agentes. O primeiro agente(agente de aluno) é responsável por receber as materias e as notas alcançadas pelo aluno, em seguida ele identifica as matérias com nota abaixo da média(6.00 no caso) e retorna as matérias com nota abaixo da média para o segundo agente(agente de professor), que é responsável por identificar as matérias recebidas e gerar um relatório com as disciplinas com notas abaixo da média

## Tecnologias Utilizadas

```bash
 - Python
 - Docker
 - Llama
```

## Como rodar

```bash
docker compose up --build
```

## Endpoints

- `POST /cadastrar-matriz`: cadastrar tópicos da disciplina
- `POST /notas`: enviar notas de um aluno
- `GET /status-turma`: obter resumo geral via IA do professor

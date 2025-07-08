# Visão Arquitetônica Inicial (Pré-modelagem de Ameaças)

## Objetivo

Esta visão descreve a arquitetura do sistema distribuído antes da aplicação de medidas de segurança. O foco está na definição dos principais componentes, seus papéis e o fluxo de dados entre eles.

---

## Componentes Principais

| Componente                         | Função                                                                 |
|-----------------------------------|------------------------------------------------------------------------|
| Aluno                              | Fornecer materias e notas alcançadas             |
| Agente 1: Tutor Virtual (IA Local) | Receber matérias e notas alcançadas pelo aluno, identificar matérias que |
| ... | a média não foi alcançada e retorna para o segundo agente  |
| Agente 2: Assistente Pedagógico    | Analisa dados recebidos do agente 1, identificar as matérias com menor  |
| ... | desempenho e retorna um relatório para o professor |
| API REST                           | Responsável pela comunicação entre os agentes                         |
| Professor                          | Recebe os relatórios com previsões e recomendações pedagógicas        |

---

## Diagrama de Arquitetura (Abstração)

[Diagrama de fluxo do sistema](Diagrama%20de%20fluxo%20do%20sistema.png)

## Pontos de Atenção(Possíveis Vulnerabilidades)

> * Spoofing(Falsificação de identidade)
> * Tampering(Manipulação de dados)
> * Repudiation(Negação de serviço)
> * Information Disclosure(Divulgação de Informação)
> * Denial of Service(Falsificação de identidade)
> * Elevation Privilege(Elevação de privilegio)

* Ausencia de autenticação para o envio de materiais e notas para o Agente 1(Spoofing/ Tampering /Denial of Service)
* Utilização de HTTP simples
* Possibilidade de interceptação de Dados tanto no envio dos dados para o Agente 1, quanto no relatório retornado pelo agente 2(Informatio Disclousure)




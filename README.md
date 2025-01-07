# Assistente Virtual Elana

Este projeto é um assistente virtual simples chamado Elana, capaz de reconhecer comandos de voz em português e realizar ações como responder perguntas, contar piadas, informar o horário, realizar buscas na internet e mais.

## Funcionalidades
- **Reconhecimento de Voz**: Captura comandos de voz em português.
- **Síntese de Fala**: Responde utilizando áudio gerado dinamicamente.
- **Ações Disponíveis**:
  - Responder a "olá" e outras saudações.
  - Informar o horário atual.
  - Contar piadas.
  - Realizar buscas no Google.
  - Encerrar com o comando "sair".

## Requisitos
- Python 3.x
- Bibliotecas:
  - `speech_recognition`
  - `gTTS`
  - `pygame`
  - `webbrowser`

## Como Executar
1. Clone o repositório ou copie o código para um arquivo local.
2. Instale as dependências necessárias utilizando:
   ```bash
   pip install speechrecognition gtts pygame
   ```
3. Execute o script Python:
   ```bash
   python speech2text.py
   ```
4. Interaja com o assistente via comandos de voz.

## Observações
- Certifique-se de que o microfone esteja configurado e funcionando corretamente.
- O idioma utilizado é o português brasileiro (pt-BR).

## Autor
Projeto criado para demonstração e aprendizado de Python.

## Lista de Piadas
As piadas utilizadas no assistente são selecionadas de uma lista fixa. Exemplos:
- "O que o zero disse para o oito? Belo cinto!"
- "Por que o computador foi preso? Porque ele executou um programa suspeito."
- "Qual é o cúmulo do absurdo? Um elétron perder o ônibus e dizer: 'Poxa, perdi o elétrico!'"

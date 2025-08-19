# 🤖 Chatbot – Ofélia Assistente de Voz

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Licença](https://img.shields.io/badge/Licença-MIT-green)](LICENSE)

**Ofélia** é uma assistente virtual baseada em reconhecimento e síntese de voz, desenvolvido em Python, capaz de responder perguntas pré programadas sobre artistas e curiosidades do mundo da música pop aplicando conceitos de processamento de linguagem natural (PLN) e interação homem-máquina. O projeto foi desenvolvido como **trabalho acadêmico** para a disciplina de **Inteligência Artificial**, no **2º semestre da graduação em Engenharia de Software**.  

---

## 🚀 Funcionalidades  

- 🎤 **Reconhecimento de voz (pt-BR)** em tempo real usando SpeechRecognition.  
- 🔊 **Respostas faladas** com Google Text-to-Speech (gTTS).  
- 🎶 **Banco de conhecimento fixo** com perguntas e respostas sobre música pop.  
- ⏱️ **Execução em loop** até o usuário encerrar a interação com palavras-chave como *“adeus”*, *“tchau”* ou *“sair”*.  
- 📢 **Feedback sonoro (beep)** indicando quando o usuário pode falar.  

---

## 🛠️ Tecnologias Utilizadas  

- **Python 3.10+**  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) → Reconhecimento de voz.  
- [gTTS](https://pypi.org/project/gTTS/) → Síntese de voz.  
- [playsound](https://pypi.org/project/playsound/) → Reprodução de áudio.  
- [Winsound](https://docs.python.org/3/library/winsound.html) → Para beep em Windows.  
- [Threading](https://docs.python.org/3/library/threading.html) → Para execução paralela do beep.  

---

## 📦 Instalação

1. Clone o repositório:

`´git clone https://github.com/MarryKukles/ChatBot-Ofelia-Assistente-de-Voz.git`
`cd ChatBot-Ofelia-Assistente-de-Voz`

2. Instale as dependências:

`pip install SpeechRecognition gtts playsound==1.2.2`

3. Execute o assistente:

`python chatbot ofelia.py`

---

## 📚 Contexto Acadêmico

Este projeto foi desenvolvido como parte dos requisitos da disciplina de Inteligência Artificial, abordando:

Processamento básico de linguagem natural (NLP).

Reconhecimento e síntese de voz.

Estruturação de um chatbot baseado em base de conhecimento fixa.

---

## 📝 Licença
Projeto acadêmico para fins educacionais.

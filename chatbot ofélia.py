import speech_recognition as sr
import time
import sys
import winsound
import os
from threading import Thread
from gtts import gTTS
import playsound


class ChatbotVoz:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Configurações do reconhecimento de voz
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = False
        self.ativo = True

        # Banco de respostas
        self.respostas = {
            "quem é a rainha do pop": "Madonna é considerada a Rainha do Pop pela sua influência cultural, inovações musicais e impacto na moda, performance e liberdade de expressão.",
            "quem é a princesa do pop": "Britney Spears ganhou o título de princesa do pop por revolucionar o pop nos anos 2000, se tornando ícone de uma geração com hits como …Baby One More Time e Toxic.",
            "me diga um marco gay": "Born This Way – Lady Gaga – Lançada em 2011, é considerada um hino da comunidade por celebrar a diversidade e incentivar o orgulho da identidade de cada um.",
            "qual artista com mais prêmios musicais": "Em 2023, Beyoncé se tornou a artista com mais vitórias na história do Grammy, com 32 estatuetas, superando todos os outros artistas.",
            "qual a maior premiação do mundo da música": "Grammy Awards – Conhecido como o 'Oscar da música', é a premiação mais prestigiada da indústria musical, reconhecendo artistas em diversas categorias desde 1959.",
            "qual é a artista feminina mais ouvida no spotify": "Taylor Swift – Recordista em streams e dona de uma base de fãs extremamente fiel, conhecida como Swifties.",
            "qual o videoclipe mais icônico": "Thriller – Michael Jackson – Revolucionou a forma de se produzir videoclipes, com narrativa, dança e efeitos inovadores.",
            "qual o primeiro sucesso de justin bieber": "Baby (2010) – Canção que o lançou para o estrelato e se tornou um marco cultural da internet e da música pop.",
            "adeus": "Até logo! Foi um prazer ajudar você. Sou Ofélia, e estarei aqui quando precisar."
        }

    def beep(self):
        try:
            winsound.Beep(800, 200)
        except:
            print("\a")

    def falar(self, texto):
        """Síntese de voz usando gTTS"""
        print(f"[ASSISTENTE] {texto}")

        try:
            # Áudio temporário
            tts = gTTS(text=texto, lang='pt-br', slow=False)
            temp_file = "temp_response.mp3"
            tts.save(temp_file)

            # Reproduz o áudio
            playsound.playsound(temp_file, True)

            # Remove o arquivo temporário
            os.remove(temp_file)
        except Exception as e:
            print(f"[ERRO] Falha na síntese de voz: {e}")

    def ouvir(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            Thread(target=self.beep).start()

            print("\n[OUVINDO] Fale agora...")
            try:
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=4)
                texto = self.recognizer.recognize_google(audio, language='pt-BR').lower()
                print(f"[USUÁRIO] {texto}")
                return texto
            except sr.UnknownValueError:
                self.falar("Não entendi, pode repetir?")
                return None
            except Exception as e:
                print(f"[ERRO] {e}")
                return None

    def processar(self, comando):
        if not comando:
            return None

        # Verificação do comando de despedida
        if "adeus" in comando or "sair" in comando or "tchau" in comando:
            self.ativo = False
            return self.respostas["adeus"]

        for trigger in self.respostas:
            if trigger in comando:
                resposta = self.respostas[trigger]
                return resposta

        return "Desculpe, não entendi. Pode reformular?"

    def iniciar(self):
        self.falar("Olá! Sou Ofélia, sua assistente virtual. Pode falar após o sinal.")

        while self.ativo:
            try:
                comando = self.ouvir()
                if comando:
                    resposta = self.processar(comando)
                    if resposta:
                        self.falar(resposta)
                        time.sleep(0.5)
            except Exception as e:
                print(f"[ERRO] {e}")
                self.falar("Ocorreu um erro. Vamos tentar novamente.")


if __name__ == "__main__":
    try:
        # Dependências necessárias
        import importlib.util

        if not importlib.util.find_spec('gtts'):
            print("Instalando gTTS...")
            os.system('pip install gtts')
        if not importlib.util.find_spec('playsound'):
            print("Instalando playsound...")
            os.system('pip install playsound==1.2.2')

        bot = ChatbotVoz()
        bot.iniciar()
    except KeyboardInterrupt:
        print("\nEncerrando o assistente...")
    finally:
        # Limpa arquivos temporários
        if os.path.exists("temp_response.mp3"):
            os.remove("temp_response.mp3")
        sys.exit(0)

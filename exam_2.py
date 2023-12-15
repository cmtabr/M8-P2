# Libraries import
import soundfile as sf
import playsound
from pathlib import Path
from txtai.pipeline import TextToSpeech
import os 
# Enviroment variables


# Config
tts = TextToSpeech("NeuML/ljspeech-jets-onnx")
speech_file_path = Path(__file__).parent / "out.mp3"

# Functions
def entrada_texto():
    text = input()
    return text

def save(text):
    speech = tts(text)
    sf.write("out.mp3", speech, 22050)

def delete():
    os.remove(speech_file_path)

def speak():
    playsound.playsound(speech_file_path)
    
# Main section
def main():
    print("Conta no meu ouvido que eu reproduzo")
    text = entrada_texto()
    while True: 
        if text == "exit":
            break
        if text != "":
            save(text)
            speak()
            delete()
            break
    main()

if __name__ == '__main__':
    main()
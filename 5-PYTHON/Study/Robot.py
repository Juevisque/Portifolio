import playsound as ps
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "Your_Api"

lang = "pt"

openai.api_key = api_key

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio, language="Pt")
                print(said)

                if "centroide" or "synthroid" in said:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.br")
                    speech.save("Answer.mp3")
                    ps.playsound("Answer.mp3")
            except Exception as error:
                print(error)

            return said
        
    get_audio() 
import pyttsx3
text_speech=pyttsx3.init()
print("Welcome to RoboSpeaker")
while True:
    answer=input("what u want me to say")
    if answer == "exit":
       break
    text_speech.say(answer)
    text_speech.runAndWait()
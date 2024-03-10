import pyttsx3
text_speech=pyttsx3.init()
print("Welcome to Robo Speaker - By Amritansh Raizada!! : ")

while(True):
    answer=input("Enter you Text Kids!! : ")
    if answer=="":
        print("No valid text to recognize")
        break

    text_speech.say(answer)
    text_speech.runAndWait()

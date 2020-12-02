from googlecontroller import GoogleAssistant

host = "192.168.0.4" #again your google homes ip
home = GoogleAssistant(host=host)
print("Type speed of tts")
speed = str(input())
print("Type for TTS")
while True:
    data = input()  
    home.say(data, speed=speed, lang = 'en-US')
from googlecontroller import GoogleAssistant

host = "192.168.0.4"
home = GoogleAssistant(host=host)
print("Type Your Volume 0.01 to 0.99/1")
home.volume(volumelevel=float(input()))
print("Type speed of tts")
speed = str(input())
print("Type for TTS")
while True:
    data = input()  
    home.say(data, speed=speed, lang = 'en-US')


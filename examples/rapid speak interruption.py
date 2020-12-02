from googlecontroller import GoogleAssistant

print("Type your google assistants ip")
host = input()
home = GoogleAssistant(host=host)
print("To end demo hit control + c")
print("Type for TTS Demo")
data = input()
while True:
    home.say(data, ignore=True)


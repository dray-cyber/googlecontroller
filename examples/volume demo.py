from googlecontroller import GoogleAssistant

host = "192.168.0.4" # your google assistant ip this is mine
home = GoogleAssistant(host=host)
print("Type Your Volume 0.01 to 0.99/1")
home.volume(volumelevel=float(input()))

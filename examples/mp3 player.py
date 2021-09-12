from googlecontroller import GoogleAssistant

host = "192.168.0.4" #again your google homes ip
home = GoogleAssistant(host=host)

home.serve_media("Victory.mp3", "C:/Users/Dray-Cyber/Documents/GitHub/googlecontroller/examples")

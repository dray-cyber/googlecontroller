from pyngrok import ngrok
import pychromecast
import threading
import socket
import time
import os
global http_tunnel
http_tunnel = None
hostname = socket.gethostname()
YourPrivateIpAddress = socket.gethostbyname(hostname)
print(YourPrivateIpAddress)
name = "googlecontroller"
__all__ = 'GoogleAssistant'
def httpserver(path):
    os.chdir(path)
    if os.name == 'nt':
        os.system('cmd /k "python -m http.server 80 --bind 127.0.0.1"')
    else:
        os.system('cmd /k "python -m SimpleHTTPServer 80 --bind 127.0.0.1"')
class GoogleAssistant:
    def __init__(self, host = None):
        try:
            if host != None:
                self.cc = pychromecast.Chromecast(host)
            else:
                print('For a host input the ip and have the option like: host = "192.168.0.whatever" home = GoogleHome(host=host) ')
        except:
            print("Some sort of error occured most likely a bad connection or ip adress")
    def play(self, url, ignore = False, contenttype = 'audio/mp3'):
        if self.cc.media_controller.status.player_state != "PLAYING" or ignore == True:
            self.cc.wait()
            media = self.cc.media_controller
            media.play_media(url, contenttype)
            media.block_until_active()
    def serve_media(self, media, folder, opentunnel = 1):
        global http_tunnel
        if opentunnel == 0:
            serverhttp = threading.Thread(target=httpserver, args=(folder,))
            serverhttp.start()
            http_tunnel = ngrok.connect(bind_tls=True)
            time.sleep(3)
            print("You are all set now!")
        url = "http://" + YourPrivateIpAddress + ":8000/" + str(media)
        http_tunnels = str(http_tunnel)
        spliced = http_tunnels.split('"')[1]
        ngrokurlpartone = spliced.split('"')[0]
        ngrokurl = ngrokurlpartone + "/" + str(media)
        print(ngrokurl)
        self.play(ngrokurl)
        time.sleep(1)
    def say(self, text, speed = 1, ignore = False, lang = 'en-US'):
        speed = str(speed)
        url = u"https://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "%21&tl=" + lang + "&ttsspeed=" + speed + "&total=1&idx=0&client=tw-ob&textlen=14&tk=594228.1040269"
        self.play(url, ignore)
    def volume(self, volumelevel):
        volumelevel = volumelevel // 100
        self.cc.set_volume(volumelevel)

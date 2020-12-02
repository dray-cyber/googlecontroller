import pychromecast
name = "googlecontroller"
__all__ = 'GoogleAssistant'
class GoogleAssistant:
    def __init__(self, host = None):
        try:
            if host != None:
                self.cc = pychromecast.Chromecast(host)
            else:
                print('For a host input the ip and have the option like: host = "192.168.0.whatever" home = GoogleHome(host=host) ')
        except:
            print("Some sort of error occured most likely a bad connection or ip adress")
    def play(self, url, contenttype = 'audio/mp3'):
        self.cc.wait()
        mc = self.cc.media_controller
        mc.play_media(url, contenttype)
        mc.block_until_active()
    def say(self, text, speed = 1, lang = 'en-US'):
        speed = str(speed)
        url = u"https://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "%21&tl=" + lang + "&ttsspeed=" + speed + "&total=1&idx=0&client=tw-ob&textlen=14&tk=594228.1040269"
        self.play(url)
    def volume(self, volumelevel):
        self.cc.set_volume(volumelevel)
